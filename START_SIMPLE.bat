@echo off
REM Ultra-simple backend starter - stays open to show errors

echo ======================================================================
echo STARTING BACKEND (SIMPLE MODE)
echo ======================================================================
echo.

REM Change to the script directory
cd /d "%~dp0"

echo Working directory: %cd%
echo.

echo Installing dependencies (if needed)...
pip install fastapi uvicorn --break-system-packages --quiet
echo.

echo Starting server...
cd backend
python -m uvicorn main:app --reload

REM This pause will only run if the server crashes
echo.
echo ======================================================================
echo SERVER STOPPED OR CRASHED!
echo ======================================================================
pause
