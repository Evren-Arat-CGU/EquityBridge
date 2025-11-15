@echo off
echo ======================================================================
echo QUICK STATUS CHECK - EquityBridge
echo ======================================================================
echo.

echo Checking Backend Status...
curl -s http://localhost:8000/ >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Backend NOT running!
    echo Action: Run START_BACKEND_NOW.bat
) else (
    echo [OK] Backend is running at http://localhost:8000
)

echo.
echo Checking Database...
if exist "backend\equitybridge.db" (
    echo [OK] Database exists
) else (
    echo [WARNING] Database not found
    echo Action: Run python backend\database.py
)

echo.
echo Checking Deployment Accounts...
railway --version >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Railway CLI not installed
    echo Action: npm install -g @railway/cli
) else (
    echo [OK] Railway CLI installed
)

vercel --version >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Vercel CLI not installed
    echo Action: npm install -g vercel
) else (
    echo [OK] Vercel CLI installed
)

echo.
echo ======================================================================
echo Status check complete!
echo ======================================================================
pause

