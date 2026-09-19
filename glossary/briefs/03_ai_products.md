あなたは、初心者向けIT用語集の執筆担当です。作業ディレクトリは、このリポジトリのルートです。

最初に必ず `glossary/SPEC.md`(仕様書。レベル基準・解説の書き方・誤爆を防ぐ別名ルール)と `glossary.json`(既存の190語。重複禁止)を読んでください。

## あなたの担当
- 出力先: `glossary/parts/03_ai_products.json`
- idの接頭辞: `aip_`
- 目標語数: 120語(±10%)
- 担当範囲: **AI関連の製品・サービス・企業・モデルの固有名**。AI駆動開発の勉強会やXの投稿で名前が出るもの。
  - AI企業・研究機関: Google DeepMind, Meta AI, Microsoft, xAI, Mistral, DeepSeek, Alibaba(Qwen), Cohere, Stability AI, Sakana AI, Preferred Networks, ELYZA, NVIDIA など
  - モデル・モデルファミリー: GPTシリーズ, 推論モデル(oシリーズ等), Llama, Qwen, DeepSeek, Mistral, Gemma, Grok, Whisper, Stable Diffusion, FLUX, Sora, Veo, Imagen, Nano Banana など(バージョン番号に依存しない説明にする)
  - 対話・検索・業務AI: Microsoft Copilot, Genspark, Felo, Manus, ChatGPTの機能名(GPTs, Canvas, Deep Research, エージェントモード), Claudeの機能名(Artifacts, Projects, Claude in Chrome, Cowork等), Geminiの機能名(Gem, Deep Research), Google AI Studio, Vertex AI, Azure OpenAI Service, Amazon Q, Apple Intelligence など
  - AIコーディング系の製品: Kiro, Antigravity, Gemini CLI, Codex CLI, Aider, Roo Code, Continue, Zed, JetBrains AI, Amp, Jules, Lovable, Firebase Studio, Base44 など(Cursor, Windsurf, Cline, Devin, Copilot, v0, Bolt, Replit は既存)
  - ノーコードAI・自動化: Zapier, Make, Power Automate, Coze, Flowise, Langflow, GAS(Google Apps Script) など(Dify, n8nは既存)
  - 画像・動画・音声・資料: Midjourney, DALL-E, Adobe Firefly, Canva AI, Runway, Kling, Pika, HeyGen, ElevenLabs, Suno, Udio, VOICEVOX, Gamma, Napkin AI, Notion AI など
  - 開発者向けAI基盤: OpenRouter, LiteLLM, LangGraph, LlamaIndex, CrewAI, AutoGen, Mastra, Vercel AI SDK, Pinecone, Weaviate, Chroma, pgvector, Groq, Cerebras, Together AI, Replicate, Modal, LM Studio, vLLM, llama.cpp, Deepgram, TypeSafe AIのJev など
- 担当外(他の人が書く): 概念語(RAG、エージェント等)、Claude Codeの機能名(スキル、フック、MCP等)、AI以外の開発ツール・クラウド(GitHub, AWS, Vercel, Supabase等)。
- 注意: 事実の正確さが最重要。**開発元と「何をするものか」だけ**を書き、バージョン・価格・「最新の」「最強の」は書かない。確信が持てない製品はWeb検索で確認するか、入れない。
- 注意: 製品名は音声認識でカタカナになりやすいので、カタカナ読みの別名を必ず入れる(`Midjourney` → `ミッドジャーニー`)。日常語と同じ読みの製品(Manus, Make, Zed, Amp, Pika, Gamma など)は `other` を書く。誤爆が避けられないなら英字表記の別名だけにする。

例に挙げた語に限らず、担当範囲で初心者が勉強会やXの投稿で目にしそうな語を自分でも洗い出して網羅してください。

書き終えたら `python3 glossary/validate.py glossary/parts/03_ai_products.json` を実行し、エラーがなくなるまで直してください。他のファイルは編集しないでください。サーバーの起動やgit操作もしないでください。最終報告は語数・レベル別内訳・迷った点だけを数行で(用語の一覧は貼らない)。
