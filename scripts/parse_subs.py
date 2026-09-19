"""YouTube json3 自動字幕を (開始秒, テキスト) の行に変換する。"""
import json
import sys
from pathlib import Path


def parse(path: Path) -> list[dict]:
    events = json.loads(path.read_text())["events"]
    lines = []
    for ev in events:
        text = "".join(seg.get("utf8", "") for seg in ev.get("segs", [])).strip()
        if not text:
            continue
        lines.append({"t": ev["tStartMs"] / 1000, "text": text})
    return lines


if __name__ == "__main__":
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    lines = parse(src)
    dst.write_text("\n".join(json.dumps(l, ensure_ascii=False) for l in lines))
    print(f"{len(lines)} lines, {lines[-1]['t'] / 60:.1f} min")
