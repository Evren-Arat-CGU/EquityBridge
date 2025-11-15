@echo off
echo ================================================================
echo DEPLOY WITH FULL LOGGING - WINDOW STAYS OPEN
echo ================================================================
echo.
echo Logging everything to: deployment_log.txt
echo.

REM Start logging
call :main 2>&1 | tee deployment_log.txt
pause
exit /b

:main
echo ================================================================
echo STEP 1: INSTALLING RAILWAY CLI
echo ================================================================
echo.

call npm install -g @railway/cli
if errorlevel 1 (
    echo.
    echo ERROR: Failed to install Railway CLI
    echo.
    echo Do you have Node.js/npm installed?
    echo Check: npm --version
    echo.
    goto :error
)

echo.
echo ================================================================
echo STEP 2: RAILWAY LOGIN
echo ================================================================
echo.
echo Browser will open for login...
echo.

call railway login
if errorlevel 1 (
    echo.
    echo ERROR: Railway login failed
    echo.
    goto :error
)

echo.
echo Login successful!
echo.

echo ================================================================
echo STEP 3: DEPLOYING BACKEND
echo ================================================================
echo.

cd /d "%~dp0backend"
echo Current directory: %CD%
echo.

echo Initializing Railway project...
call railway init
if errorlevel 1 (
    echo.
    echo ERROR: Railway init failed
    echo.
    goto :error
)

echo.
echo Deploying to Railway...
call railway up
if errorlevel 1 (
    echo.
    echo ERROR: Railway deployment failed
    echo Check the logs above for details
    echo.
    goto :error
)

echo.
echo ================================================================
echo BACKEND DEPLOYED SUCCESSFULLY!
echo ================================================================
echo.

echo Getting your Railway URL...
call railway status
echo.

cd /d "%~dp0"

echo.
echo ================================================================
echo STEP 4: INSTALLING VERCEL CLI
echo ================================================================
echo.

call npm install -g vercel
if errorlevel 1 (
    echo.
    echo ERROR: Failed to install Vercel CLI
    echo.
    goto :error
)

echo.
echo ================================================================
echo STEP 5: DEPLOYING FRONTEND
echo ================================================================
echo.

cd /d "%~dp0frontend"
echo Current directory: %CD%
echo.

call vercel --prod
if errorlevel 1 (
    echo.
    echo ERROR: Vercel deployment failed
    echo.
    goto :error
)

echo.
echo ================================================================
echo ALL DEPLOYMENTS COMPLETE!
echo ================================================================
echo.
echo Check above for your URLs!
echo.
echo Also saved in: deployment_log.txt
echo.
goto :end

:error
echo.
echo ================================================================
echo DEPLOYMENT FAILED - CHECK ERRORS ABOVE
echo ================================================================
echo.
echo Full log saved in: deployment_log.txt
echo.
goto :end

:end
cd /d "%~dp0"
echo.
echo Press any key to close...
pause >nul
exit /b
