@echo off
echo ======================================================================
echo DEPLOYING EQUITYBRIDGE FRONTEND TO VERCEL
echo ======================================================================
echo.
echo Prerequisites:
echo 1. Vercel CLI installed: npm install -g vercel
echo 2. Logged in: vercel login
echo.
echo ======================================================================
echo.

REM Check if Vercel CLI is installed
vercel --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Vercel CLI not found!
    echo Install with: npm install -g vercel
    pause
    exit /b 1
)

echo Step 1: Checking frontend files...
if not exist "frontend\index.html" (
    echo ERROR: frontend\index.html not found!
    pause
    exit /b 1
)

echo.
echo Step 2: Deploying to Vercel...
echo NOTE: Make sure to set VITE_API_URL environment variable in Vercel dashboard
echo.
vercel --prod

echo.
echo ======================================================================
echo DEPLOYMENT COMPLETE!
echo ======================================================================
echo.
echo Update backend CORS settings with your Vercel URL
echo Share URLs with team for StoryMap integration
echo.
pause

