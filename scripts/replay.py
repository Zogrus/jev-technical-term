"""文字起こしを用語集に流して、別名の当たり方を点検する。

  python3 scripts/replay.py data/raw/transcript.jsonl          … 照合だけ(Jevを呼ばない。速い)
  python3 scripts/replay.py data/raw/transcript.jsonl --jev    … Jevの判定まで行い、却下されがちな別名を出す
"""
import collections
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "app"))
sys.path.insert(0, str(ROOT / "scripts"))
import server  # noqa: E402
from judge import load_env, make_windows  # noqa: E402


def main(path: Path, use_jev: bool) -> None:
    load_env()
    server.load_glossary()
    m = server.matcher
    lines = [json.loads(l) for l in path.read_text().splitlines()]
    windows = make_windows(lines)
    print(f"用語集 {len(m.by_id)}語 / 別名 {len(m.pairs)} / 窓 {len(windows)}")

    hits = collections.Counter()
    sample = {}
    for w in windows:
        for c in m.find(w["text"], w["context"], limit=999):
            hits[(c["id"], c["matched"])] += 1
            sample.setdefault((c["id"], c["matched"]), w["text"])
    per_window = sum(hits.values()) / len(windows)
    print(f"照合ヒット: 合計{sum(hits.values())} / 1窓あたり平均{per_window:.1f} / 用語の種類{len({k[0] for k in hits})}")
    print("\n== よく当たる別名(上位40)")
    for (tid, alias), n in hits.most_common(40):
        t = m.by_id[tid]
        print(f"  {n:>4}回 L{t['level']} {alias} → {t['display']}{'  [other有]' if t.get('other') else ''}")
    if not use_jev:
        return

    def work(w):
        try:
            return server.judge(w["text"], w["context"], detect_unknown=False)
        except Exception as e:
            return {"terms": [], "error": str(e)}

    # 却下も見たいので、しきい値を一時的に0にして全候補の確率を取る
    server.TECH_MIN = 0.0
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(work, windows))
    probs = collections.defaultdict(list)
    for w, r in zip(windows, results):
        for t in r["terms"]:
            probs[(t["key"], t["matched"])].append((t["p"], w["text"]))
    print("\n== Jevに却下されがちな別名(平均確率が低い順。誤爆しやすい別名の候補)")
    rows = sorted(((sum(p for p, _ in v) / len(v), k, v) for k, v in probs.items()), key=lambda r: r[0])
    for avg, (tid, alias), v in rows[:40]:
        worst = min(v, key=lambda x: x[0])
        print(f"  平均{avg:.2f} ({len(v)}回) {alias} → {m.by_id[tid]['display']} | 例: …{worst[1][:60]}…")
    shown = collections.Counter()
    for (tid, _), v in probs.items():
        if any(p >= 0.5 for p, _ in v):
            shown[m.by_id[tid]["level"]] += 1
    print(f"\n== 確率0.5以上で一度でも出る用語の種類: 初級{shown[1]} / 中級{shown[2]} / 上級{shown[3]}")
    (ROOT / "data/replay_probs.json").write_text(json.dumps(
        [{"id": k[0], "alias": k[1], "probs": [round(p, 2) for p, _ in v]} for k, v in probs.items()], ensure_ascii=False))


if __name__ == "__main__":
    main(Path(sys.argv[1]), "--jev" in sys.argv)
