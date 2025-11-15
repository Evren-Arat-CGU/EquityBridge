# ✅ DEPLOYMENT VERIFICATION CHECKLIST

**Pre-Deployment Checks:** All automated  
**Post-Deployment Checks:** Manual testing required

---

## ✅ PRE-DEPLOYMENT VERIFICATION (AUTOMATED)

### Backend Readiness
- [x] `railway.json` exists and configured
- [x] `Procfile` exists and configured
- [x] `backend/requirements.txt` exists with all dependencies
- [x] `backend/main.py` has startup event for database initialization
- [x] CORS configured to accept all origins (will update with Vercel URL)
- [x] Database initialization on startup implemented
- [x] Health endpoint (`/`) returns `{"status":"healthy"}`
- [x] API endpoint (`/api/match-grants`) implemented

### Frontend Readiness
- [x] `vercel.json` exists and configured
- [x] `frontend/config.js` exists for API URL configuration
- [x] `frontend/index.html` loads config.js before app.js
- [x] `frontend/app.js` uses `window.API_URL` for API calls
- [x] All static files present (HTML, CSS, JS)

### Database Readiness
- [x] Database file exists (`backend/equitybridge.db`)
- [x] Database has grants loaded (21+ grants)
- [x] Startup event creates database if missing
- [x] Database path is relative (works in production)

### Configuration Files
- [x] Railway config: `railway.json` ✅
- [x] Railway start: `Procfile` ✅
- [x] Vercel config: `vercel.json` ✅
- [x] API config: `frontend/config.js` ✅

---

## 🧪 POST-DEPLOYMENT VERIFICATION (MANUAL)

### Backend (Railway)
1. **Health Check:**
   ```
   GET https://[railway-url].railway.app/
   Expected: {"status":"healthy"}
   ```

2. **API Test:**
   ```
   POST https://[railway-url].railway.app/api/match-grants
   Body: {
     "name": "Test Org",
     "zip_code": "92501",
     "mission": "Health services",
     "focus_area": "health",
     "annual_budget": 250000,
     "staff_size": "6-20 staff"
   }
   Expected: Array of 5 grants with match scores
   ```

3. **CORS Check:**
   - Open browser console on frontend
   - Submit form
   - No CORS errors

### Frontend (Vercel)
1. **Page Loads:**
   ```
   GET https://[vercel-url].vercel.app/
   Expected: HTML page with form
   ```

2. **API Connection:**
   - Open browser console
   - Check `window.API_URL` is set correctly
   - Submit form
   - Verify API calls go to Railway URL

3. **Form Submission:**
   - Fill out form
   - Submit
   - See 5 matching grants
   - Match scores display correctly

---

## 🔧 ENVIRONMENT VARIABLES NEEDED

### Railway (Backend)
- `CORS_ORIGINS` = `https://[vercel-url].vercel.app` (set after Vercel deploy)
- `PORT` = Auto-set by Railway
- `HOST` = Auto-set by Railway

### Vercel (Frontend)
- `VITE_API_URL` = `https://[railway-url].railway.app` (optional, can use config.js)
- Or update `frontend/config.js` directly

---

## 📋 DEPLOYMENT ORDER

1. **Deploy Backend to Railway** (15 min)
   - Get Railway URL
   - Test health endpoint
   - Test API endpoint

2. **Deploy Frontend to Vercel** (15 min)
   - Get Vercel URL
   - Update `frontend/config.js` with Railway URL
   - Commit and push (auto-redeploy)

3. **Update CORS** (2 min)
   - Railway → Variables → Set `CORS_ORIGINS` = Vercel URL
   - Redeploy backend

4. **Test End-to-End** (10 min)
   - Open frontend
   - Submit form
   - Verify grants return

---

## ✅ ALL SYSTEMS READY

**Status:** ✅ READY TO DEPLOY  
**Blockers:** None  
**Next Step:** Deploy backend to Railway

