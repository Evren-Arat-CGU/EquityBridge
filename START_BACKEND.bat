@echo off
echo ============================================================
echo STARTING EQUITYBRIDGE BACKEND
echo ============================================================
echo.
echo Backend will start at: http://localhost:8000
echo.
echo Keep this window OPEN while testing!
echo Press Ctrl+C to stop the server.
echo.
echo ============================================================
echo.

cd /d "%~dp0backend"

uvicorn main:app --reload
