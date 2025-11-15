# ⚡ QUICK DEPLOYMENT CHECKLIST

**Time:** 3:00 PM → 3:45 PM  
**Status:** START NOW

---

## 🚀 BACKEND → RAILWAY (15 min)

### Step 1: Railway Setup (5 min)
- [ ] Go to https://railway.app
- [ ] Login (email or GitHub)
- [ ] Click **"New Project"**
- [ ] Select **"Deploy from GitHub repo"**
- [ ] If GitHub not connected: Settings → Connected Accounts → Connect GitHub
- [ ] Select repo: **Evren-Arat-CGU/EquityBridge**

### Step 2: Configure (2 min)
- [ ] Railway auto-detects `railway.json` ✅
- [ ] If not, set:
  - Build: `cd backend && pip install -r requirements.txt`
  - Start: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`

### Step 3: Deploy (5 min)
- [ ] Railway starts building automatically
- [ ] Wait 2-3 minutes
- [ ] Get URL from Railway dashboard
- [ ] **COPY URL:** `https://________________.railway.app`

### Step 4: Test (3 min)
- [ ] Open: `https://[url].railway.app/`
- [ ] Should see: `{"status":"healthy"}`
- [ ] Test: `https://[url].railway.app/api/match-grants` (POST with test data)

**✅ BACKEND URL:** `https://________________.railway.app`

---

## 🚀 FRONTEND → VERCEL (15 min)

### Step 1: Vercel Setup (5 min)
- [ ] Go to https://vercel.com
- [ ] Login (email or GitHub)
- [ ] Click **"Add New..."** → **"Project"**
- [ ] Select **"Import Git Repository"**
- [ ] If GitHub not connected: Settings → Git → Connect GitHub
- [ ] Select repo: **Evren-Arat-CGU/EquityBridge**

### Step 2: Configure (3 min)
- [ ] **IMPORTANT:** Set **Root Directory** to: `CGU_HACKATHON_FRESH_BUILD/frontend`
- [ ] Framework: **Other** (or auto-detect)
- [ ] Build Command: (leave blank)
- [ ] Output Directory: `.` (current)

### Step 3: Environment Variable (2 min)
- [ ] Add Environment Variable:
  - Key: `VITE_API_URL`
  - Value: `https://[your-railway-url].railway.app`
- [ ] (Or update `frontend/config.js` after deployment)

### Step 4: Deploy (3 min)
- [ ] Click **"Deploy"**
- [ ] Wait 1-2 minutes
- [ ] Get URL from Vercel dashboard
- [ ] **COPY URL:** `https://________________.vercel.app`

### Step 5: Update API URL (2 min)
- [ ] Edit `frontend/config.js`:
  ```javascript
  window.API_URL = 'https://[your-railway-url].railway.app';
  ```
- [ ] Commit and push:
  ```bash
  git add frontend/config.js
  git commit -m "Update API URL for production"
  git push
  ```
- [ ] Vercel auto-redeploys

**✅ FRONTEND URL:** `https://________________.vercel.app`

---

## 🧪 TEST END-TO-END (10 min)

### Test Flow:
- [ ] Open frontend URL: `https://[vercel-url].vercel.app`
- [ ] Fill form:
  - Name: "Riverside Community Health Clinic"
  - Zip: "92501"
  - Mission: "Providing primary care to underserved families"
  - Focus: "Community Health"
  - Budget: "250000"
  - Staff: "6-20 staff"
- [ ] Click "Find Matching Grants"
- [ ] **Verify:** See 5 matching grants with scores

### If CORS Error:
- [ ] Go to Railway → Variables
- [ ] Set `CORS_ORIGINS` = `https://[vercel-url].vercel.app`
- [ ] Redeploy backend

### If API Error:
- [ ] Check Railway logs
- [ ] Verify backend URL in `frontend/config.js`
- [ ] Test backend directly: `https://[railway-url]/api/match-grants`

---

## ✅ FINAL CHECK

- [ ] Backend URL working
- [ ] Frontend URL working
- [ ] Form submission works
- [ ] Grants return with scores
- [ ] No CORS errors
- [ ] No console errors

**🎉 DEPLOYMENT COMPLETE!**

---

## 📋 URLS TO REPORT

**Backend:** `https://________________.railway.app`  
**Frontend:** `https://________________.vercel.app`  
**Status:** ✅ Working / ⚠️ Issues

