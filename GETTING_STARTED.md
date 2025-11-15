# 🚀 Getting Started - EquityBridge

**Quick setup guide to get the app running in 5 minutes**

---

## Prerequisites

- Python 3.9+ installed
- Web browser (Chrome, Firefox, Edge)
- Terminal/Command Prompt

---

## Step 1: Install Backend Dependencies (2 minutes)

```bash
cd CGU_HACKATHON_FRESH_BUILD/backend
pip install -r requirements.txt
```

**Expected output:** All packages install successfully

---

## Step 2: Initialize Database (30 seconds)

```bash
# Still in backend folder
python database.py
```

**Expected output:**
```
[OK] Database created successfully
[OK] Sample data inserted
```

This creates `equitybridge.db` with 3 sample grants.

---

## Step 3: Start Backend Server (1 minute)

```bash
# Still in backend folder
python main.py
```

**Expected output:**
```
INFO:     Started server process
INFO:     Waiting for application startup.
[OK] Database found, ready to serve
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**✅ Backend is now running on http://localhost:8000**

**Test it:** Open http://localhost:8000/docs in your browser to see the API documentation.

---

## Step 4: Open Frontend (1 minute)

**Option A: Direct file open**
- Navigate to `CGU_HACKATHON_FRESH_BUILD/frontend/`
- Double-click `index.html`
- Opens in your default browser

**Option B: Local server (recommended)**
```bash
# In a new terminal, navigate to frontend folder
cd CGU_HACKATHON_FRESH_BUILD/frontend
python -m http.server 8080
```
Then open http://localhost:8080 in your browser

---

## Step 5: Test the App (1 minute)

1. **Fill out the form:**
   - Organization Name: `Test Community Health Center`
   - Zip Code: `92501`
   - Mission: `Providing health equity services to underserved communities`
   - Focus Area: `Community Health`
   - Annual Budget: `250000`
   - Staff Size: `6-20 staff`

2. **Click "Find Matching Grants"**

3. **Expected result:**
   - Loading message appears
   - Results section shows 1-3 matching grants
   - Each grant shows:
     - Title and funder
     - Amount range
     - Deadline
     - Match score (percentage)
     - Match reason
     - Eligibility info

---

## ✅ Success Checklist

- [ ] Backend dependencies installed
- [ ] Database created with sample data
- [ ] Backend server running on port 8000
- [ ] Frontend opens in browser
- [ ] Form submission works
- [ ] Grant results appear

---

## 🐛 Troubleshooting

### Backend won't start
- **Error:** `ModuleNotFoundError: No module named 'fastapi'`
  - **Fix:** Run `pip install -r requirements.txt` in the backend folder

- **Error:** `Address already in use`
  - **Fix:** Another process is using port 8000. Kill it or change port in `main.py`

### Frontend shows "Error finding grants"
- **Check:** Is backend running? Look for `Uvicorn running on http://0.0.0.0:8000`
- **Check:** Browser console (F12) for CORS errors
- **Fix:** Make sure backend is running before submitting form

### No results appear
- **Check:** Database exists: `backend/equitybridge.db`
- **Check:** Database has grants: Run `python database.py` again
- **Check:** Browser console for JavaScript errors

### Database not found
- **Fix:** Run `python database.py` in the backend folder
- **Check:** You're running `main.py` from the backend folder (not parent folder)

---

## 📁 Project Structure

```
CGU_HACKATHON_FRESH_BUILD/
├── backend/
│   ├── main.py              # FastAPI server (START THIS)
│   ├── database.py          # Database setup (run once)
│   ├── requirements.txt     # Python dependencies
│   └── equitybridge.db      # SQLite database (auto-created)
├── frontend/
│   ├── index.html          # Main page (OPEN THIS)
│   ├── app.js              # Frontend logic
│   └── styles.css          # Styling
└── docs/                   # Documentation
```

---

## 🎯 Next Steps

Once it's working:
1. ✅ **Hour 1 Complete!** You have a working demo
2. See `ACTION_PLAN.md` for Hour 2-5 tasks
3. Add more grants to database
4. Integrate Mind Studio API
5. Deploy and create StoryMap

---

## 💡 Quick Commands Reference

```bash
# Start backend
cd backend
python main.py

# Initialize/reset database
cd backend
python database.py

# View API docs (when backend running)
# Open: http://localhost:8000/docs

# Test API directly
curl http://localhost:8000/api/grants
```

---

**Questions?** Check `ACTION_PLAN.md` or `STATUS.md` for more details.

**Ready to build! 🚀**

