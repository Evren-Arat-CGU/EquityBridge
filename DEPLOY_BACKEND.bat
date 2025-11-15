@echo off
echo ======================================================================
echo DEPLOYING EQUITYBRIDGE BACKEND TO RAILWAY
echo ======================================================================
echo.
echo Prerequisites:
echo 1. Railway CLI installed: npm install -g @railway/cli
echo 2. Logged in: railway login
echo 3. Project initialized: railway init
echo.
echo ======================================================================
echo.

REM Check if Railway CLI is installed
railway --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Railway CLI not found!
    echo Install with: npm install -g @railway/cli
    pause
    exit /b 1
)

echo Step 1: Testing local build...
cd backend
python -c "import fastapi, uvicorn; print('Dependencies OK')"
if errorlevel 1 (
    echo ERROR: Dependencies not installed!
    echo Run: pip install -r requirements.txt
    pause
    exit /b 1
)
cd ..

echo.
echo Step 2: Deploying to Railway...
railway up

echo.
echo ======================================================================
echo DEPLOYMENT COMPLETE!
echo ======================================================================
echo.
echo Get your backend URL from Railway dashboard
echo Update frontend/.env with the new API URL
echo.
pause

