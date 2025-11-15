@echo off
echo ======================================================================
echo TESTING API FOR MIND STUDIO INTEGRATION
echo ======================================================================
echo.
echo This tests if Mind Studio can successfully call our backend API
echo.
echo Make sure backend is running first!
echo (Run START_BACKEND_NOW.bat in another window)
echo.
echo ======================================================================
echo.

cd backend
python test_for_mindstudio.py
