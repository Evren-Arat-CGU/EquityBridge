@echo off
echo ================================================================
echo VERCEL FRONTEND DEPLOYMENT - AUTOMATED
echo ================================================================
echo.
echo This will:
echo 1. Install Vercel CLI
echo 2. Deploy your frontend
echo 3. Get you the URL
echo.
echo ================================================================
echo.

echo Installing Vercel CLI...
call npm install -g vercel
echo.

echo Vercel CLI installed!
echo.
echo Deploying frontend...
cd /d "%~dp0frontend"
call vercel --prod
echo.

echo ================================================================
echo DEPLOYMENT COMPLETE!
echo ================================================================
echo.
echo Your Vercel URL should appear above.
echo Look for: https://something.vercel.app
echo.
echo Copy that URL and paste it in chat!
echo.
pause
