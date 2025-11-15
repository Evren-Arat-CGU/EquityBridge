@echo off
cd /d "%~dp0"
cd backend
echo Starting backend server...
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
pause
