# 🚨 START DEPLOYMENT NOW - 3 HOURS TO DEMO

**Current Time:** 3:00 PM  
**Demo Time:** 6:00 PM  
**Status:** READY TO DEPLOY

---

## ✅ PRE-DEPLOYMENT CHECKLIST

All deployment configs are ready:
- ✅ Railway config (`railway.json`, `Procfile`) - Ready
- ✅ Vercel config (`vercel.json`) - Ready
- ✅ Backend CORS configured - Ready
- ✅ Frontend API URL configurable - Ready
- ✅ All files pushed to GitHub - Ready

---

## 🚀 DEPLOYMENT INSTRUCTIONS

### **OPTION 1: Use the Quick Checklist (RECOMMENDED)**
Open: **`QUICK_DEPLOY_CHECKLIST.md`** - Follow step-by-step

### **OPTION 2: Use the Detailed Guide**
Open: **`EMERGENCY_DEPLOY_NOW.md`** - Complete instructions

---

## ⚡ FASTEST PATH (30 minutes)

### 1. BACKEND → RAILWAY (15 min)

1. Go to: https://railway.app
2. Login (email or GitHub)
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. If GitHub not connected: Settings → Connected Accounts → Connect GitHub
5. Select: **Evren-Arat-CGU/EquityBridge**
6. Railway auto-detects config ✅
7. Wait 2-3 minutes for build
8. **COPY BACKEND URL:** `https://________________.railway.app`
9. Test: Open URL in browser → Should see `{"status":"healthy"}`

**✅ BACKEND URL:** `https://________________.railway.app`

---

### 2. FRONTEND → VERCEL (15 min)

1. Go to: https://vercel.com
2. Login (email or GitHub)
3. Click **"Add New..."** → **"Project"**
4. Select **"Import Git Repository"**
5. If GitHub not connected: Settings → Git → Connect GitHub
6. Select: **Evren-Arat-CGU/EquityBridge**
7. **IMPORTANT:** Set **Root Directory** to: `CGU_HACKATHON_FRESH_BUILD/frontend`
8. Framework: **Other** (or auto-detect)
9. Click **"Deploy"**
10. Wait 1-2 minutes
11. **COPY FRONTEND URL:** `https://________________.vercel.app`

**✅ FRONTEND URL:** `https://________________.vercel.app`

---

### 3. CONNECT FRONTEND TO BACKEND (5 min)

1. Edit `frontend/config.js`:
   ```javascript
   window.API_URL = 'https://[your-railway-url].railway.app';
   ```
2. Commit and push:
   ```bash
   git add frontend/config.js
   git commit -m "Update API URL for production"
   git push
   ```
3. Vercel auto-redeploys (1-2 minutes)

---

### 4. TEST END-TO-END (10 min)

1. Open frontend URL: `https://[vercel-url].vercel.app`
2. Fill form:
   - Name: "Riverside Community Health Clinic"
   - Zip: "92501"
   - Mission: "Providing primary care to underserved families"
   - Focus: "Community Health"
   - Budget: "250000"
   - Staff: "6-20 staff"
3. Click "Find Matching Grants"
4. **Verify:** See 5 matching grants with scores

**If CORS Error:**
- Railway → Variables → Set `CORS_ORIGINS` = `https://[vercel-url].vercel.app`
- Redeploy backend

---

## 📋 REPORT BACK

When done, report:
- **Backend URL:** `https://________________.railway.app`
- **Frontend URL:** `https://________________.vercel.app`
- **Status:** ✅ Working / ⚠️ Issues

---

## 🆘 IF STUCK

1. Check `EMERGENCY_DEPLOY_NOW.md` for detailed troubleshooting
2. Check Railway/Vercel logs for errors
3. Verify GitHub repo is accessible
4. Test backend directly: `https://[railway-url]/api/match-grants`

---

**START NOW!** 🚀
