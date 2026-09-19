#!/bin/bash
# Mac用の起動ファイル。Finderでダブルクリックすると技術用語ガイドが起動する。
cd "$(dirname "$0")"
if [ ! -f .env ]; then
  echo ".env ファイルがありません。.env.example をコピーして .env を作り、JevのAPIキーを書いてください。"
  read -r -p "Enterキーで閉じます"; exit 1
fi
if ! command -v python3 >/dev/null; then
  echo "python3 が見つかりません。https://www.python.org/downloads/ からインストールしてください。"
  read -r -p "Enterキーで閉じます"; exit 1
fi
(sleep 1; open "http://localhost:8765") &
python3 app/server.py
