@echo off
echo ======================================================================
echo STARTING EQUITYBRIDGE BACKEND
echo ======================================================================
echo.
echo Starting FastAPI server on http://localhost:8000
echo.
echo Keep this window OPEN while testing the demo!
echo.
echo Press Ctrl+C to stop the server
echo.
echo ======================================================================
echo.

cd /d "%~dp0"
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

pause

