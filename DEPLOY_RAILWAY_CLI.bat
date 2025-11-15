@echo off
echo ======================================================================
echo EMERGENCY RAILWAY DEPLOYMENT VIA CLI
echo ======================================================================
echo.

REM Check if Railway CLI is installed
railway --version >nul 2>&1
if errorlevel 1 (
    echo Installing Railway CLI...
    npm install -g @railway/cli
    if errorlevel 1 (
        echo ERROR: Failed to install Railway CLI
        echo Please install manually: npm install -g @railway/cli
        pause
        exit /b 1
    )
)

echo.
echo Step 1: Login to Railway...
railway login

echo.
echo Step 2: Initializing Railway project...
railway init

echo.
echo Step 3: Deploying...
railway up

echo.
echo ======================================================================
echo DEPLOYMENT COMPLETE!
echo ======================================================================
echo.
echo Get your Railway URL from the dashboard or run: railway domain
echo.
pause

