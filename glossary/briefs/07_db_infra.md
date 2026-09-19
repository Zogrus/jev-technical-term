あなたは、初心者向けIT用語集の執筆担当です。作業ディレクトリは、このリポジトリのルートです。

最初に必ず `glossary/SPEC.md`(仕様書。レベル基準・解説の書き方・誤爆を防ぐ別名ルール)と `glossary.json`(既存の190語。重複禁止)を読んでください。

## あなたの担当
- 出力先: `glossary/parts/07_db_infra.json`
- idの接頭辞: `dbi_`
- 目標語数: 160語(±10%)
- 担当範囲: **データベース・データ** と **サーバー・ネットワーク・クラウド・デプロイ・運用**。中級〜上級が中心だが、初級者が最初の公開でつまずく語(デプロイ先、ドメイン設定、環境の違い)はレベル1〜2で。
  - データベース: テーブル/レコード(行)/カラム(列)/スキーマ/主キー/外部キー/リレーション/インデックス(DBの)/クエリ/SELECT・INSERT・UPDATE・DELETE/JOIN/トランザクション/ACID/デッドロック/正規化/マイグレーション/シードデータ/ORM/N+1問題/コネクションプール/レプリケーション/シャーディング/バックアップとリストア/RDB/NoSQL/キーバリューストア/ドキュメントDB/グラフDB/全文検索/RLS(行レベルセキュリティ)/ストアドプロシージャ など
  - DB・データ製品: PostgreSQL, MySQL, SQLite, MongoDB, Redis, DynamoDB, Firestore, Neon, PlanetScale, Turso, Elasticsearch, BigQuery, Snowflake, Databricks, S3/オブジェクトストレージ, データレイク/データウェアハウス, ETL, dbt, Airflow, データパイプライン, BIツール(Tableau, Looker Studio, Metabase), Airtable など
  - ネットワーク: TCP/IP, UDP, ファイアウォール, ロードバランサー, リバースプロキシ, Nginx, APIゲートウェイ, WebSocket, SSE, gRPC, GraphQL, ポーリング, 帯域, タイムアウト, CORS, CDNは既存確認, SSL証明書, Let's Encrypt, ドメイン取得, ネームサーバー設定, Aレコード/CNAME など
  - クラウド・実行基盤: IaaS/PaaS/SaaS(の技術的な区別), リージョン, 仮想マシン(VM), EC2, ECS, Fargate, Cloud Run, Heroku, Render, Railway, Fly.io, Netlify, Cloudflare Workers/Pages, エッジ関数, オートスケール, 従量課金, 無料枠, クラウド破産, IAM(ロール・ポリシー), VPC, サブネット, セキュリティグループ, マネージドサービス, コンテナイメージ, Dockerfile, Docker Compose, コンテナレジストリ, Pod, Helm など
  - デプロイ・運用: 開発環境/検証環境, プレビューデプロイ, ロールバック, ブルーグリーンデプロイ, カナリアリリース, ダウンタイム, ヘルスチェック, 死活監視, アラート, オンコール, インシデント, 障害対応, SLA/SLO, 可用性, 冗長化, フェイルオーバー, 単一障害点, バッチ処理, cron(定期実行), ジョブキュー, メッセージキュー(SQS, Kafka, Pub/Sub), ワーカー, デーモン, ログ収集, メトリクス, トレーシング, Datadog, Sentry, New Relic, Prometheus, SRE, DevOps, プラットフォームエンジニアリング, GitOps, Ansible, シークレット管理(Secrets Manager, Vault) など
- 担当外(他の人が書く): セキュリティ攻撃手法と認証方式の詳細、プログラミング概念、Git/CIの開発プロセス、AI用語、PCやWebの初歩(ブラウザ、URL、ドメインとは何か等)。
- 注意: 既存の `glossary.json` に AWS, GCP/Azure, Cloudflare, クラウド, Docker/コンテナ, Kubernetes, サーバーレス, エンドポイント, REST/HTTP, Webhook, キャッシュ, 本番環境, IaC, オブザーバビリティ, スケーリング, データベース, SQL, Supabase, Firebase, Vercel, Grafana, デプロイ 等がすでに入っている。重複に注意。
- 注意: 「ログ」「プロセス」「ワーカー」「ビュー」「ロック」「エッジ」「レコード」「テーブル」などは日常語や他の語の一部と衝突しやすい。SPECの別名ルール3・4を厳守し、複合語にするか `other` を書く。

例に挙げた語に限らず、担当範囲で初心者が勉強会やXの投稿で目にしそうな語を自分でも洗い出して網羅してください。

書き終えたら `python3 glossary/validate.py glossary/parts/07_db_infra.json` を実行し、エラーがなくなるまで直してください。他のファイルは編集しないでください。サーバーの起動やgit操作もしないでください。最終報告は語数・レベル別内訳・迷った点だけを数行で(用語の一覧は貼らない)。
