@echo off
echo ================================================================
echo RAILWAY BACKEND DEPLOYMENT - AUTOMATED
echo ================================================================
echo.
echo This will:
echo 1. Install Railway CLI
echo 2. Deploy your backend
echo 3. Get you the URL
echo.
echo ================================================================
echo.

echo Installing Railway CLI...
call npm install -g @railway/cli
echo.

echo Railway CLI installed!
echo.
echo Opening browser for login...
call railway login
echo.

echo After you login in browser, come back here and press any key...
pause
echo.

echo Deploying backend...
cd /d "%~dp0backend"
call railway init
call railway up
echo.

echo ================================================================
echo DEPLOYMENT COMPLETE!
echo ================================================================
echo.
echo Your Railway URL should appear above.
echo Look for: https://something.railway.app
echo.
echo Copy that URL and paste it in chat!
echo.
pause
