@echo off
echo ======================================================================
echo EMERGENCY VERCEL DEPLOYMENT VIA CLI
echo ======================================================================
echo.

REM Check if Vercel CLI is installed
vercel --version >nul 2>&1
if errorlevel 1 (
    echo Installing Vercel CLI...
    npm install -g vercel
    if errorlevel 1 (
        echo ERROR: Failed to install Vercel CLI
        echo Please install manually: npm install -g vercel
        pause
        exit /b 1
    )
)

echo.
echo Step 1: Login to Vercel...
vercel login

echo.
echo Step 2: Deploying frontend...
cd frontend
vercel --prod

echo.
echo ======================================================================
echo DEPLOYMENT COMPLETE!
echo ======================================================================
echo.
echo IMPORTANT: Update API URL in Vercel dashboard:
echo Settings -^> Environment Variables -^> Add VITE_API_URL
echo Value: https://[your-railway-url]
echo.
pause

