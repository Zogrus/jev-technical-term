"""技術用語ガイドの判定サーバー(状態を持たない)。

聞き手のブラウザ(index.html)から発話テキストを受け取り、Jevの判定結果だけを返す。
クールダウン・表示履歴・「もう知ってる」・表示レベルは聞き手ごとにブラウザ側で管理する。

    python3 app/server.py  →  http://localhost:8765
"""
import json
import re
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from glossary_loader import USER_GLOSSARY, Matcher, load_terms, normalize  # noqa: E402
from judge import call_jev, load_env  # noqa: E402

PORT = 8765
TECH_MIN = 0.5
UNKNOWN_MIN = 0.7
MAX_UNKNOWN = 8
DEFAULT_OTHER = "一般的な日常語としての意味、別分野の意味、または音声認識の誤り"
UNKNOWN_CATS = {
    "tech": "AI・プログラミング・IT分野の専門用語、技術の名前、または製品・サービス名",
    "common": "一般的な日常語・ビジネス用語(初心者でも知っている)",
    "proper": "人名・会社名・イベント名・キャラクター名",
    "noise": "音声認識の誤りで意味が分からない語",
}

lock = threading.Lock()
matcher: Matcher = None  # load_glossary() で設定


def load_glossary() -> None:
    global matcher
    matcher = Matcher(load_terms())


def add_user_term(title: str, body: str, level: int = 1) -> dict:
    title, body = title.strip(), body.strip()
    if not title or not body:
        raise ValueError("用語と解説の両方が必要です")
    with lock:
        user = json.loads(USER_GLOSSARY.read_text()) if USER_GLOSSARY.exists() else []
        user = [t for t in user if t["display"] != title]  # 同じ用語の再登録は上書き
        term = {"id": "user:" + title, "level": level, "display": title, "aliases": [title],
                "sense": body.split("。")[0][:80], "short": body}
        user.insert(0, term)
        USER_GLOSSARY.write_text(json.dumps(user, ensure_ascii=False, indent=1))
        load_glossary()
    return term


def needs_judgement(term: dict, alias: str) -> bool:
    """Jevに聞く必要がある候補か。別の意味を持つ語と、短くて部分一致の事故が起きやすい別名だけを聞く。
    長くて紛れようのない別名(「トークンを溶かす」「プロンプトエンジニアリング」等)は、そのまま採用する。"""
    if term.get("other"):
        return True
    return len(alias) <= 3 if alias.isascii() else len(alias) <= 5


TOKEN = re.compile(r"[ァ-ヴー]{4,}|(?<![A-Za-z])[A-Z][A-Za-z0-9]{1,}(?![a-z])")


def unknown_candidates(text: str, m: Matcher, spans: list) -> list[str]:
    """用語集にないカタカナ語・英略語の候補。

    以前は「用語集のどれかの別名と部分一致する語」を丸ごと除外していたが、用語集が大きくなると
    「ネットワーク」(←コンテンツデリバリーネットワーク)や「カレンダー」(←レンダー)まで除外されてしまう。
    その発話の中で、実際に用語集の語として一致した範囲と半分以上重なる語だけを除外する。"""
    out = []
    for mt in TOKEN.finditer(text):
        w = mt.group(0)
        if w in out or m.is_alias(w) or m.covered(mt.start(), mt.end(), spans) >= 0.5:
            continue
        out.append(w)
    return out[:MAX_UNKNOWN]


def judge(text: str, context: str, min_level: int = 1, detect_unknown: bool = True) -> dict:
    text, context = normalize(text), normalize(context)
    m = matcher  # 途中で用語集が再読み込みされても、この判定の中では同じものを使う
    cands, spans = m.find(text, context, min_level=min_level, with_spans=True)
    unknowns = unknown_candidates(text, m, spans) if detect_unknown else []
    if not cands and not unknowns:
        return {"terms": [], "latency": 0}

    questions = {}
    for i, c in enumerate(cands):
        term = m.by_id[c["id"]]
        if not needs_judgement(term, c["matched"]):
            continue
        # Jevは字面どおりに読むので、Yes/Noより「別の意味」を明示した二択のほうが判別が安定する
        questions[f"g_{i}"] = {
            "type": "choice",
            "instructions": f"これは音声認識による書き起こしである。「現在の発話」の中の「{c['matched']}」は、話し手がどちらの意味で言った言葉か。「現在の発話」の内容を優先して判断すること",
            "criteria": {"tech": term["sense"], "other": term.get("other") or DEFAULT_OTHER},
        }
    for i, u in enumerate(unknowns):
        questions[f"u_{i}"] = {
            "type": "choice",
            "instructions": f"「現在の発話」の中の「{u}」という語は、次のどれに当たるか",
            "criteria": UNKNOWN_CATS,
        }
    answers, latency = {}, 0
    if questions:
        res, latency = call_jev({
            "model": "jev-latest",
            "state": {"直前の文脈": context[-400:], "現在の発話": text},
            "questions": questions,
        })
        answers = res["answers"]

    terms = []
    for i, c in enumerate(cands):
        p = answers[f"g_{i}"]["probabilities"]["tech"] if f"g_{i}" in answers else 1.0
        if p >= TECH_MIN:
            term = m.by_id[c["id"]]
            terms.append({"key": c["id"], "kind": "glossary", "level": term["level"], "title": term["display"],
                          "body": term["short"], "matched": c["matched"], "p": p})
    for i, u in enumerate(unknowns):
        a = answers[f"u_{i}"]
        if a["choice"] == "tech" and a["probabilities"]["tech"] >= UNKNOWN_MIN:
            terms.append({"key": "u:" + u, "kind": "unknown", "level": 0, "title": u,
                          "body": "用語集にまだない専門用語のようです。", "matched": u, "p": a["probabilities"]["tech"]})
    return {"terms": terms, "latency": round(latency, 2)}


class Handler(BaseHTTPRequestHandler):
    def _send(self, body: bytes, ctype: str, status=200):
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.startswith("/stats"):
            levels = [t["level"] for t in matcher.by_id.values()]
            out = {"total": len(levels), "by_level": {str(l): levels.count(l) for l in (1, 2, 3)}}
            return self._send(json.dumps(out).encode(), "application/json")
        self._send((ROOT / "app/index.html").read_bytes(), "text/html; charset=utf-8")

    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        try:
            if self.path == "/judge":
                out = judge(data["text"], data.get("context", ""), int(data.get("min_level", 1)), bool(data.get("detect_unknown", True)))
            elif self.path == "/glossary/add":
                out = {"term": add_user_term(data["title"], data["body"], int(data.get("level", 1)))}
            else:
                return self._send(b'{"error":"not found"}', "application/json", 404)
            status = 200
        except Exception as e:  # 失敗しても聞き手側の認識ループを止めない
            out, status = {"error": str(e)}, 502
        self._send(json.dumps(out, ensure_ascii=False).encode(), "application/json; charset=utf-8", status)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    load_env()
    load_glossary()
    print(f"用語集: {len(matcher.by_id)}語")
    print(f"技術用語ガイド: http://localhost:{PORT}")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
