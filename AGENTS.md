# AGENTS.md — AIコーディングエージェント向けの案内

このファイルは、Claude Code / Codex / Cursor などのAIエージェントが、このリポジトリを扱うときに最初に読むためのものです。
人間向けの説明は `README.md` にあります。

## このリポジトリは何か

「技術用語ガイド」: YouTubeの解説動画やZoomのセミナーなどを聞きながら技術(AI駆動開発など)を学ぼうとしている初心者向けに、
話の中に出てきたデジタル系の技術用語の**ひとこと解説**をリアルタイム表示するローカルWebアプリ。

- 文字起こし: Chrome内蔵の音声認識(Web Speech API)。視聴中のタブの音声を `getDisplayMedia` で取り、`SpeechRecognition.start(audioTrack)` に渡す
- 用語の照合: ローカルの技術用語集(約1,370語)と文字列照合(`scripts/glossary_loader.py`)
- 意味の判別: 紛らわしい語だけ TypeSafe AI の **Jev** に二択で聞く(`app/server.py` の `judge()`)。利用者がキーを用意して呼び出すAIは Jev だけ
- 画面: `app/index.html`(素のHTML/JS。クールダウン・「もう知ってる」・表示レベルはブラウザ側の localStorage)

## 構成

| パス | 役割 |
|---|---|
| `app/server.py` | 判定サーバー(Python 3 標準ライブラリのみ、状態なし)。`POST /judge`, `POST /glossary/add`, `GET /stats` |
| `app/index.html` | 画面。音声取得・文字起こし・カード表示 |
| `scripts/glossary_loader.py` | 用語集の読み込み(優先順: `glossary.user.json` → `glossary.json` → `glossary/parts/*.json`)と照合器 |
| `scripts/judge.py` | Jev API の呼び出し(`call_jev`)、`.env` の読み込み、検証用の窓分割 |
| `glossary.json` | 基本の用語集(レベルは `glossary/parts/00_base_levels.json`) |
| `glossary/parts/NN_*.json` | 分野別の用語集。**用語を追加・修正するのはここ** |
| `glossary/SPEC.md` | 用語集の書き方(レベル基準、解説の書き方、誤爆を防ぐ別名のルール)。**用語を書く前に必ず読む** |
| `glossary/validate.py` | 用語集の形式チェック |
| `glossary.user.json` | 利用者が画面から登録した用語(自動生成、gitignore) |
| `scripts/replay.py` ほか | 文字起こしを使ったオフライン検証(入力の `data/` はリポジトリに含まれない) |
| `docs/` | 検証ノート(技術者向け・初心者向け) |
| `start.command` / `start.bat` | ダブルクリック起動用 |

## 起動方法

```
cp .env.example .env    # JEV_API_KEY=... を書く
python3 app/server.py   # http://localhost:8765 (Windows: python app\server.py)
```

追加のライブラリは不要(pip install しない)。Python 3.10 以上を想定。

## 守ること

- **依存関係を増やさない。** サーバーは Python 標準ライブラリのみ、画面はフレームワークなしの素のHTML/JS。初心者がインストールなしで動かせることを最優先にしている
- **`.env` と `glossary.user.json` と `data/` はコミットしない**(`.gitignore` 済み)。APIキーをコードやドキュメントに書かない
- **Jev以外のAIサービスを判定や生成に組み込まない。** 「利用者が呼び出すAIはJevだけ」という前提で配布している。解説文の自動生成は意図的に外した(以前は Claude CLI で生成していたが削除)
- **用語を書くときは `glossary/SPEC.md` に従い、`python3 glossary/validate.py <ファイル>` を通す**
- 画面の文言は日本語。読者は非エンジニアを含む初心者
- サーバーは状態を持たない設計を保つ(将来ホスティングしても同じ動作にするため)

## よくある作業

- **用語を足す**: `glossary/parts/` の該当分野のJSONに1行追加(書式は SPEC.md)→ `python3 glossary/validate.py glossary/parts/<file>.json` → サーバー再起動
- **判定のしきい値を変える**: `app/server.py` の `TECH_MIN`(用語集の語、既定0.5)/ `UNKNOWN_MIN`(用語集にない語、既定0.7)
- **カードが出るタイミングを調整する**: `app/index.html` の `EARLY_CHARS`(既定50字)/ `EARLY_MS`(既定3000ms)
- **Jevに聞く対象を変える**: `app/server.py` の `needs_judgement()`(otherを持つ語と短い別名だけ聞く)
- **文字起こしで検証する**: `python3 scripts/replay.py data/raw/transcript.jsonl [--jev]`(`data/raw/transcript.jsonl` は `{"t": 秒, "text": ...}` のJSONL)

## Jevの使い方で分かっていること(要約)

詳しくは `docs/jev-learnings.md`。

- Yes/No(Noul)より、「技術的な意味 / 別の意味」を両方書いた Choice の二択のほうが確率がはっきり割れる
- 1つの質問に1つの判断。用語を「抜き出す」ことはできないので、候補はコードで作って選ばせる
- 紛れようのない長い別名やスラングはJevに聞かず、そのまま採用する
- 1回の呼び出しに質問を並列で載せても遅くならない(約2万トークンは通る。約12万は `max_tokens_exceeded`)
