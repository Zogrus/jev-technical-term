"""検証: 用語集の全語をJevに「この発話で使われているか」と聞く方式(全量方式)を、文字起こし全体に流す。

  python3 scripts/alljev_replay.py data/raw/transcript.jsonl

結果は data/alljev_results.jsonl に窓ごとに追記する(途中で止まっても再開できる)。
同じ窓を現行方式(Pythonで照合→必要な語だけJevに聞く)でも判定し、data/current_results.jsonl に保存する。
"""
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "app"))
sys.path.insert(0, str(ROOT / "scripts"))
import server  # noqa: E402
from judge import call_jev, load_env, make_windows  # noqa: E402

CHUNK = 230       # 1回の呼び出しに載せる質問数(1,371語を1回で送ると max_tokens_exceeded になる)
KEEP_MIN = 0.2    # これ以上の確率だけ保存する(しきい値を後から変えて分析するため)
OUT = ROOT / "data/alljev_results.jsonl"
CUR = ROOT / "data/current_results.jsonl"


def main(path: Path) -> None:
    load_env()
    server.load_glossary()
    terms = list(server.matcher.by_id.values())
    chunks = [terms[i:i + CHUNK] for i in range(0, len(terms), CHUNK)]
    lines = [json.loads(l) for l in path.read_text().splitlines()]
    windows = make_windows(lines)
    done = {json.loads(l)["start"] for l in OUT.read_text().splitlines()} if OUT.exists() else set()
    todo = [w for w in windows if w["start"] not in done]
    print(f"用語 {len(terms)}語 / {len(chunks)}分割 / 窓 {len(windows)} (未処理 {len(todo)})", flush=True)

    lock = threading.Lock()

    def ask_chunk(text: str, chunk: list[dict]) -> dict:
        qs = {f"t{i}": {"type": "noul", "instructions": f"これは音声認識による書き起こしである。「現在の発話」の中で、「{t['display']}」({t['sense']})という技術用語が、その意味で使われているか"} for i, t in enumerate(chunk)}
        t0 = time.perf_counter()
        res, _ = call_jev({"model": "jev-latest", "state": {"現在の発話": text}, "questions": qs})
        hits = [{"id": chunk[int(k[1:])]["id"], "p": a["noul"]} for k, a in res["answers"].items() if a["noul"] >= KEEP_MIN]
        return {"hits": hits, "tokens": res["usage"]["input_tokens"], "latency": time.perf_counter() - t0}

    def work(w: dict) -> None:
        text = server.normalize(w["text"])
        t0 = time.perf_counter()
        # 1つの窓の6分割は同時に投げる(本番で1発話を判定するときと同じ形)
        with ThreadPoolExecutor(max_workers=len(chunks)) as inner:
            rs = list(inner.map(lambda c: ask_chunk(text, c), chunks))
        row = {"start": w["start"], "text": w["text"], "wall": round(time.perf_counter() - t0, 2),
               "tokens": sum(r["tokens"] for r in rs), "hits": [h for r in rs for h in r["hits"]]}
        with lock:
            with OUT.open("a") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")

    t0 = time.perf_counter()
    # 同時に2窓まで(=最大12リクエスト、約25万トークン/秒の上限を超えないように)
    with ThreadPoolExecutor(max_workers=2) as pool:
        for i, _ in enumerate(pool.map(work, todo), 1):
            if i % 40 == 0:
                print(f"  {i}/{len(todo)} 窓 完了 ({time.perf_counter() - t0:.0f}秒)", flush=True)
    print(f"全量方式 完了: {time.perf_counter() - t0:.0f}秒", flush=True)

    # 現行方式でも同じ窓を判定して保存(しきい値0で全候補の確率を取る)
    server.TECH_MIN = 0.0
    def cur(w):
        r = server.judge(w["text"], w["context"], 1, False)
        return {"start": w["start"], "latency": r.get("latency", 0), "terms": [{"id": t["key"], "p": t["p"], "matched": t["matched"]} for t in r["terms"]]}
    with ThreadPoolExecutor(max_workers=6) as pool:
        rows = list(pool.map(cur, windows))
    CUR.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows))
    print("現行方式 完了", flush=True)


if __name__ == "__main__":
    main(Path(sys.argv[1]))
