@echo off
start cmd /k "cd /d "d:\Estudos Python\kleber-ai\backend" && "..\.venv\Scripts\uvicorn" main:app --reload"
start cmd /k "cd /d "d:\Estudos Python\kleber-ai\frontend" && npm run dev"
