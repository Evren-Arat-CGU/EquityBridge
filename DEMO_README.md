# EquityBridge Demo - Quick Start

## 🚀 FASTEST WAY TO RUN DEMO

### Option 1: One-Click Launch (EASIEST)
```
Double-click: LAUNCH_DEMO.bat
```
This automatically starts backend + opens frontend!

---

## 📋 Step-by-Step Launch

### Option 2: Manual Launch

**Step 1: Verify Everything Works**
```
Double-click: RUN_DEMO_TEST.bat
```
This checks database, backend files, frontend files.

**Step 2: Start Backend**
```
Double-click: START_BACKEND_NOW.bat
```
Keep this window OPEN!

**Step 3: Open Frontend**
```
Double-click: OPEN_FRONTEND.bat
```

---

## 🧪 Testing the Demo

Fill in the form with this test data:

- **Organization Name**: Riverside Community Health Clinic
- **Zip Code**: 92501
- **Mission**: Providing health services to underserved communities
- **Focus Area**: Community Health
- **Annual Budget**: 250000
- **Staff Size**: 6-20 staff

Click **"Find Matching Grants"**

**Expected Result**: ~5 matching grants with relevance scores!

---

## 📂 Project Structure

```
CGU_HACKATHON_FRESH_BUILD/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── database.py          # Database setup
│   └── equitybridge.db      # SQLite database (21 grants)
├── frontend/
│   ├── index.html           # Main page
│   ├── app.js               # Form handling & API calls
│   └── styles.css           # Styling
├── LAUNCH_DEMO.bat          # ← START HERE (one-click)
├── RUN_DEMO_TEST.bat        # Test everything
├── START_BACKEND_NOW.bat    # Start backend only
└── OPEN_FRONTEND.bat        # Open frontend only
```

---

## ✅ What Works Right Now

- ✅ **Backend API** - FastAPI with grant matching algorithm
- ✅ **Database** - 21 California grants loaded
- ✅ **Frontend Form** - Accessible, mobile-friendly
- ✅ **Matching Logic** - Scores grants 0-100 based on:
  - Focus area match (health/environment)
  - Geographic eligibility
  - Budget fit
  - Mission alignment
- ✅ **WCAG 2.1 AA** - Keyboard navigation, screen reader friendly

---

## 🎯 For Your Team

**When they return from lunch:**

1. Show them the working demo (use LAUNCH_DEMO.bat)
2. They can focus on:
   - UI/UX improvements (frontend/)
   - Mind Studio chatbot integration
   - ArcGIS StoryMap creation
   - Testing and refinement

**Backend is DONE and working!**

---

## 🔧 Troubleshooting

**Backend won't start?**
- Make sure you have: `pip install fastapi uvicorn`
- Check if port 8000 is already in use

**No grants showing?**
- Run: `SETUP_DATABASE.bat` to reload grants

**Frontend can't connect?**
- Make sure backend is running (green text in backend window)
- Check browser console for errors (F12)

---

## 📞 Need Help?

Database has grants: Run `RUN_DEMO_TEST.bat` to verify
Backend running: Look for "Uvicorn running on http://127.0.0.1:8000"
Frontend loaded: Should see EquityBridge form in browser

**Current time**: 12:30 PM
**Time until demo**: ~5.5 hours
**Status**: Backend working, ready to demo! ✅
