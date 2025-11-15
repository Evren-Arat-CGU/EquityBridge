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

echo.
echo ================================================================
echo STEP 1: DEPLOYING BACKEND TO RAILWAY
echo ================================================================
echo.

call DEPLOY_RAILWAY.bat

echo.
echo ================================================================
echo STEP 2: DEPLOYING FRONTEND TO VERCEL
echo ================================================================
echo.

call DEPLOY_VERCEL.bat

echo.
echo ================================================================
echo ALL DONE!
echo ================================================================
echo.
echo You should now have:
echo - Backend URL (Railway)
echo - Frontend URL (Vercel)
echo.
echo Share both URLs with Samantha for StoryMap!
echo.
pause
