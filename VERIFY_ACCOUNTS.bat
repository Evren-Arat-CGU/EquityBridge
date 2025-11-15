@echo off
echo ======================================================================
echo VERIFYING RAILWAY AND VERCEL ACCOUNTS
echo ======================================================================
echo.

echo Checking Railway CLI...
railway --version >nul 2>&1
if errorlevel 1 (
    echo [NOT INSTALLED] Railway CLI
    echo.
    echo To install:
    echo   npm install -g @railway/cli
    echo.
    echo Then login:
    echo   railway login
    echo.
) else (
    echo [OK] Railway CLI installed
    railway --version
    echo.
    echo Checking Railway login status...
    railway whoami >nul 2>&1
    if errorlevel 1 (
        echo [NOT LOGGED IN] Railway
        echo.
        echo To login:
        echo   railway login
        echo.
    ) else (
        echo [OK] Logged into Railway
        railway whoami
    )
)

echo.
echo ======================================================================
echo.

echo Checking Vercel CLI...
vercel --version >nul 2>&1
if errorlevel 1 (
    echo [NOT INSTALLED] Vercel CLI
    echo.
    echo To install:
    echo   npm install -g vercel
    echo.
    echo Then login:
    echo   vercel login
    echo.
) else (
    echo [OK] Vercel CLI installed
    vercel --version
    echo.
    echo Checking Vercel login status...
    vercel whoami >nul 2>&1
    if errorlevel 1 (
        echo [NOT LOGGED IN] Vercel
        echo.
        echo To login:
        echo   vercel login
        echo.
    ) else (
        echo [OK] Logged into Vercel
        vercel whoami
    )
)

echo.
echo ======================================================================
echo VERIFICATION COMPLETE
echo ======================================================================
echo.
echo If anything shows [NOT INSTALLED] or [NOT LOGGED IN]:
echo   1. Follow the instructions above
echo   2. Or see: SETUP_ACCOUNTS_GUIDE.md
echo.
pause

