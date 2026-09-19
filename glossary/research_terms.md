# 調査結果: 用語集に入れるべき語

調査日: 2026-09-18。WebSearch / WebFetch により、note・Zenn・Qiita・はてなブログ・connpass・YouTube動画概要・企業オウンドメディア・Xの投稿を引用した記事などを横断的に調査した。`glossary.json`(既存92語)にある語と重複するものには `(※既存)` を付けた。Xの投稿そのものは直接検索・取得できないことが多く、各カテゴリの末尾に取得状況を記載している。

---

## 1. 初心者がつまずいている語

- エージェンティックループ(agentic loop) — 「情報収集→実行→検証→繰り返し」というAI自律実行サイクルの概念が初心者にはつかみにくい [Qiita](https://qiita.com/shou-dev19/items/e1583af614a573e4b245)
- ハーネスエンジニアリング — 「プロンプト→コンテキスト→ハーネス」という進化の文脈で突然登場し、業界内でも定義が定まっていない新語 [Qiita](https://qiita.com/shou-dev19/items/0f4ee962b89a322eefc0) / [ITmedia](https://atmarkit.itmedia.co.jp/ait/articles/2606/01/news016.html)
- ループエンジニアリング — 停止条件を満たすまで人間なしで走らせる運用設計、という抽象概念 [Qiita](https://qiita.com/shou-dev19/items/0f4ee962b89a322eefc0)
- 検証ループ — AI自身が合否を判定する仕組みという聞き慣れない語 [Qiita](https://qiita.com/shou-dev19/items/0f4ee962b89a322eefc0)
- オーケストレーター `(※既存: orchestration の別名)` — 複数AIエージェントに仕事を割り振る「指揮者・PM」役という比喩で語られる新語 [Qiita](https://qiita.com/shou-dev19/items/0f4ee962b89a322eefc0)
- 敵対的検証 — 別エージェントに基準に照らして批判・検証させるパターン、耳慣れない組み合わせ語 [Qiita](https://qiita.com/shou-dev19/items/0f4ee962b89a322eefc0)
- 動的ワークフロー — AIがタスク専用の実行手順をその場で組み立てるという抽象的な説明 [Qiita](https://qiita.com/shou-dev19/items/0f4ee962b89a322eefc0)
- Agent Teams — 独立セッション同士がチームを組む新機能、名前だけでは機能が想像できない [Qiita](https://qiita.com/shou-dev19/items/0f4ee962b89a322eefc0)
- 権限モード／許可モード `(※既存: permission の別名)` — どこまで自動承認するか5段階もあり、選び方がわからない [Qiita](https://qiita.com/shou-dev19/items/0f4ee962b89a322eefc0) / [Qiita](https://qiita.com/westtail/items/15767bbabf15a6db381d)
- YOLOモード(--dangerously-skip-permissions) — 俗語由来の名前の意味と危険性が伝わりにくい [Jicoo](https://www.jicoo.com/magazine/blog/claude-code-auto-mode-dangerously-skip-permissions)
- Auto Mode — YOLOモード・通常モードとの違いが名前だけでは判別できない [WORK WONDERS](https://workwonders.jp/media/archives/32822/)
- AGENTS.md — CLAUDE.mdとの違い・使い分けがわからないという声 [Zenn](https://zenn.dev/redamoon/articles/article27-agents)
- .env(環境変数ファイル) `(※既存: env_var の別名)` — 「秘密情報を保存する金庫」と例えられるが、ファイルの存在自体が謎 [GO! BLOG!!!](https://satsuki-bistro.com/claude-code-yogo-shu/)
- ハードコーディング — 「暗証番号をカードに油性ペンで書く」危険行為に例えられる専門用語 [GO! BLOG!!!](https://satsuki-bistro.com/claude-code-yogo-shu/)
- node_modules — npm installで生成される謎のフォルダ、消してよいかわからず混乱 [Qiita](https://qiita.com/mdrq/items/b815bd360d46d22ea6d8)
- package-lock.json — 何のためのファイルかわからない [Qiita](https://qiita.com/mdrq/items/b815bd360d46d22ea6d8)
- package.json — 役割がわからない [Qiita](https://qiita.com/ktr_web_dev/items/08cecf3142337918af8d)
- npm／npx／nvmの違い `(npm自体は既存語)` — 名前が似ていて何が違うのか定番の混乱ポイント [Qiita](https://qiita.com/ktr_web_dev/items/08cecf3142337918af8d) / [Qiita](https://qiita.com/shibuchaaaan/items/66020718b57bdcb801ed)
- PATH(パスを通す) — command not foundの原因として出てくるが意味不明 [Qiita](https://qiita.com/fe1ix/items/559d1175bd2c4735507a)
- sudo — 権限昇格コマンドの意味・危険性がわからない [note](https://note.com/xcamp/n/nb3a6df5511c3)
- Permission denied(権限エラー) — 何が「拒否」されているのか理解できず立ち往生 [Qiita](https://qiita.com/fe1ix/items/559d1175bd2c4735507a)
- command not found — インストール不足かPATHの問題か切り分けられない [Qiita](https://qiita.com/fe1ix/items/559d1175bd2c4735507a)
- SSH鍵(公開鍵・秘密鍵) — GitHub連携で急に出てくる暗号用語、どちらを公開してよいか不安になる [Qiita](https://qiita.com/suneo46/items/d5f1c31dc704fa2d4af6)
- Weekly limit／週間制限(Claudeの利用制限) — 5時間制限との二重構造がわからず「待ったのにまだ使えない」と混乱 [JAPAN AIラボ](https://japan-ai.co.jp/media/5937/)
- 5時間制限(ローリングセッション) — 週次制限との違いがわかりにくい [JAPAN AIラボ](https://japan-ai.co.jp/media/5937/)
- 使用量クレジット — 上限超過時の追加課金の仕組みがわかりにくい [GENAI](https://genai-ai.co.jp/ai-kanri/blog/cc-claude-limits-complete-guide/)
- Kiro — AWSのAI IDE、名前だけでは何のツールか判断できない [Zenn](https://zenn.dev/beagle/articles/1dea6ff60b1143)
- Spec Kit — GitHub提供の仕様駆動開発ツールキット、Kiroとの違いが不明瞭 [azukiazusa.dev](https://azukiazusa.dev/blog/spec-driven-development-with-spec-kit/)
- GitHub Spark — 存在を知らない人が多いAIアプリ開発ツール [note](https://note.com/shohei6117/n/ne8ccdfcd5eb2)
- Copilot Extensions — GitHub Copilotの拡張機能、名前だけでは何ができるかわからない [note](https://note.com/shohei6117/n/ne8ccdfcd5eb2)
- ローコード／ノーコード — 「プログラミング不要」という点でバイブコーディングとの違いがわからない [窓の杜](https://forest.watch.impress.co.jp/docs/serial/aidev/2078521.html)
- LLMOps — MLOpsとの違いがわからない新語 [窓の杜](https://forest.watch.impress.co.jp/docs/serial/aidev/2078521.html)
- Copilot型／Agent型(AI活用の型の違い) — 「人が主役」か「AIが主役」かの区別が初心者にはピンとこない [窓の杜](https://forest.watch.impress.co.jp/docs/serial/aidev/2078521.html)
- コンテキストが溢れる／コンテキスト消費 — コンテキストウィンドウが尽きるとどうなるかイメージできない [GO! BLOG!!!](https://satsuki-bistro.com/claude-code-yogo-shu/)
- 従量課金 — AIサービスの料金体系がわからず高額請求を心配する声 [Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q10316377105)
- プロジェクトメモリ／ユーザーメモリ(CLAUDE.mdのスコープ) — `.claude/CLAUDE.md`と`~/.claude/CLAUDE.md`の違いがわからない [Qiita](https://qiita.com/westtail/items/15767bbabf15a6db381d)
- MCPのスコープ(user/project/local) — 同じMCPでも設定範囲が3段階あり混乱する [Qiita](https://qiita.com/westtail/items/15767bbabf15a6db381d)
- VS Code `(※既存: IDE/エディタ の別名)` — 名前だけでは何のソフトかわからず、初心者が迷う代表用語として明記 [libecity](https://library.libecity.com/articles/01KQ7MECYX8ZVPXJNCQ4NPTNN1)
- データ構造 — 「アプリが保存する情報の種類と形式」という説明自体が非エンジニアには馴染みがない [はてなブログ](https://gen-ai-note.hatenablog.com/entry/vibe-coding-tips)
- バージョン管理(の考え方自体) — Gitという言葉を知らなくても「動いていたコードを保存しておく」という発想が新しい [はてなブログ](https://gen-ai-note.hatenablog.com/entry/vibe-coding-tips)
- pip install — npmとの違いがわからず、Python環境で何をしているか理解できない [note](https://note.com/nagisa2works/n/n40c61771d08d)
- ffmpeg — 名前の意味が不明で、何のためにインストールしているのかわからない音声・動画処理ソフト [note](https://note.com/nagisa2works/n/n40c61771d08d)
- ステータスライン(statusline) — Claude Code画面下の表示のカスタマイズ方法・設定ファイルの記法でつまずく [Qiita](https://qiita.com/ryu-ki/items/fa32472acb437bd2565a)
- DevContainer — Dockerとの関係や、なぜAI開発で推奨されるのかが初心者にはわかりにくい [Qiita](https://qiita.com/0xv80/items/3288da52e6a2652c3718)
- 壁打ち(AIとの) — テニス由来の比喩表現で、初心者には「何をすればいいのか」がわからない生成AI活用法 [note](https://note.com/reikirishima/n/n24428e788f5c)
- checkpoint／rewind機能 — `/rewind`でどこまで戻せてどこから戻せないのか(コマンド実行の副作用は戻らない等)が把握しづらい [Qiita](https://qiita.com/yureki_lab/items/35251957a3b769c6d4b4)
- ultrathink(拡張思考の呪文コマンド) — 「ultrathink」と打つと思考が深くなるという通称の意味がわからない [Zenn](https://zenn.dev/tmasuyama1114/books/claude_code_basic/viewer/ultrathink-mode)
- シンキングバジェット(拡張思考の予算) — 「予算」という金銭的な語感とトークン消費の関係が直感的にわからない [Claude Docs](https://platform.claude.com/docs/ja/build-with-claude/extended-thinking)
- stdio／SSE／HTTP(MCPの接続方式) `(HTTPは既存: rest_http の別名)` — 略語だらけで、どれを選べばいいのか初心者には判断できない [Zenn](https://zenn.dev/nanananano/articles/df5802334d999e)
- オートモード分岐の三択(Auto/YOLO/通常) — 三つのモードの安全性の違いが直感的にわからず、誤って危険な方を選んでしまう不安 [WORK WONDERS](https://workwonders.jp/media/archives/32822/)
- モジュール機能(CLAUDE.mdのインポート分割) — 「大規模プロジェクトで指示を複数ファイルに整理」する仕組みだが、どのレベルで分割すべきか判断基準が不明 [Qiita](https://qiita.com/westtail/items/15767bbabf15a6db381d)
- 設定ファイルの乱立(AGENTS.md/SKILL.md/DESIGN.md) — CLAUDE.mdと役割が似た複数の指示書ファイルが並立し、どれをいつ使うべきか判断できない [Zenn](https://zenn.dev/genda_jp/articles/f71d3ed7d4d7e8)
- context: fork(コンテキストの分岐実行) — 「独立したコンテキストで実行」という概念がイメージしにくい [Qiita](https://qiita.com/westtail/items/15767bbabf15a6db381d)
- /scheduleコマンド — Claude Codeのスラッシュコマンド一覧の中で用途が直感的にわからないものの一つ [GO! BLOG!!!](https://satsuki-bistro.com/claude-code-yogo-shu/)
- /voiceコマンド — 「コードをしゃべって書く」音声入力機能で、日本語認識の追加設定が必要なことに気づきにくい [Zenn](https://zenn.dev/aki1990/articles/6e3008c2a1c180)
- Claude Code Router — Claude CodeのAPIリクエストを別モデルに転送する仕組み、ローカルOllama連携を試みて失敗した体験談がある [taneyats.com](https://www.taneyats.com/entry/claude-code-router)
- Traceback — Pythonのエラーメッセージ形式。実行経路の読み方がわからず心が折れるポイント [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- ModuleNotFoundError — インポートエラーで、初心者は原因(環境の違い)がわからず詰まる [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- 仮想環境(Virtual Environment) — プロジェクトごとに隔離されたPython環境という概念自体がなぜ必要かわからない [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- 依存関係地獄(Dependency Hell) — ライブラリ同士が競合し解決困難になる状態で、AIに指示しても解決しにくい [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- セレクタ — BeautifulSoupやSeleniumでHTML要素を指定する仕組み、スクレイピング系コード生成でよく登場し混乱 [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- CAPTCHA — 「ロボット確認」パズルがAI駆動のスクレイピング処理を止める要因になることを知らずに詰まる [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- uv(Pythonパッケージマネージャ) — pipより高速な次世代ツールとして紹介されるが、pipとの違い・使い分けがわからない [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- CORSエラー — 「異なるオリジンからのリクエスト」制御という概念が抽象的で、原因不明のエラーに混乱する [note](https://note.com/munchieblog/n/n2a687479470b)
- 二重ヘッダー(CORSの重複ヘッダー問題) — CORSを設定できる箇所が2つあり、AIが両方に設定して衝突する現象がわからない [note](https://note.com/munchieblog/n/n2a687479470b)
- レースコンディション — 複数処理が同じデータに予想外のタイミングでアクセスして起きるバグ、直感的に理解できない [Qiita](https://qiita.com/Yuya_baseball/items/807ab2aa0c9a821f7d69)
- オーケストレーションパターン(Classify-and-act／Fan-out-and-synthesize／Tournament) — 複数エージェントの連携方式が4種類も並立し区別が難しい [Qiita](https://qiita.com/shou-dev19/items/0f4ee962b89a322eefc0)
- Material Ambiguity(実在する曖昧性) — 実装方向や検証方法など結果を大きく変える不確実さを指す独自定義語 [Zenn](https://zenn.dev/explaza/articles/d0aeb08fcd1888)
- 型エラー(TypeError) `(※既存: type_system の別名)` — 「同じ場所で同じエラーが繰り返し発生する」ことが多く、原因(型の不一致)がわからず詰まる [techblog.ap-com.co.jp](https://techblog.ap-com.co.jp/entry/2026/03/27/144621)
- 非同期処理(同期/非同期の違い) — AIが書いた非同期コードが実機で遅い理由がわからず「なぜ」を説明できないまま使ってしまう [Think IT](https://thinkit.co.jp/article/39515)
- .gitignore — Git管理対象外の設定ファイルという役割が、非エンジニアには存在意義から不明 [GO! BLOG!!!](https://satsuki-bistro.com/claude-code-yogo-shu/)
- Hooksのタイミング(PreToolUse/PostToolUse等) — 「ツール実行時に自動実行されるシェルコマンド」だが5種類のタイミングの区別がつかない [Qiita](https://qiita.com/westtail/items/15767bbabf15a6db381d)
- ベクトルDB(ベクトルデータベース) `(※既存: embedding の別名)` — AI駆動開発文脈のエンジニア職能解説で登場するが、通常のDBとの違いが不明 [malanka.org](https://www.malanka.org/entry/forward-deployed-engineer-fde)
- JWT/OAuth/SAML(認証プロトコルの違い) `(OAuthは既存: auth の別名)` — 「認証/認可」はわかってもプロトコル名の違いが区別できない [malanka.org](https://www.malanka.org/entry/forward-deployed-engineer-fde)
- SRE(Site Reliability Engineer) — AI駆動開発時代の新職種紹介で頻出する略語だが、開発エンジニアとの違いが直感的にわからない [malanka.org](https://www.malanka.org/entry/forward-deployed-engineer-fde)

補足: X(旧Twitter)の投稿本文は認証制限のため直接取得できなかった。ただし「Xで〜という声」の形で投稿内容を引用・要約している記事は複数取得できた。

---

## 2. 発信者がよく使う語・新語

- AIスロップ(AI Slop) — 読者価値を無視しAIで大量生産された低品質コンテンツを指す蔑称 [e-words](https://e-words.jp/w/AI%E3%82%B9%E3%83%AD%E3%83%83%E3%83%97.html)
- ハーネスエンジニアリング — LLM以外の周辺環境(ツール・検証ロジック・観測レイヤー等)を設計する技術。プロンプト→コンテキスト→ハーネスの順で進化 [Findy](https://jp.findy-team.io/blog/ai-casestudy/harness-engineering/)
- 壁打ち(AI壁打ち) — AIを思考整理のための対話相手・サウンディングボードとして使うこと [note](https://note.com/realworld/n/nc69b952334e7)
- 丸投げ(AI丸投げ) — 詳細な設計をせず漠然とした指示でAIに実装を任せること。技術的負債とセットで語られる [note](https://note.com/danimal141/n/n86816b343988)
- 理解負債 — 丸投げによりコードの中身を人間が理解しないまま積み上がっていく負債 [blog.myntinc.com](https://blog.myntinc.com/2026/06/ai_0817465567.html)
- 自走(自走型AIエージェント) — 人が張り付かなくても目標達成までタスクを自律的にこなし続けるエージェント [note](https://note.com/ikuo00uk/n/n65b8a1ec2ed4)
- Ralph loop(ラルフループ) — 同じ指示文を繰り返しAIに渡し、実装→テスト→コミットを自律的に繰り返させる開発手法 [Zenn](https://zenn.dev/syuya2036/articles/ralph-agent-loop)
- ループエンジニアリング(Loop Engineering) — プロンプトエンジニアリングの次段階として、AIを自律的に回す「ループ」自体を設計する営み [Zenn](https://zenn.dev/spectee/articles/loop-engineering-ai-dev-cycle)
- エージェンティックコーディング — LLMベースのAIエージェントが目標に対し自ら計画・実行・修正を繰り返す開発手法 [ISSOH](https://www.issoh.co.jp/tech/details/6797/)
- エージェンティックエンジニアリング — バイブコーディングの限界を超え、人間が設計・評価を担い複数のAIエージェントを統制する開発スタイル [ITmedia](https://atmarkit.itmedia.co.jp/ait/articles/2602/19/news018.html)
- コンテキスト腐敗(Context Rot) — コンテキストが増えるほどモデルの注意が分散し精度が落ちる現象 [note](https://note.com/seeso/n/n6912707d42c5)
- コンテキスト汚染 — 古い試行錯誤やハルシネーションが会話履歴に混入し、どの情報が有効か判断できなくなる状態 [note](https://note.com/tqy/n/nbada3d1087ed)
- 記憶が飛ぶ／Claude Codeがアホになる — コンテキストウィンドウが約80%超で自動発動する「オートコンパクティング」で詳細な文脈が失われる現象の俗な言い方 [Zenn](https://zenn.dev/shintaroamaike/articles/1a6d4bb199d666)
- コンテキストがパンパン — コンテキストウィンドウがほぼ埋まっている状態を指すカジュアルな表現 [Qiita](https://qiita.com/yama3133/items/09b5288b4a661bc9a20a)
- コンテキストエンジニア — AIに適切な文脈情報を設計・提供する専門家というAI時代の新職種呼称 [note](https://note.com/nagoya_blog/n/n0e3ca1abdb20)
- ワンショット(プロンプト) `(※既存: few_shot の別名)` — 一度の指示・1回の生成で意図通りの成果物を得ること [note](https://note.com/yoshiyuki_hongoh/n/n364d3fbf2e77)
- 秘伝のタレ — 自分の価値観・文体・ノウハウを言語化したMDファイル等をAIに読み込ませ、指示を最小限にして狙った出力を得る個人ナレッジ [note](https://note.com/okodukai_prompt/n/n4535b9b17399)
- AI疲れ — 生成AIを使い続けることで生じる独特の疲労感。「作業者」から「監督・評価者」への役割変化による認知負荷 [Zenn](https://zenn.dev/karamage/articles/306f0c571e0af9)
- AIツール沼 — 次々に登場する新AIツールを試し続けて時間とコストを消耗する状態 [note](https://note.com/ai_trendnavi/n/necfc95b1c6e6)
- Claude Code沼 — Claude Codeにのめり込んでいく様子を指すカジュアルな表現 [note](https://note.com/daiki_acc_it/n/n7c4125b0f81c)
- 写経(AI写経) — AIが生成したコードをそのまま書き写し、体に落とし込んで学ぶ学習法 [Zenn](https://zenn.dev/unr_tech_lab/articles/d7934ef6e0b78e)
- トークンを食う — Claude Code等が想定以上にトークン(コスト)を消費すること [Zenn](https://zenn.dev/ruralwritter/articles/b5e90a4883308e)
- トークンを溶かす — `/model`切替や`--resume`等でプロンプトキャッシュが無効化され、コストが跳ね上がること [kaitoy.xyz](https://www.kaitoy.xyz/2026/06/21/claude-code-prompt-caching/)
- ガチャ(AIガチャ／プロンプトガチャ) — 同じ指示でも毎回違う出力が返る様子を、ゲームのガチャに例えた表現 [日本経済新聞](https://www.nikkei.com/article/DGXZQOUC253L40V21C25A1000000/)
- AIネイティブ(開発) — AIを後付けでなく最初から前提として設計・運営される開発スタイル [Zenn](https://zenn.dev/umi_mori/books/ai-native-programming/viewer/what_is_ai_native_programming)
- 脳死コーディング — 内容を深く考えずAIの出力をそのまま受け入れて作業する状態 [zawatto.com](https://zawatto.com/meme/noushi/)
- ultrathink(ウルトラシンク) — Claude Codeで最大思考予算を引き出す魔法の言葉。他に"think harder"等の思考レベル指定語がある [ClaudeLog](https://claudelog.com/faqs/what-is-ultrathink/)
- 神プロンプト — AIから最高品質の回答を引き出す指示文・テンプレートを指す称賛的な呼び方 [note](https://note.com/murayama_taro/n/n38b1f32d2a02)
- 指示出し力 — テンプレ化したプロンプトより、状況・目的をAIに伝える汎用的な力こそ一生モノとする議論で使われる語 [note](https://note.com/yusuke_motoyama/n/n40a63005fc19)
- プロンプト職人 — AIに指示を出しその力を最大限引き出す人を指すカジュアルな呼び方 [note](https://note.com/kakujuku/n/n66a7bf8e3311)
- プロンプトエンジニア不要論／オワコン論 — AIの進化により「呪文探し」としてのプロンプト技術は不要になったとする議論 [note](https://note.com/hiro____note/n/n8bd8a5ce1e89)
- AGENTS.md — AIコーディングエージェント向けにビルド手順・コーディング規約等を伝える「プロジェクトの取扱説明書」的な設定ファイルの業界標準 [techfun.co.jp](https://www.techfun.co.jp/services/magazine/generative-ai/agents-md-basics-and-practice.html)
- Spec Kit — GitHubが公開した仕様駆動開発を支援するオープンソースツールキット [ServerWorks Blog](https://blog.serverworks.co.jp/github-spec-kit-guide)
- PRP(Product Requirement Prompt) — PRD＋コードベース情報＋エージェント向け実行指示をまとめ、AIが一発で実装できるようにするプロンプト設計手法 [asdlc.io](https://asdlc.io/concepts/product-requirement-prompt/)
- Agent Employee(AIエージェント従業員) — AIエージェントを同僚として業務に組み込むという2026年提唱のコンセプト [Zenn](https://zenn.dev/ase_dataeng/articles/ai-data-platform-glossary)
- 人間がボトルネック — AIの処理速度に対し、人間の意思決定・タイピング速度が開発の制約になっている状態を指す言い回し [Zenn](https://zenn.dev/acntechjp/articles/36a93b7a4d14c3)
- 爆速開発 — AI駆動でこれまでより大幅に速い開発速度を実現することを指す常套句 [note](https://note.com/cor_instrument/n/n800a959f7284)
- AI伴走／伴走支援 — 外部専門家やAIがチームの一員のように並走し、内製化・自走化を支援すること [digital-front.jp](https://digital-front.jp/blog/1229/)
- AIファースト — AIエージェントが最大限自律的に業務を担う前提で事業・プロダクトを設計し直す経営モデル [三菱総研](https://dx.mri.co.jp/column/column-1203/)
- 一人ユニコーン — AIエージェントの活用により個人だけで評価額10億ドル規模の企業を築くという2026年のバズ概念 [note](https://note.com/startup_now0708/n/n3444c33cfc57)
- バイブマーケティング(Vibe Marketing) — AIツールを駆使し少人数チームで大量に高品質コンテンツを生成し、統一した「雰囲気」を発信するマーケティング手法 [note](https://note.com/ai__worker/n/ncda4af1f3ded)
- バイブチェック(Vibe Check) — AI生成コードを出す前に人間が目視で妥当性を確認する工程(英語圏発で日本語定着はやや限定的) [Palo Alto Networks](https://www.paloaltonetworks.com/blog/identity-security/vibe-check-your-vibe-code-adding-human-judgment-to-ai-driven-development/)
- マルチエージェント地獄／オーケストレーション疲れ — フレームワーク乱立とエージェント間調整の複雑さに開発者が疲弊する状況を表す俗語 [Zenn](https://zenn.dev/babushkai/articles/2026-01-20-multi-agent-orchestration-patterns)
- サブスク破産 — Claude Codeのサブスクプラン費用感が想定より重くなる懸念を指す非公式な言い回し [Zenn](https://zenn.dev/sanpi34/articles/claude-code-pricing-shift-2026)
- 従量課金沼 — API従量課金の使い方次第でコストが想定以上に膨らむ状態を指すカジュアルな表現 [Qiita](https://qiita.com/sakamoto66/items/abe1f1106104a9bd1b34)
- 承認ゲート — 仕様駆動開発(SDD)の各フェーズに人間の確認を挟み、自動化と統制を両立させる仕組み [itcompass.lanitech.jp](https://itcompass.lanitech.jp/blog/ai-driven-development-glossary/)
- ステアリングドキュメント — AIエージェントに常時与える前提・規約・技術選定等を書いた文脈ファイル群 [itcompass.lanitech.jp](https://itcompass.lanitech.jp/blog/ai-driven-development-glossary/)
- ゲームエンド — 従来手法を覆す新技術登場時にAI推進派が使う高揚を表すフレーズ(画像生成AI界隈発祥) [w.atwiki.jp](https://w.atwiki.jp/genai_problem/pages/12.html)
- AIウォッシング(AI washing) — 企業が自社製品のAI活用度を誇張・欺瞞的に表現するマーケティング行為 [日経クロストレンド](https://xtrend.nikkei.com/atcl/contents/18/00079/00315/)
- クランカー(Clanker) — ロボット/AIを指す侮蔑的スラング。直近数ヶ月で使用が急増していると報告 [日経クロストレンド](https://xtrend.nikkei.com/atcl/contents/18/00079/00315/)
- FDE(フォワード・デプロイド・エンジニア) — 顧客現場に入り込んでAI・ソフトウェアを実装する新職能 [malanka.org](https://www.malanka.org/entry/forward-deployed-engineer-fde)
- AI-Augmented Engineer(AI拡張型エンジニア) — GitHub CopilotやClaude Codeを使い倒して「高速開発」するエンジニアを指す新呼称 [note](https://note.com/hacomono_obata/n/n9705c383839b)
- Vibe Coder(バイブコーダー) — 意図や感覚をAIに伝えて生成コードを組み合わせるスタイルの開発者を指す呼称 [note](https://note.com/hacomono_obata/n/n9705c383839b)
- AI Native Leader — AIを前提に組織・プロダクトを設計する次世代型リーダーを指す新呼称 [note](https://note.com/hacomono_obata/n/n9705c383839b)
- CAIO(Chief AI Officer) — 全社的AI戦略を統括する新設役員職の呼称 [note](https://note.com/hacomono_obata/n/n9705c383839b)
- AI Transformation Leader — 既存業務・プロセスにAIを導入し組織変革を推進する管理職の呼称 [note](https://note.com/hacomono_obata/n/n9705c383839b)
- AI PdM(AIプロダクトマネージャー) — AI特性を理解した上でプロダクト戦略を立案するPM職の呼称 [note](https://note.com/hacomono_obata/n/n9705c383839b)
- 意図駆動型開発 — Vibe Codingに続く2026年のバズワードとして、「目的(意図)」を軸に開発するAgentic AI時代のアプローチ [note](https://note.com/ai__worker/n/na7b51bc39a53)
- Agentic AI(自律型AI) — 「目的を伝えれば自律的にタスクを完遂するAI」として2026年の開発現場のキーワード [ARSAGA](https://www.arsaga.jp/blog/frontline-ai-driven-development/)
- お祈り駆動開発(PDD) — テストコードの代わりに「信仰」で品質を保証するという風刺的スラング。「信仰ベーステスト」等の派生語も [Zenn](https://zenn.dev/hiyotsuku/articles/5d5cb56ba5bb15)
- リセマラ — 納得いくまでAIに何度もコードを生成し直させる行為を、ゲームの「リセットマラソン」になぞらえた造語 [Zenn](https://zenn.dev/aun_phonogram/articles/8132677fc3bb69)
- 老害おじさん図鑑 — 2026年5月頃からXで大バズりした、生成AIがITエンジニア/SIerおじさんの「あるある」を再現したミーム表現 [DIAMOND ONLINE](https://www.diamondv.jp/article/bB3YwSAzjw7bUUw3Qa8JT3)
- 4点セット — AIにエラー解決を依頼する際に必要な情報(①エラーログ全文②コード③目標④環境情報)をまとめた実務スラング [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- 環境汚染 — グローバルPython環境に継ぎ足しでライブラリをインストールし続け、何が入っているかわからなくなった状態の比喩 [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- 秘伝のタレ化した環境 — 中身が誰にもわからなくなった開発環境を「秘伝のタレ」になぞらえた表現 [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- サンクコストの呪縛 — 苦労してセットアップしたから使い続けてしまう心理を指すスラング [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- エラー地獄 — 複数のエラーが絡み合い解決不可能に見える状態を指す実務スラング [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- モグラ叩き — 1つ直すと別の場所でエラーが出る無限ループ状態を指す表現 [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- 2ストライク・ルール — Auto Fixを2回試して直らないなら設計ミスと判断してアプローチを変えるという実務ルールの俗称 [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- ラバーダック・デバッグ — AIに状況を説明することで思考が整理される手法を指す比喩表現 [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- エラーログ駆動開発 — エラーログを入力情報として戦略的にAIに活用させる開発手法の俗称 [prompter-note.com](https://prompter-note.com/ai-programming-error-log-driven-development/)
- 一気通貫 — 要件から実装まで同一担当者・同一AIエージェントが責任を持つ体制を指す表現 [Zenn](https://zenn.dev/explaza/articles/d0aeb08fcd1888)
- P0〜P3優先度分類 — AIによる自動コードレビューの指摘事項を重要度別に分類する際に使われる実務用語 [Zenn](https://zenn.dev/explaza/articles/d0aeb08fcd1888)
- AI業務設計者 — 「プロンプト職人」に代わる新しい呼称として、業務設計スキルを持つ人材を指す表現がXで話題に [note](https://note.com/alive_crane5316/n/n08eb9a383345)
- AI社員 — チャットで答えるだけでなくSlack常駐で実務をこなす「デジタル従業員」を指す2026年のトレンド呼称 [DeNA Engineering](https://engineering.dena.com/blog/2026/08/ai-employee-introduction/)
- 運ゲー化 — AIコーディングの成否が運に左右される状態を指す表現、「静かに進行する恐怖」として発信者が警鐘を鳴らす文脈で使われる [Zenn](https://zenn.dev/aun_phonogram/articles/8132677fc3bb69)

補足: X本文はWebSearch/WebFetchでは直接取得できなかったが、Xの投稿・トレンドを引用・要約しているnote/Zenn記事(老害おじさん図鑑のバズ、プロンプト職人論争など)は複数取得できた。

---

## 3. 勉強会で頻出の語

- Claude Agent SDK — 「Claude CodeでClaude Agent SDKを使ってエージェントを自作しよう」LTで、Claude Codeの土台となるSDKとして紹介 [connpass](https://aid.connpass.com/event/386203/)
- Claude Cowork — 「全社員のClaude Code・Coworkの利用状況をOpenTelemetryとGrafanaで可視化した話」で言及 [connpass](https://aid.connpass.com/event/386203/)
- SoC(関心の分離) — 「煩雑なSkills管理をSoCにより解決する」というLTタイトルの設計原則 [connpass](https://aid.connpass.com/event/386203/)
- A2A(Agent to Agent) — 「A2AとMCPで作るエージェント」LT [Zenn](https://zenn.dev/almondo/articles/246007a6c6de81)
- Anthropic Sandbox Runtime(srt) — 「Claude CodeのSandbox機能をAnthropic Sandbox Runtime(srt)で試そう」LT [connpass](https://aid.connpass.com/event/394427/)
- Tasks機能(Plan+Tasks) — 「大規模実装をClaude Codeに任せるには？ Plan + Tasksで精度を上げる4つのコツ」LT [connpass](https://findy.connpass.com/event/383312/)
- rules整備 — 「Claude Codeを育てる開発スタイル ─ 情報収集からrules整備まで」LT [connpass](https://findy.connpass.com/event/383312/)
- Google ADK(Agent Development Kit) — 「Google ADKを活用したAI Agent開発と運用知見」セッション [connpass](https://cyberagent.connpass.com/event/371245/)
- CodingAgent — 「CodingAgentを用いた新規プロダクト爆速立ち上げと運用について」セッション [connpass](https://cyberagent.connpass.com/event/371245/)
- Langfuse — 「LangfuseでAIエージェントの可観測性を高めよう！」LT [connpass](https://mlops.connpass.com/event/347046/)
- Ai Workforce — 「Ai WorkforceでのAI Agentの作り方」(LayerX社プラットフォーム)LT [connpass](https://mlops.connpass.com/event/347046/)
- Gemini Code Assist — AI Agent勉強会Vol.5で言及されたAIコーディング支援ツール [Zenn](https://zenn.dev/almondo/articles/0fd942ade1ee67)
- Greptile — 同上、コードレビューAIツールとして紹介 [Zenn](https://zenn.dev/almondo/articles/0fd942ade1ee67)
- CodeRabbit — AI Agent勉強会Vol.5、AI駆動開発カンファレンス双方で言及されたAIコードレビューツール [Zenn](https://zenn.dev/almondo/articles/0fd942ade1ee67)
- shadcn/ui — AI Agent勉強会Vol.5でUI自動生成の文脈で紹介 [Zenn](https://zenn.dev/almondo/articles/0fd942ade1ee67)
- Storybook — 同上、UIコンポーネント管理ツールとして言及 [Zenn](https://zenn.dev/almondo/articles/0fd942ade1ee67)
- Google Colab — AIエージェント開発ハンズオンやAI Agent勉強会vol.8で使用環境として言及 [Zenn](https://zenn.dev/almondo/articles/d5a83063fc71c2)
- 物体検出 — 「LLMの可能性を拡張する！物体検出×AIエージェントによる図面認識・解釈」LT [Zenn](https://zenn.dev/almondo/articles/d5a83063fc71c2)
- Zoltraak — 「大規模システム生成AI『Zoltraak』『Babel』から『神威』への進化と今後の展望」LT(自然言語プログラミングツール) [Zenn](https://zenn.dev/manase/scraps/31aec39fa638c2)
- 神威(KAMUI) — 同上、Zoltraakの後継ツールとして紹介 [Zenn](https://zenn.dev/manase/scraps/31aec39fa638c2)
- GEAR.indigo — 「要件定義から実装まで…GEAR.indigoの徹底紹介」LT(ドキュメント生成型開発ツール) [Zenn](https://zenn.dev/manase/scraps/31aec39fa638c2)
- 要件定義プログラミング — AI駆動開発勉強会メモに登場する開発手法用語 [Zenn](https://zenn.dev/manase/scraps/31aec39fa638c2)
- 自然言語プログラミング — 同上、ZoltraakやGEAR.indigoの文脈で頻出 [Zenn](https://zenn.dev/manase/scraps/31aec39fa638c2)
- メタプロンプト — 同上、対話型プロンプト・要件定義プロンプトと並んで登場 [Zenn](https://zenn.dev/manase/scraps/31aec39fa638c2)
- Jules — AI駆動開発勉強会の振り返り記事でAIコーディングツールとして言及 [Zenn](https://zenn.dev/acntechjp/articles/ca581cfda42b45)
- Kiro — 同上(AWSのAI駆動IDE) [Zenn](https://zenn.dev/acntechjp/articles/ca581cfda42b45)
- Podman — 同上、開発環境ツールとして言及 [Zenn](https://zenn.dev/acntechjp/articles/ca581cfda42b45)
- WSL — 同上 [Zenn](https://zenn.dev/acntechjp/articles/ca581cfda42b45)
- SPA(Single Page Application) — 同上、AI駆動開発のアーキテクチャ文脈 [Zenn](https://zenn.dev/acntechjp/articles/ca581cfda42b45)
- GitHub Copilot Agent Mode — AI駆動開発カンファレンス2026夏「2億人の開発者と、エージェントの時代」セッション [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- Copilot Code Review(CCR) — 同上 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- GitHub Code Quality — 同上 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- Agentic Workflow — 同上、複数セッションで頻出のキーワード群 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- SIEM連携 — 同上、エンタープライズガバナンスの文脈 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- AI-DLC(AI-Driven Development Life Cycle) — 同上 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- Package Firewall — 同上、サプライチェーンセキュリティ機能 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- Secret Scanning — 同上(GitHub Advanced Securityの機能) [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- Code Scanning — 同上 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- GHAS(GitHub Advanced Security) — 同上 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- Dependabot — 同上 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- Copilot Autofix — 同上 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- DORA Metrics — 同上、AI時代の開発生産性指標として紹介 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- Defense in Depth — 「Defense in Depth: How Replit Secures Every Layer of AI-Generated Software」セッション [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- Claude Design — 「Claude Codeで思ったUIを出力してくれないあなたへ ─ Claude Designで解決できるかも」LT [connpass](https://aid.connpass.com/event/402949/)
- Claude Code Portal — 「魔法少女がClaude Codeを監視する！Claude Code Portalというアプリを開発しました」LT [connpass](https://aid.connpass.com/event/402949/)
- グラフエンジニアリング — 「グラフエンジニアリング、効く問いと効かない問い。実測で切り分けた」LT [connpass](https://aid.connpass.com/event/402949/)
- Kanary — 「Kanary / Gista.js開発者からみたClaude Fable 5の実力とは？」セッション [connpass](https://aid.connpass.com/event/394427/)
- Gista.js — 同上 [connpass](https://aid.connpass.com/event/394427/)
- Claude Fable 5 — 同上、登壇者が言及したClaudeモデルの通称 [connpass](https://aid.connpass.com/event/394427/)
- スマートグラス — 「スマートグラスで並列バイブコーディング」LT [connpass](https://aid.connpass.com/event/394427/)
- ウォーターフォール開発 — 「チームで進めるAI駆動アジャイル×ウォーターフォール」LT [Zenn](https://zenn.dev/almondo/articles/d5a83063fc71c2)
- ASI(Artificial Specific Intelligence) — AI駆動開発勉強会メモの用語一覧に登場 [Zenn](https://zenn.dev/manase/scraps/31aec39fa638c2)
- AI音楽生成 — 「AI音楽生成からYouTube投稿まで——n8nで構築した自動運営ワークフロー」LT [connpass](https://aiagentsoftware.connpass.com/event/369714/)
- Gemini 2.5 Computer Use Model — 「AIエージェントがLTやってみた」LTで使用されたモデル [connpass](https://aiagentsoftware.connpass.com/event/369714/)
- ログ基盤 — 「ログ基盤・プラグイン・ダッシュボード、全部整えた。でも最後は人だった。」LT [connpass](https://aid.connpass.com/event/386203/)
- ダッシュボード — 同上 [connpass](https://aid.connpass.com/event/386203/)
- GStreamer — AI駆動開発勉強会第1回、映像配信×AIのセッションで言及 [connpass](https://aid.connpass.com/event/306406/)
- Jetson — 同上、エッジデバイスとして言及 [connpass](https://aid.connpass.com/event/306406/)
- Multi Agents Orchestration — AI駆動開発カンファレンス2026夏のセッションキーワード [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- Role-Based Agent Design — 同上 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- SSO/SCIM/RBAC `(SSOは既存: auth の別名)` — 同上、エンタープライズ権限管理の文脈 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- Review Hub — 同上 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- Agentic Security Remediation — 同上 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- ガーディアンレイヤー — 同上、Multi-layer Quality Controlの構成要素として言及 [Qiita](https://qiita.com/y-morimatsu/items/13581b6db23770d1a4f6)
- Amazon Q CLI — さくらのAI Meetup vol.12「バイブコーディング」でAIコーディングエージェントの例として言及 [connpass](https://sakura-ai.connpass.com/event/361525/)
- ステアリングループ — 「実践ハーネスエンジニアリング：ステアリングループを実例から読み解く」LT [connpass](https://aid.connpass.com/event/391153/)
- Even G2 — 「Claude CodeとEven G2で広がる世界」LT(スマートグラスデバイス) [connpass](https://aid.connpass.com/event/391153/)
- Company as a Filesystem — 「Claude Codeで会社を経営する — Company as a Filesystem」LT [connpass](https://aid.connpass.com/event/391153/)
- HCI(ヒューマンコンピュータインタラクション) — 「Claude Codeと仕事する — 音声入力と自作キーボードのすすめ」LTで言及 [connpass](https://aid.connpass.com/event/391153/)
- 音声入力 — 同上 [connpass](https://aid.connpass.com/event/391153/)
- スプリントマネジメント — 「AI駆動 スプリントマネジメント」LT [Zenn](https://zenn.dev/almondo/articles/0fd942ade1ee67)
- Google Cloud Agent Engine(Vertex AI Agent Engine) — 「AIエージェント開発 ハンズオン」でAgent Engineを用いたデプロイ実習 [connpass](https://genai-users.connpass.com/event/357403/)
- PBI(プロダクトバックログアイテム) — 「hooksのStopをつかって永遠にpbi定義&開発を繰り返させ続ける」LT [connpass](https://aid.connpass.com/event/361635/)
- dotfiles — 「Claude Codeをdotfiles管理しよう！」LT [connpass](https://aid.connpass.com/event/361635/)
- スクラム(Scrum) `(※既存: agile の別名)` — 「スクラムイベントの議事録をAIが書く時代 〜Claude Code活用事例〜」LT [connpass](https://aid.connpass.com/event/361635/)
- Notion — Cursor Meetup Fukuoka #2「CursorでNotionと仲良くなる with tips」LT [connpass](https://aiau.connpass.com/event/384755/)

調査元: connpass(Claude Code Meetup Japan #2/#4/#5/#6/#7、Claude Code活用LT会、AI駆動開発勉強会 第1〜3回、AI AgentOps LT大会、CA.ai#3、第3回AIエージェントソフトウェア開発勉強会、さくらのAI Meetup vol.12、Cursor Meetup Fukuoka #2、AIエージェント開発ハンズオン)、Zenn(AI Agent勉強会 Vol.3/5/8、AI駆動開発勉強会メモ・振り返り記事)、Qiita(AI駆動開発カンファレンス2026夏 参加レポート)。Cursor Meetup Tokyo/OsakaなどLTタイトル・資料が未公開のイベントは対象外とした。

---

## 4. 既存の用語集に載っている基本語(抜粋)

調査元(9サイト): [G-gen「生成AIを理解する14の基礎用語」](https://g-gen.co.jp/useful/General-tech/introductory-guide-generative-ai/) / [AI総研「ビジネス向けの生成AI用語集20選」](https://metaversesouken.com/ai/generative_ai/terms/) / [テックキャンプ「初心者向けIT用語40選」](https://tech-camp.in/note/technology/55696/) / [LB MEDIA「IT用語集」](https://lb-media.jp/management-2/basic_knowledge_technology_0016/) / [クーシー「比べてわかるWeb制作用語24選」](https://coosy.co.jp/blog/webproduction-terms/) / [スタートアップカフェ大阪「専門用語30選」](https://startupcafe-ku.osaka/journal/column/2136/) / [note(りょーた)「IT用語30選」](https://note.com/ryootalife/n/na838ecd37b9c) / [ねんごろ「生成AI用語集」](https://nengoro.com/generation_ai/fundamentals/fundamentals-01-70/) / [CareerForge「生成AIの用語」](https://careerforge.jp/ai-terms-japanese/)

**生成AI・機械学習系**
- 事前学習 — 大規模データセットでAIモデルを最初に訓練する段階 [G-gen]
- AI TRiSM — AI利用のリスク・信頼性・セキュリティを管理する考え方 [G-gen]
- ベクトル検索 `(※既存: embedding の別名)` — データを数値(ベクトル)に変換し類似度で検索する手法 [G-gen]
- Transformer(トランスフォーマー) — 自己注意機構を特徴とする、現代の生成AIの基盤技術 [G-gen][AI総研]
- 特徴量 — データの中で予測に重要な要素・パターン [G-gen]
- 画像生成AI — テキストの指示から画像を作り出す生成AI [AI総研]
- GAN — 2つのモデルを競わせて学習させる生成技術 [AI総研]
- VAE — 画像の認識・生成を行う生成モデルの一種 [AI総研]
- ディープフェイク — AIで本物そっくりの映像・音声を合成する技術 [AI総研]
- 学習データ `(※既存: training の別名)` — AIモデルの学習に使われるデータ群 [ねんごろ]
- 知識のカットオフ — AIが学習した情報が更新されている最終時点 [CareerForge]

**IT基礎(ハード・ソフト・ネットワーク)**
- ブラウザー — Webページを表示するためのソフト [テックキャンプ]
- インターネット — 世界中のコンピュータをつなぐネットワーク [テックキャンプ]
- ネットワーク — コンピュータ同士が接続された状態・仕組み [テックキャンプ]
- ソフトウェア — コンピュータ上で動くアプリケーション全般 [テックキャンプ]
- OS — コンピューターの基本操作を司るシステムソフト [テックキャンプ]
- ハードウェア — コンピュータの物理的な部品・装置 [テックキャンプ]
- UI — 人とデバイスの接点(操作画面など) [テックキャンプ]
- GUI — 画面上のアイコンなどで操作するインターフェース [テックキャンプ]
- CUI — 文字入力で操作するインターフェース [テックキャンプ]
- IPアドレス — ネットワーク上の機器を識別する番号 [LB MEDIA]
- インターフェース — 機器やソフト同士、人との接点 [LB MEDIA]
- 仮想化 — 物理的なリソースをソフトウェア上で仮想的に扱う技術 [LB MEDIA]
- オンプレミス — 自社内にサーバーなどを設置し運用する形態 [LB MEDIA]
- エッジコンピューティング — データ処理をネットワーク末端(端末近く)で行う技術 [LB MEDIA]
- IaaS — インフラをインターネット経由で提供するクラウドサービス形態 [LB MEDIA]
- SaaS — インターネット経由でソフトウェアを利用できるサービス形態 [LB MEDIA]
- ICT — 情報通信技術 [LB MEDIA]
- IoT — モノがインターネットに接続され情報をやりとりする仕組み [LB MEDIA]
- IoB — 人の行動データをインターネットに接続する概念 [テックキャンプ]
- CPU — コンピュータの中央演算処理装置 [LB MEDIA]
- メインメモリ — コンピュータが処理中のデータを一時保存する装置 [LB MEDIA]
- ビット — コンピュータが扱う情報の最小単位 [LB MEDIA]
- LAN — 限られた範囲内のネットワーク [LB MEDIA]
- WAN — 広範囲をつなぐネットワーク [LB MEDIA]
- Wi-Fi — 無線でネットワークに接続する規格 [LB MEDIA]
- アクセスポイント — 無線LAN機器をネットワークに接続する中継機 [LB MEDIA]
- 5G — 第5世代移動通信システム [LB MEDIA]
- VR — 仮想現実 [LB MEDIA]
- ビッグデータ — 従来の手法では扱いきれない大量・多様なデータ [LB MEDIA]
- ブロックチェーン — 取引記録を分散管理する技術 [LB MEDIA]
- NFT — 非代替性トークン [テックキャンプ]
- RPA — 定型業務をソフトウェアロボットで自動化する技術 [LB MEDIA]
- 量子コンピューター — 量子力学の原理を利用した超高速計算機 [note(りょーた)]
- プロトコル — 通信の際の取り決め・ルール [note(りょーた)]
- VPN — 安全に通信するための仮想専用回線技術 [note(りょーた)]
- FTP — サーバーにファイルを転送するための通信方式 [スタートアップカフェ大阪]

**セキュリティ**
- ファイアウォール — 不正アクセスを防ぐ仕組み [LB MEDIA]
- セキュリティホール — システムの安全上の欠陥・弱点 [LB MEDIA]
- マルウェア — 悪意のあるソフトウェアの総称 [LB MEDIA]
- サイバー攻撃 — ネットワークやシステムへの不正な攻撃 [note(りょーた)]
- フィッシング詐欺 — 偽サイトなどで情報を盗み取る詐欺手口 [note(りょーた)]
- ランサムウェア — データを人質に身代金を要求するウイルス [note(りょーた)]
- クッキー(Cookie) — Webサイト訪問時にブラウザへ保存される情報 [LB MEDIA][クーシー]

**プログラミング基礎**
- テキストエディター — ソースコードを書くためのアプリ [テックキャンプ]
- プログラミング言語 — コンピュータへ命令を伝えるための言語 [テックキャンプ]
- ソースコード — プログラムの元になる文字列 [テックキャンプ]
- C言語 — 古くから使われるプログラミング言語の一つ [LB MEDIA]
- スクリプト言語 — 簡易に実行できるプログラミング言語 [LB MEDIA]
- ラッパー — 別の機能を異なる環境で使えるようにする仕組み [テックキャンプ]
- ロールバック — 変更前の状態に戻すこと [テックキャンプ]
- バグ — プログラムの不具合・誤り [テックキャンプ]
- 例外 — プログラムで想定されたエラー処理 [テックキャンプ]
- ファイルパス — ファイルやフォルダの場所を示す文字列 [テックキャンプ]
- 変数 — データを一時的に記憶する入れ物 [テックキャンプ]
- 代入 — 変数に値を入れること [テックキャンプ]
- 定数 — 値が変化しないデータ [テックキャンプ]
- 真/偽(真偽値) — 条件式が成り立つかどうかを表す値 [テックキャンプ]
- 算術演算子 — 「+」「-」など計算に使う記号 [テックキャンプ]
- 比較演算子 — 「<」「>」「==」など値を比較する記号 [テックキャンプ]
- 論理演算子 — 「AND」「OR」など条件を組み合わせる記号 [テックキャンプ]
- 関数・メソッド — 処理をひとまとめにしたもの [テックキャンプ]
- ループ — 処理を繰り返すこと [テックキャンプ]
- コメント — コード内に書く説明・メモ [テックキャンプ]
- クライアント — サービスを利用する側の端末・ユーザー [テックキャンプ]
- アルゴリズム — 問題を解決するための手順 [note(りょーた)]
- モジュール — プログラムを機能単位に分割した部品 [LB MEDIA]
- スクラッチ開発 — 既存システムを使わずゼロから開発すること [LB MEDIA]
- ローコード・ノーコード開発 — 最小限、またはコードを書かずに行う開発手法 [テックキャンプ]
- CRUD — Create・Read・Update・Deleteというデータ操作の基本機能 [スタートアップカフェ大阪]
- hoge — プログラムのサンプルで使われる意味のない仮の名前 [スタートアップカフェ大阪]
- α版/β版 — 正式リリース前の試作・試験版 [スタートアップカフェ大阪]

**Web制作**
- PHP — サーバーサイドで動作し動的なWebページを生成する言語 [クーシー]
- WordPress — 世界でもっとも使われているCMS [クーシー]
- CMS — Webサイトのコンテンツを管理・更新するシステム [LB MEDIA]
- URL — インターネット上のページの場所を示す文字列 [クーシー]
- ドメイン — インターネット上の住所にあたる文字列 [クーシー][LB MEDIA]
- SSL — 通信を暗号化し安全にやりとりするための規格 [クーシー]
- サイトマップ — サイト内ページの構成を示すもの [クーシー]
- バックアップ — データ消失に備えたコピーの保存 [クーシー]
- Basic認証 — Webサイトにかける簡易的な認証機能 [クーシー]
- GA4 — Webサイトの訪問後の行動を分析するツール(Google Analytics 4) [クーシー]
- サーチコンソール — サイト流入前の検索データを確認できるツール [クーシー]
- SEO — 検索エンジンでの表示順位を上げるための施策 [スタートアップカフェ大阪]
- ウェブアナリティクス — Webサイトのアクセスデータを分析すること [LB MEDIA]
- コンバージョン — Webサイトでの成果(購入・申込など)達成 [LB MEDIA]
- ワイヤーフレーム — Webページなどのレイアウト設計図 [LB MEDIA]
- リロード — ページを再読み込みすること [スタートアップカフェ大阪]
- リダイレクト — 別のURLへ自動的に転送すること [スタートアップカフェ大阪]
- リストア — バックアップからデータを復元すること [スタートアップカフェ大阪]

**開発プロセス・ビジネス系ジャーゴン**
- デフォルト — 初期設定・標準の状態 [スタートアップカフェ大阪]
- マイルストーン — プロジェクトの中間目標地点 [スタートアップカフェ大阪][LB MEDIA]
- ローンチ — 新サービスや製品を公開すること [スタートアップカフェ大阪][LB MEDIA]
- リリース — サービスや機能を公開・提供開始すること [スタートアップカフェ大阪]
- トラブルシューティング — 問題を特定し解決すること [スタートアップカフェ大阪]
- ベストエフォート — 最善を尽くすが結果を保証しない方式 [スタートアップカフェ大阪]
- ウォーターフォール — 工程を順番に進める従来型の開発手法 [スタートアップカフェ大阪]
- 落ちる — システムやアプリが突然停止すること(業界俗語) [スタートアップカフェ大阪]
- バッファ — 処理の余裕・データの一時的な緩衝領域 [スタートアップカフェ大阪]
- リソース — 業務やシステムで使われる資源(人・モノ・データなど) [LB MEDIA]
- ライセンス — ソフトウェアなどの使用許諾 [LB MEDIA]
- サブスクリプション — 定額で継続的にサービスを利用する契約形態 [LB MEDIA]
- サードパーティ — 開発元・提供元以外の第三者(企業) [LB MEDIA]
- アドオン — ソフトに機能を追加する拡張プログラム [LB MEDIA]
- アプリケーション — 特定の目的のために作られたソフトウェア [LB MEDIA]
- アクセシビリティ — 誰もが情報や機能を利用しやすくすること [LB MEDIA]
- 圧縮 — データサイズを小さくすること [LB MEDIA]
- データサイエンス — データを分析し価値を引き出す学問・技術 [LB MEDIA]
- データドリブン — データに基づいて意思決定を行う考え方 [LB MEDIA]
- テレワーク — 場所にとらわれず働く勤務形態 [LB MEDIA]
- DX — デジタル技術で業務やビジネスを変革すること [LB MEDIA][note(りょーた)]

---

## 所感

- 初心者のつまずきは大きく2系統に分かれる。(1)Claude Code/AIエージェント固有の新語・モード名(エージェンティックループ、ハーネスエンジニアリング、YOLOモード、権限モードなど)、(2)ターミナル・Git・npm・Python周りの「環境構築」用語(PATH、node_modules、SSH鍵、仮想環境、Permission deniedなど)。後者は生成AIと無関係な昔からのIT基礎知識だが、バイブコーディングで初めてターミナルに触れる非エンジニアには等しく壁になっている。
- 複数の記事が「つまずきの本質は個々の用語よりも“進め方”や“検証の仕方”がわからないことにある」と指摘していた。用語集だけでなく、エラー対処の型(4点セット、2ストライク・ルールなど)のような「振る舞いの解説」も需要があるかもしれない。
- 発信者のスラングは、コンテキスト管理系(コンテキスト腐敗、記憶が飛ぶ、コンテキストがパンパン)とコスト系(トークンを食う/溶かす、サブスク破産、従量課金沼)に密集していた。どちらもClaude Codeを一定期間使い込んだユーザーが「あるある」として発信しており、初心者が動画を見ていて置いてけぼりになりやすい領域だと考えられる。
- 「壁打ち」「丸投げ」「秘伝のタレ」「ultrathink」のように、カテゴリ1(初心者のつまずき)とカテゴリ2(発信者スラング)の両方に出てきた語がある。これは「発信者が当たり前に使う→初心者が意味を知らずつまずく」という同一現象を別角度から観測した結果であり、用語集での優先度が高いことの裏付けと見てよい。
- 勉強会(connpass)からは、ツール名・製品名(Zoltraak、GEAR.indigo、Kiro、Google ADK、Langfuse等)と、エンタープライズ運用寄りの略語(GHAS、DORA Metrics、AI-DLCなど)が特に多く出た。前者は「今話題の固有名詞」としてのカバー率、後者はやや上級者向けで1,000語構成の優先度は低めでよいかもしれない。
- 既存の初心者向け用語集(IT基礎・Web制作系)からは、AI駆動開発の文脈だけでは出てこない周辺知識(ネットワーク、セキュリティ、Web制作、開発プロセスの俗語)が多数見つかった。これらは動画中に直接AIの話として出るわけではないが、雑談や環境構築の説明で頻出しうるため、「AI用語集」ではなく「勉強会を聞くための基礎IT用語集」として別レイヤーで扱うのが良さそうだ。
- X(旧Twitter)本文の直接取得は4回の調査すべてで不可(認証制限)だった。ただし、Xの投稿・トレンドを引用・要約している note/Zenn記事は多数存在し、そこから「老害おじさん図鑑」「クランカー」「AI業務設計者」のような直近のバズ語を拾えた。X発の最新ミームを網羅するには、今後Xの検索・閲覧が可能な別ツール(公式API等)での追加調査が必要。
- 合計語数は334語(カテゴリ1: 75語、カテゴリ2: 75語、カテゴリ3: 76語、カテゴリ4: 108語)で、目標の300語を上回った。既存glossary.json(92語)との重複が確認できたものには `(※既存)` の印を付けている(VS Code、.env、オーケストレーター、権限モード、型エラー、ワンショット、スクラム、ベクトル検索、学習データ、npm/SSO/OAuth/HTTPの一部語義など)。
