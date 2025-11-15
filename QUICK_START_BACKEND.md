# 🚀 QUICK START BACKEND

## File Location

The file is here:
```
C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD\START_BACKEND_NOW.bat
```

## How to Start Backend

### Option 1: Double-Click the File
1. Navigate to: `CGU_HACKATHON_FRESH_BUILD` folder
2. Double-click: `START_BACKEND_NOW.bat`
3. Keep the window open!

### Option 2: From Command Line
```bash
cd C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD
START_BACKEND_NOW.bat
```

### Option 3: Direct Command
```bash
cd C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD\backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Verify It's Running

Open in browser: http://localhost:8000/

Should see:
```json
{"status":"healthy","service":"EquityBridge API","version":"1.0.0"}
```

## ⚠️ IMPORTANT

**Keep the backend window OPEN!** Don't close it while testing.

---

**I just started it for you in the background - check if it's running!**

