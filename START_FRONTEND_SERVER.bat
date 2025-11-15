@echo off
echo ======================================================================
echo STARTING FRONTEND SERVER
echo ======================================================================
echo.
echo Frontend will be available at: http://localhost:8080
echo.
echo Press Ctrl+C to stop the server
echo.
echo ======================================================================
echo.

cd /d "%~dp0"
cd frontend
python -m http.server 8080

pause

