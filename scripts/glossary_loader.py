"""用語集の読み込みと、文字起こしからの用語候補の照合。

読み込み順(先に読んだものが優先。別名が衝突したら後から来たほうの別名を捨てる):
  1. glossary.user.json      … 聞き手が自分で登録した用語
  2. glossary.json           … 基本の用語集(レベルは glossary/parts/00_base_levels.json)
  3. glossary/parts/NN_*.json … 分野別の用語集
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
USER_GLOSSARY = ROOT / "glossary.user.json"
TAIL_CHARS = 12  # 発話の境界をまたいだ用語を拾うための、直前の文脈の末尾


def _read(path: Path):
    return json.loads(path.read_text()) if path.exists() else []


def _alias_key(alias: str) -> str:
    return alias.lower() if alias.isascii() and len(alias) >= 4 else alias


def load_terms(verbose: bool = False) -> list[dict]:
    base_levels = _read(ROOT / "glossary/parts/00_base_levels.json") or {}
    sources = [("user", _read(USER_GLOSSARY)), ("base", _read(ROOT / "glossary.json"))]
    for p in sorted((ROOT / "glossary/parts").glob("[0-9][0-9]_*.json")):
        if p.name != "00_base_levels.json":
            sources.append((p.stem, _read(p)))

    terms, seen_alias, seen_id, dropped = [], {}, set(), []
    for src, items in sources:
        for t in items:
            t = dict(t)
            t.setdefault("level", base_levels.get(t["id"], 1) if src == "base" else 1)
            if t["id"] in seen_id:
                dropped.append((src, t["display"], "idが重複"))
                continue
            keep = []
            for a in t["aliases"]:
                key = _alias_key(a)
                if key in seen_alias:
                    dropped.append((src, f"{t['display']} の別名「{a}」", f"「{seen_alias[key]}」と重複"))
                else:
                    keep.append(a)
            if not keep:
                continue
            for a in keep:
                seen_alias[_alias_key(a)] = t["display"]
            seen_id.add(t["id"])
            t["aliases"], t["source"] = keep, src
            terms.append(t)
    if verbose:
        for d in dropped:
            print("  dropped:", *d)
    return terms


_SPACE_NEAR_JA = re.compile(r"(?<=[^\x00-\x7F])[ \u3000]+|[ \u3000]+(?=[^\x00-\x7F])")


def normalize(text: str) -> str:
    """音声認識(Chrome)は単語の間に空白を入れる(「コード レビュー」「AI 駆動開発」)。
    日本語に隣接する空白だけを取り除く。英単語どうしの空白("Claude Code")は残す。"""
    return _SPACE_NEAR_JA.sub("", text)


def _pattern(alias: str) -> re.Pattern:
    if alias.isascii():
        # 英字は単語境界つき("PR" が "Pro" に当たらない)。短い略語は大文字小文字を区別する
        flags = re.IGNORECASE if len(alias) >= 4 else 0
        return re.compile(rf"(?<![A-Za-z0-9]){re.escape(alias)}(?![A-Za-z0-9])", flags)
    return re.compile(re.escape(alias))


class Matcher:
    """別名→用語の照合器。1,000語規模でも毎回の正規表現コンパイルを避けるため、読み込み時に一度だけ組み立てる。"""

    def __init__(self, terms: list[dict]):
        self.by_id = {t["id"]: t for t in terms}
        pairs = [(a, t["id"]) for t in terms for a in t["aliases"]]
        # 長い別名を先に当て、"サブエージェント" の中の "エージェント" を二重に拾わない
        pairs.sort(key=lambda p: -len(p[0]))
        self.pairs = [(a, tid, _pattern(a)) for a, tid in pairs]
        self.aliases = [a for a, _, _ in self.pairs]
        self._alias_set = {a.lower() for a in self.aliases}

    def find(self, text: str, context: str = "", min_level: int = 1, limit: int = 20, with_spans: bool = False):
        tail = normalize(context)[-TAIL_CHARS:]
        hay = tail + normalize(text)
        hay_lower = hay.lower()
        found, taken = [], []
        for alias, tid, pat in self.pairs:
            if alias.lower() not in hay_lower:
                continue  # 正規表現の前に安い部分一致で足切り(「AI駆動開発」のような英字まじりの別名も小文字で比べる)
            for m in pat.finditer(hay):
                if m.end() <= len(tail) or any(s < m.end() and m.start() < e for s, e in taken):
                    continue
                taken.append((m.start(), m.end()))
                term = self.by_id[tid]
                # レベル外の語も「場所取り」はさせる(より短い別名の誤一致を防ぐ)が、候補には入れない
                if term["level"] >= min_level and tid not in [f["id"] for f in found]:
                    found.append({"id": tid, "matched": alias})
        if with_spans:
            # 一致した範囲を、normalize(text) 上の位置で返す(レベル外の語の一致も含む)
            spans = [(max(s - len(tail), 0), e - len(tail)) for s, e in taken if e > len(tail)]
            return found[:limit], spans
        return found[:limit]

    def is_alias(self, word: str) -> bool:
        return word.lower() in self._alias_set

    def covered(self, start: int, end: int, spans: list) -> float:
        """語[start,end)のうち、用語集の語として一致した範囲が占める割合。"""
        n = sum(max(0, min(end, e) - max(start, s)) for s, e in spans)
        return n / max(end - start, 1)
