@echo off
rem Windows用の起動ファイル。ダブルクリックすると技術用語ガイドが起動する。
chcp 65001 >nul
cd /d "%~dp0"
if not exist .env (
  echo .env ファイルがありません。.env.example をコピーして .env を作り、JevのAPIキーを書いてください。
  pause
  exit /b 1
)
where python >nul 2>nul
if errorlevel 1 (
  echo Python が見つかりません。https://www.python.org/downloads/ からインストールしてください。インストール時に「Add python.exe to PATH」にチェックを入れてください。
  pause
  exit /b 1
)
start "" "http://localhost:8765"
python app\server.py
pause
