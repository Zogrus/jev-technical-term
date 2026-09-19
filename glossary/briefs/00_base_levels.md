作業ディレクトリは、このリポジトリのルートです。

最初に `glossary/SPEC.md` を読み、「レベルの基準」(1=初級 / 2=中級 / 3=上級)を理解してください。

## 依頼
既存の用語集 `glossary.json`(190語)の**各用語にレベルを付ける対応表**を作ってください。`glossary.json` 自体は編集しないでください。

- 出力先: `glossary/parts/00_base_levels.json`
- 形式: `{"用語のid": レベル, ...}` というJSONオブジェクト。`glossary.json` の全idを漏れなく含めること。例: `{"claude_code": 1, "llm": 1, "bff": 3, "otel": 3}`

判断の目安(読者は、AIにアプリを作らせ始めた非エンジニアを含む初心者):
- レベル1: 始めて1〜2ヶ月で必ず耳にする語(Claude Code, LLM, プロンプト, API, GitHub, デプロイ, トークン, ハルシネーション 等)
- レベル2: 自分でアプリを作って公開し始めると出会う語(RAG, MCP, フック, 環境変数, CI/CD, Docker, リファクタリング 等)
- レベル3: エンジニア実務の設計・運用や、AIの仕組みに踏み込んだ語(BFF, マイクロサービス, OpenTelemetry, MDM, 量子化, IaC 等)
- 迷ったら低いほうに倒す。

書き終えたら、次で全idの網羅を確認し、不足・余分があれば直してください。

python3 -c "
import json
from collections import Counter
g={t['id'] for t in json.load(open('glossary.json'))}
m=json.load(open('glossary/parts/00_base_levels.json'))
print('missing',g-set(m),'extra',set(m)-g,'bad',[k for k,v in m.items() if v not in (1,2,3)])
print(Counter(m.values()))
"

最終報告は、レベル別の語数と、判断に迷った語を数個だけ。
