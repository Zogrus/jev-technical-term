"""judge.py の判定結果に、しきい値とクールダウンを適用して「技術用語ガイドに何がいつ出るか」を再現する。"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TECH_MIN = 0.7       # 技術用語として使われている確率
NEED_MIN = 0.6       # 理解への必要度 (0〜2)
COOLDOWN_SEC = 20 * 60


def mmss(sec: float) -> str:
    return f"{int(sec // 3600)}:{int(sec % 3600 // 60):02d}:{int(sec % 60):02d}"


def main(judgments: Path, out: Path) -> None:
    by_id = {t["id"]: t for t in json.loads((ROOT / "glossary.json").read_text())}
    rows = [json.loads(l) for l in judgments.read_text().splitlines()]
    last_shown: dict[str, float] = {}
    shown, rejected, cooled = [], [], 0
    for r in rows:
        for c in r["candidates"]:
            tech = r["answers"][f"{c['id']}__tech"]["noul"]
            need = r["answers"][f"{c['id']}__need"]["score"]
            item = {"t": r["start"], "id": c["id"], "matched": c["matched"], "tech": tech, "need": need, "text": r["text"]}
            if tech < TECH_MIN or need < NEED_MIN:
                rejected.append(item)  # 弾いた場合はクールダウンを開始しない
            elif r["start"] - last_shown.get(c["id"], -1e9) < COOLDOWN_SEC:
                cooled += 1
            else:
                last_shown[c["id"]] = r["start"]
                shown.append({**item, "first": c["id"] not in {s["id"] for s in shown}})

    md = [f"# 技術用語ガイド再現タイムライン", "",
          f"しきい値: tech≥{TECH_MIN}, need≥{NEED_MIN}, クールダウン{COOLDOWN_SEC // 60}分",
          f"表示 {len(shown)}件 / クールダウンで抑制 {cooled}件 / Jevが却下 {len(rejected)}件", "",
          "## 表示されるもの", ""]
    for s in shown:
        tag = "初出" if s["first"] else "再掲"
        md += [f"### {mmss(s['t'])} {by_id[s['id']]['display']} ({tag}, tech={s['tech']:.2f}, need={s['need']:.2f})",
               f"> {by_id[s['id']]['short']}", "", f"発話: …{s['text']}…", ""]
    md += ["## Jevが却下したもの", ""]
    for s in rejected:
        md += [f"- {mmss(s['t'])} **{s['matched']}** tech={s['tech']:.2f} need={s['need']:.2f} — …{s['text']}…"]
    out.write_text("\n".join(md))
    print(f"shown={len(shown)} cooled={cooled} rejected={len(rejected)} -> {out}")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
