"""alljev_replay.py の結果を集計し、全量方式と現行方式を比べる。"""
import collections
import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from glossary_loader import load_terms  # noqa: E402

by_id = {t["id"]: t for t in load_terms()}
A = [json.loads(l) for l in (ROOT / "data/alljev_results.jsonl").read_text().splitlines()]
A.sort(key=lambda r: r["start"])
C = {r["start"]: r for r in map(json.loads, (ROOT / "data/current_results.jsonl").read_text().splitlines())}

tok = sum(r["tokens"] for r in A)
walls = sorted(r["wall"] for r in A)
print(f"窓 {len(A)} / 入力トークン合計 {tok:,} / コスト ${tok / 1e6 * 0.042:.2f} / 1窓あたり ${tok / 1e6 * 0.042 / len(A):.4f}")
print(f"1窓(6分割を同時送信)の所要: 中央値 {statistics.median(walls):.2f}秒 / 90%点 {walls[int(len(walls) * .9)]:.2f}秒 / 最大 {walls[-1]:.2f}秒")


def cards(rows, get_terms, thr, cooldown=600):
    last, n, kinds = {}, 0, set()
    for r in rows:
        for tid, p in get_terms(r):
            if p < thr:
                continue
            if r["start"] - last.get(tid, -1e9) >= cooldown:
                last[tid] = r["start"]; n += 1; kinds.add(tid)
    return n, len(kinds)


cur_rows = [C[r["start"]] for r in A]
for thr in (0.5, 0.7, 0.9):
    n, k = cards(A, lambda r: [(h["id"], h["p"]) for h in r["hits"]], thr)
    print(f"全量方式 しきい値{thr}: 2時間で{n}枚 / 用語{k}種類")
n, k = cards(cur_rows, lambda r: [(t["id"], t["p"]) for t in r["terms"]], 0.5)
print(f"現行方式 しきい値0.5: 2時間で{n}枚 / 用語{k}種類")

THR = 0.7
only_all, only_cur, both = collections.Counter(), collections.Counter(), collections.Counter()
ex_all, ex_cur = {}, {}
for r in A:
    a = {h["id"]: h["p"] for h in r["hits"] if h["p"] >= THR}
    c = {t["id"]: t for t in C[r["start"]]["terms"] if t["p"] >= 0.5}
    for tid in a:
        if tid in c: both[tid] += 1
        else:
            only_all[tid] += 1; ex_all.setdefault(tid, (a[tid], r["text"]))
    for tid in c:
        if tid not in a:
            only_cur[tid] += 1
            pa = next((h["p"] for h in r["hits"] if h["id"] == tid), 0.0)
            ex_cur.setdefault(tid, (pa, c[tid]["matched"], r["text"]))
print(f"\n窓×用語の一致(全量{THR}以上 / 現行0.5以上): 両方 {sum(both.values())} / 全量だけ {sum(only_all.values())} / 現行だけ {sum(only_cur.values())}")

def show(title, counter, ex, fmt):
    print(f"\n== {title}(上位{min(45, len(counter))}種類 / 全{len(counter)}種類)")
    for tid, n in counter.most_common(45):
        print("  " + fmt(tid, n, ex[tid]))

show("全量方式だけが拾った用語", only_all, ex_all,
     lambda tid, n, e: f"{n}回 L{by_id[tid]['level']} {by_id[tid]['display']} p={e[0]:.2f} | …{e[1][:70]}…")
show("現行方式だけが拾った用語", only_cur, ex_cur,
     lambda tid, n, e: f"{n}回 L{by_id[tid]['level']} {by_id[tid]['display']} (一致した別名「{e[1]}」, 全量方式でのp={e[0]:.2f}) | …{e[2][:60]}…")
