"""用語集ファイルの検証。 python3 glossary/validate.py glossary/parts/xx.json [...]"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ["id", "level", "display", "aliases", "sense", "short"]


def check(path: Path, base_aliases: dict) -> list[str]:
    errs = []
    try:
        terms = json.loads(path.read_text())
    except Exception as e:
        return [f"JSONとして読めません: {e}"]
    ids = set()
    for n, t in enumerate(terms):
        where = f"[{n}] {t.get('display', '?')}"
        for k in REQUIRED:
            if not t.get(k):
                errs.append(f"{where}: {k} がありません")
        if errs and errs[-1].startswith(where):
            continue
        if not re.fullmatch(r"[a-z0-9_]+", t["id"]):
            errs.append(f"{where}: id は半角英小文字・数字・_ のみ ({t['id']})")
        if t["id"] in ids:
            errs.append(f"{where}: id が重複 ({t['id']})")
        ids.add(t["id"])
        if t["level"] not in (1, 2, 3):
            errs.append(f"{where}: level は 1/2/3")
        if len(t["short"]) > 100:
            errs.append(f"{where}: short が長すぎます ({len(t['short'])}字)")
        if len(t["sense"]) > 60:
            errs.append(f"{where}: sense が長すぎます ({len(t['sense'])}字)")
        if t["display"] not in t["aliases"] and not any(a.lower() == t["display"].lower() for a in t["aliases"]):
            # 「A / B」形式の見出しは別名に分けて入っていればよい
            if " / " not in t["display"] and "(" not in t["display"]:
                errs.append(f"{where}: display と同じ表記を aliases に入れてください")
        for a in t["aliases"]:
            if a.isascii():
                if len(a) < 2:
                    errs.append(f"{where}: 英字の別名は2文字以上 ({a})")
            elif len(a) < 3 and a not in ("冪等",):
                errs.append(f"{where}: 日本語の別名は3文字以上 ({a})")
            if a in base_aliases:
                errs.append(f"{where}: 別名「{a}」は既存の用語集(glossary.json)の「{base_aliases[a]}」と重複")
    return errs


if __name__ == "__main__":
    base = json.loads((ROOT / "glossary.json").read_text())
    base_aliases = {a: t["display"] for t in base for a in t["aliases"]}
    failed = False
    for arg in sys.argv[1:]:
        p = Path(arg)
        errs = check(p, base_aliases)
        n = len(json.loads(p.read_text())) if not errs or not errs[0].startswith("JSON") else 0
        print(f"{p}: {n}語, エラー{len(errs)}件")
        for e in errs[:40]:
            print("  -", e)
        failed |= bool(errs)
    sys.exit(1 if failed else 0)
