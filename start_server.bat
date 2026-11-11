@echo off
echo ========================================================
echo Starting MediScan AI Diagnostic System (FastAPI Backend)
echo ========================================================
call .venv\Scripts\activate.bat
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
pause

