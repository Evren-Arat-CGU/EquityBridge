@echo off
echo ================================================================
echo DEPLOY EVERYTHING - ONE CLICK
echo ================================================================
echo.
echo This will deploy BOTH backend and frontend automatically.
echo.
echo You'll need to:
echo 1. Login to Railway when browser opens
echo 2. Login to Vercel when prompted
echo.
echo That's it. Everything else is automatic.
echo.
echo ================================================================
pause
echo.

REM Change to script directory
cd /d "%~dp0"

echo.
echo ================================================================
echo STEP 1: DEPLOYING BACKEND TO RAILWAY
echo ================================================================
echo.

echo Installing Railway CLI...
call npm install -g @railway/cli
echo.

echo Railway CLI installed! Opening browser for login...
call railway login
echo.

echo After you login in browser, press any key to continue...
pause
echo.

echo Deploying backend...
cd backend
call railway init
call railway up
cd ..
echo.

echo.
echo ================================================================
echo STEP 2: DEPLOYING FRONTEND TO VERCEL  
echo ================================================================
echo.

echo Installing Vercel CLI...
call npm install -g vercel
echo.

echo Deploying frontend...
cd frontend
call vercel --prod
cd ..
echo.

echo.
echo ================================================================
echo ALL DONE!
echo ================================================================
echo.
echo Look above for your URLs:
echo - Railway URL: https://something.railway.app
echo - Vercel URL: https://something.vercel.app
echo.
echo Copy both URLs and share with Samantha!
echo.
pause
