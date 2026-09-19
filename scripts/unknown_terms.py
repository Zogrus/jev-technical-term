"""用語集にない語の検出実験: コードで候補を拾い、Jevに4分類させる。"""
import json, re, sys, collections
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from judge import ROOT, load_env, call_jev

CATS = {
    "tech": "AI・プログラミング・IT分野の専門用語、技術の名前、または製品・サービス名",
    "common": "一般的な日常語・ビジネス用語(初心者でも知っている)",
    "proper": "人名・会社名・イベント名・キャラクター名",
    "noise": "音声認識の誤りで意味が分からない語",
}

def main():
    load_env()
    glossary = json.loads((ROOT / "glossary.json").read_text())
    known = [a for t in glossary for a in t["aliases"]]
    rows = [json.loads(l) for l in (ROOT / "data/judgments.jsonl").read_text().splitlines()]
    jobs = []
    for r in rows:
        cands = set(re.findall(r"[ァ-ヴー]{4,}", r["text"])) | set(re.findall(r"(?<![A-Za-z])[A-Z][A-Za-z0-9]{1,}(?![a-z])", r["text"]))
        cands = [c for c in cands if not any(k in c or c in k for k in known)][:12]
        if cands:
            jobs.append((r, cands))

    def work(job):
        r, cands = job
        qs = {f"c{i}": {"type": "choice", "instructions": f"「現在の発話」の中の「{c}」という語は、次のどれに当たるか", "criteria": CATS} for i, c in enumerate(cands)}
        res, _ = call_jev({"model": "jev-latest", "state": {"現在の発話": r["text"]}, "questions": qs})
        return [(c, r["start"], res["answers"][f"c{i}"]) for i, c in enumerate(cands)]

    with ThreadPoolExecutor(max_workers=6) as pool:
        out = [x for xs in pool.map(work, jobs) for x in xs]
    agg = collections.defaultdict(list)
    for c, t, a in out:
        agg[c].append(a)
    summary = []
    for c, answers in agg.items():
        p = {k: sum(a["probabilities"][k] for a in answers) / len(answers) for k in CATS}
        summary.append({"term": c, "n": len(answers), **{k: round(v, 2) for k, v in p.items()}})
    (ROOT / "data/unknown_terms.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1))
    print(f"calls={len(jobs)} candidates={len(out)} unique={len(summary)}")
    for cat in CATS:
        xs = sorted((s for s in summary if max(CATS, key=lambda k: s[k]) == cat), key=lambda s: -s[cat])
        print(f"## {cat} ({len(xs)}):", " / ".join(f"{s['term']}({s[cat]})" for s in xs[:60]))

main()
