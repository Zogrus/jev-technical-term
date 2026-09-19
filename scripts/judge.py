"""文字起こしを時間窓に区切り、用語候補をJevに判定させて結果をキャッシュする。

クールダウン等の時系列ルールはここでは適用しない(timeline.py側)。
こうしておくと、しきい値を変えてもJevを呼び直さずに済む。
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API_URL = "https://api.typesafe.ai/v1/systemone"
WINDOW_SEC = 20
CONTEXT_SEC = 60
TAIL_CHARS = 12  # 窓の境界をまたいだ用語を拾うための、前の窓の末尾


def load_env() -> None:
    for line in (ROOT / ".env").read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"'))


def make_windows(lines: list[dict]) -> list[dict]:
    windows: dict[int, list[dict]] = {}
    for l in lines:
        windows.setdefault(int(l["t"] // WINDOW_SEC), []).append(l)
    out = []
    for idx in sorted(windows):
        start = idx * WINDOW_SEC
        text = "".join(l["text"] for l in windows[idx])
        context = "".join(l["text"] for l in lines if start - CONTEXT_SEC <= l["t"] < start)
        out.append({"start": start, "text": text, "context": context})
    return out


def alias_pattern(alias: str) -> re.Pattern:
    if alias.isascii():  # "PR" が "Pro" に当たらないよう、英字は単語境界つき
        return re.compile(rf"(?<![A-Za-z0-9]){re.escape(alias)}(?![A-Za-z0-9])")
    return re.compile(re.escape(alias))


def find_candidates(window: dict, glossary: list[dict]) -> list[dict]:
    tail = window["context"][-TAIL_CHARS:]
    hay = tail + window["text"]
    found, taken = [], []
    # 長い別名を先に当て、"サブエージェント" の中の "エージェント" を二重に拾わない
    pairs = sorted(((a, t) for t in glossary for a in t["aliases"]), key=lambda p: -len(p[0]))
    for alias, term in pairs:
        for m in alias_pattern(alias).finditer(hay):
            if m.end() <= len(tail) or any(s < m.end() and m.start() < e for s, e in taken):
                continue
            taken.append((m.start(), m.end()))
            if term["id"] not in [f["id"] for f in found]:
                found.append({"id": term["id"], "matched": alias})
    return found


def build_request(window: dict, candidates: list[dict], by_id: dict) -> dict:
    questions = {
        "unknown_term": {
            "type": "noul",
            "instructions": "「現在の発話」に、AIやプログラミングの初心者が知らない可能性が高い専門用語・略語・製品名が含まれているか",
        }
    }
    for c in candidates:
        term = by_id[c["id"]]
        questions[f"{c['id']}__tech"] = {
            "type": "noul",
            "instructions": f"「現在の発話」の中の「{c['matched']}」という語は、{term['sense']}の意味で使われているか",
            "criteria": {"true": "その意味で使われている", "false": "別の意味、一般的な日常語、または音声認識の誤り"},
        }
        questions[f"{c['id']}__need"] = {
            "type": "score",
            "instructions": f"AIやプログラミングの初心者が「現在の発話」の話の流れについていくために、「{term['display']}」という用語の意味を知っていることはどれくらい必要か",
            "criteria": [
                "不要。軽く触れただけで、知らなくても話についていける",
                "知っていると理解が深まる",
                "必要。知らないと何の話をしているのか分からなくなる",
            ],
        }
    return {
        "model": "jev-latest",
        "state": {"直前の文脈": window["context"][-400:], "現在の発話": window["text"]},
        "questions": questions,
    }


def call_jev(payload: dict) -> tuple[dict, float]:
    body = json.dumps(payload).encode()
    for attempt in range(6):
        req = urllib.request.Request(API_URL, data=body, headers={
            "Authorization": f"Bearer {os.environ['JEV_API_KEY']}",
            "Content-Type": "application/json",
            "User-Agent": "jev-technical-term/0.1",
        })
        t0 = time.perf_counter()
        try:
            with urllib.request.urlopen(req, timeout=30) as res:
                return json.loads(res.read()), time.perf_counter() - t0
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 529):
                raise RuntimeError(f"{e.code}: {e.read().decode()[:500]}") from e
            time.sleep(2 ** attempt)
        except urllib.error.URLError:  # DNS失敗など一時的な通信エラー
            time.sleep(2 ** attempt)
    raise RuntimeError("retries exhausted")


def main(transcript: Path, out: Path) -> None:
    load_env()
    glossary = json.loads((ROOT / "glossary.json").read_text())
    by_id = {t["id"]: t for t in glossary}
    lines = [json.loads(l) for l in transcript.read_text().splitlines()]
    windows = make_windows(lines)

    def work(w: dict) -> dict:
        cands = find_candidates(w, glossary)
        res, latency = call_jev(build_request(w, cands, by_id))
        return {**w, "candidates": cands, "answers": res["answers"], "usage": res["usage"], "latency": latency}

    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(work, windows))
    out.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in results))
    print(f"{len(results)} windows judged -> {out}")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
