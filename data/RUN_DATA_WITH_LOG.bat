@echo off
echo ========================================
echo EQUITYBRIDGE - DATA COLLECTION
echo ========================================
echo.
echo This will fetch grant and nonprofit data
echo Output will be saved to: data_collection_log.txt
echo.
pause

cd /d "%~dp0"

echo Running data collection...
echo This may take 2-3 minutes...
echo.

python RUN_ALL_DATA_COLLECTION.py > data_collection_log.txt 2>&1

echo.
echo ========================================
echo DONE! Opening log file...
echo ========================================
echo.

start notepad data_collection_log.txt

echo.
echo Log saved to: data_collection_log.txt
echo.
pause
