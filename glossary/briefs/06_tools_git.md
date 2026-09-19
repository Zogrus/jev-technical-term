あなたは、初心者向けIT用語集の執筆担当です。作業ディレクトリは、このリポジトリのルートです。

最初に必ず `glossary/SPEC.md`(仕様書。レベル基準・解説の書き方・誤爆を防ぐ別名ルール)と `glossary.json`(既存の190語。重複禁止)を読んでください。

## あなたの担当
- 出力先: `glossary/parts/06_tools_git.json`
- idの接頭辞: `tlg_`
- 目標語数: 150語(±10%)
- 担当範囲: **プログラミング言語・フレームワーク・ライブラリ・開発ツールの固有名** と **Git/GitHub・チーム開発の進め方**。レベル1〜3。
  - 言語: Go, Rust, Java, Kotlin, Swift, C#, C/C++, PHP, Ruby, Dart, R など(Python, JavaScript/TypeScript, HTML/CSS, SQL は既存)
  - Webフロント: Vue, Nuxt, Svelte, Angular, Astro, Remix, Tailwind CSS, shadcn/ui, Bootstrap, Vite, webpack, Storybook, jQuery, Three.js など(React, Next.jsは既存)
  - バックエンド/フルスタック: Express, Hono, NestJS, FastAPI, Django, Flask, Ruby on Rails, Laravel, Spring Boot, Prisma, Drizzle, tRPC など
  - モバイル/デスクトップ/ゲーム: Flutter, React Native, Expo, SwiftUI, Electron, Tauri, Unity, Unreal Engine, Godot など
  - パッケージ管理・実行環境: pip, uv, venv(仮想環境), conda, pnpm, yarn, bun, Deno, npx, Homebrew, winget, nvm, package.json, requirements.txt, lockファイル など(npm, Node.jsは既存)
  - 品質・テストツール: ESLint, Prettier, Biome, Jest, Vitest, Playwright, Cypress, Selenium, pytest, Ruff, mypy, Husky など
  - エディタ・周辺: Vim/Neovim, JetBrains(IntelliJ等), Xcode, Android Studio, Jupyter Notebook, Google Colab, Postman, curl, DevTools(開発者ツール), WSL, PowerShell, tmux, SSH, dotfiles, Obsidian, Notion, Figma, Miro など
  - Git/GitHub(既存にない細目): リモートとローカル, origin, mainブランチ, フィーチャーブランチ, チェックアウト, ステージング(git add), .gitignore, コミットメッセージ, リバート, リセット, リベース, スカッシュ, チェリーピック, スタッシュ, タグ, フォーク, PRの承認(Approve), ドラフトPR, ブランチ保護, GitHub Pages, GitHub CLI(gh), GitLab, Bitbucket, モノレポ, サブモジュール など
  - チーム開発・進め方: チケット/バックログ/カンバン/スプリント計画/デイリースクラム/レトロスペクティブ(振り返り)/ストーリーポイント/ベロシティ/ロードマップ/マイルストーン/リリースノート/チェンジログ/セマンティックバージョニング/ホットフィックス/フィーチャーフラグ/トランクベース開発/Git Flow/ドッグフーディング/コーディング規約/README/ADR/設計ドキュメント/ポストモーテム/モブプログラミング/Jira/Linear/Backlog など
- 担当外(他の人が書く): プログラミングの概念(変数・関数等)、データベース製品、クラウド・インフラ・デプロイ先(AWS, Vercel, Docker等)、セキュリティ、AI関連の製品(Cursor等)、ビジネス用語。
- 注意: 既存の `glossary.json` にGitの基本語(Git, コミット, ブランチ, マージ, プッシュ/プル, クローン, コンフリクト, Issue, GitHub Actions, 差分, PR, リポジトリ, ワークツリー)やアジャイル/スクラム/スプリントがすでに入っている。重複に注意。
- 注意: 製品名はカタカナ読みの別名を必ず入れる(`Tailwind` → `テイルウィンド`)。日常語と同形の名前(Go, Rust, Swift, Ruby, Dart, Deno, Bun, Express, Flask, Spring, Unity, Linear, Backlog, Husky, Ruff など)は `other` を書き、短い英字の別名に注意する(`Go` は `Go言語` `Golang` `ゴーラング` のようにする)。

例に挙げた語に限らず、担当範囲で初心者が勉強会やXの投稿で目にしそうな語を自分でも洗い出して網羅してください。

書き終えたら `python3 glossary/validate.py glossary/parts/06_tools_git.json` を実行し、エラーがなくなるまで直してください。他のファイルは編集しないでください。サーバーの起動やgit操作もしないでください。最終報告は語数・レベル別内訳・迷った点だけを数行で(用語の一覧は貼らない)。
