@echo off
echo ================================================================
echo DEPLOY - NEVER CLOSES - SEE ALL ERRORS
echo ================================================================
echo.

cd /d "%~dp0"

echo Installing Railway CLI...
npm install -g @railway/cli
echo.
echo Railway CLI install completed (check for errors above)
echo.
pause
echo.

echo Opening browser for Railway login...
railway login
echo.
echo Login step completed (check for errors above)
echo.
pause
echo.

echo Deploying backend...
cd backend
railway init
echo.
echo Railway init completed (check for errors above)
echo.
pause
echo.

railway up
echo.
echo Railway deployment completed (check for errors above)
echo.
pause
echo.

echo Getting Railway URL...
railway status
echo.
pause
echo.

cd ..
echo.

echo Installing Vercel CLI...
npm install -g vercel
echo.
echo Vercel CLI install completed (check for errors above)
echo.
pause
echo.

echo Deploying frontend...
cd frontend
vercel --prod
echo.
echo Vercel deployment completed (check for errors above)
echo.
pause
echo.

cd ..
echo.
echo ================================================================
echo ALL DONE!
echo ================================================================
echo.
echo Your URLs should be shown above.
echo.
echo This window will stay open.
echo Press any key when you've copied your URLs...
pause
