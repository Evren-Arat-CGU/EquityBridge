# 🚨 START DEPLOYMENT NOW

**Time:** 3:00 PM  
**Demo:** 6:00 PM  
**Status:** READY TO DEPLOY

---

## ✅ PRE-DEPLOYMENT CHECKLIST

- ✅ Backend code complete (FastAPI, 21 grants)
- ✅ Frontend code complete (HTML/CSS/JS)
- ✅ Railway config (`railway.json`) ready
- ✅ Vercel config (`vercel.json`) ready
- ✅ All code pushed to GitHub
- ✅ Deployment scripts created

---

## 🚀 DEPLOYMENT STEPS (30 MINUTES TOTAL)

### 1️⃣ BACKEND → RAILWAY (10 min)

**URL:** https://railway.app/new

**Steps:**
1. Click "Deploy from GitHub repo"
2. Connect GitHub if needed (authorize, select repos)
3. Select: `Evren-Arat-CGU/EquityBridge`
4. Click "Deploy" (Railway auto-detects config)
5. Wait 2-3 minutes
6. Get URL: Settings → Networking → Generate Domain
7. Test: Open URL → Should see `{"status":"healthy"}`

**✅ Backend URL:** `https://[SAVE-THIS-URL].railway.app`

---

### 2️⃣ FRONTEND → VERCEL (10 min)

**URL:** https://vercel.com/new

**Steps:**
1. Click "Import Git Repository"
2. Connect GitHub if needed
3. Select: `Evren-Arat-CGU/EquityBridge`
4. **IMPORTANT:** Click "Edit" next to Root Directory
5. Set Root Directory to: `CGU_HACKATHON_FRESH_BUILD/frontend`
6. Framework: "Other"
7. Click "Deploy"
8. Wait 1-2 minutes
9. Get URL from Vercel dashboard

**✅ Frontend URL:** `https://[SAVE-THIS-URL].vercel.app`

---

### 3️⃣ UPDATE API URL (5 min)

**After you have Railway URL:**

**Option A: Use script**
```bash
UPDATE_API_URL.bat
# Enter Railway URL when prompted
git add frontend/config.js
git commit -m "Update API URL for production"
git push
```

**Option B: Manual**
1. Edit `frontend/config.js`
2. Change line 3 to:
   ```javascript
   window.API_URL = 'https://[YOUR-RAILWAY-URL].railway.app';
   ```
3. Save, commit, push
4. Vercel auto-redeploys

---

### 4️⃣ TEST (5 min)

1. Open frontend URL
2. Fill form:
   - Name: "Riverside Community Health Clinic"
   - Zip: "92501"
   - Mission: "Primary care for underserved"
   - Focus: "Community Health"
   - Budget: "250000"
   - Staff: "6-20 staff"
3. Submit → Should see 5 grants
4. Check console (F12) for errors

---

## 🆘 IF CORS ERROR

**Railway Dashboard:**
1. Your service → Variables
2. Add: `CORS_ORIGINS` = `https://[YOUR-VERCEL-URL].vercel.app`
3. Backend auto-redeploys

---

## 📋 FINAL REPORT

After deployment, report:

**Backend URL:** `https://[URL].railway.app`  
**Frontend URL:** `https://[URL].vercel.app`  
**Status:** ✅ Working / ❌ Errors

---

## 🎯 TIMELINE

- **3:00 PM:** Start deployment
- **3:10 PM:** Backend deployed
- **3:20 PM:** Frontend deployed
- **3:25 PM:** API URL updated
- **3:30 PM:** Testing complete
- **3:35 PM:** Ready for demo! 🎉

---

**START NOW!** 🚀

