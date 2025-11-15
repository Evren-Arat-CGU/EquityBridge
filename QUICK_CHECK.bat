@echo off
echo ============================================================
echo EQUITYBRIDGE - QUICK STATUS CHECK
echo ============================================================
echo.

cd /d "%~dp0"

python TEST_EVERYTHING.py

echo.
echo ============================================================
echo.
echo To test the full system:
echo   1. Run: START_BACKEND.bat
echo   2. Open: frontend/index.html
echo.
echo Full instructions in: STATUS_REPORT.md
echo.
pause
