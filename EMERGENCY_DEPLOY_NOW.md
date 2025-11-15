# 🚨 EMERGENCY DEPLOYMENT - 3 HOURS TO DEMO

**Time:** 3:00 PM  
**Demo:** 6:00 PM  
**Status:** DEPLOYING NOW

---

## ⚡ FASTEST PATH (Using Existing Repo)

**Repository:** https://github.com/Evren-Arat-CGU/EquityBridge  
**Strategy:** Deploy from existing repo, configure subdirectories

---

## 🚀 STEP 1: DEPLOY BACKEND TO RAILWAY (15 min)

### Option A: Railway Web UI (Fastest if GitHub connected)

1. **Go to:** https://railway.app
2. **New Project** → **Deploy from GitHub repo**
3. **Select:** Evren-Arat-CGU/EquityBridge
4. **Configure:**
   - Root Directory: `CGU_HACKATHON_FRESH_BUILD` (or leave blank if repo root)
   - Build Command: `cd backend && pip install -r requirements.txt`
   - Start Command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
5. **Deploy** - Wait 2-3 minutes
6. **Get URL:** Railway will show `https://[app].railway.app`
7. **Test:** `https://[app].railway.app/` should return `{"status":"healthy"}`

### Option B: Railway CLI (If web UI not working)

```bash
# Install CLI
npm install -g @railway/cli

# Login
railway login

# In project folder
cd C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD

# Initialize
railway init

# Set root directory (if needed)
railway variables set RAILWAY_ROOT_DIRECTORY=CGU_HACKATHON_FRESH_BUILD

# Deploy
railway up
```

---

## 🚀 STEP 2: DEPLOY FRONTEND TO VERCEL (15 min)

### Option A: Vercel Web UI

1. **Go to:** https://vercel.com
2. **New Project** → **Import Git Repository**
3. **Select:** Evren-Arat-CGU/EquityBridge
4. **Configure:**
   - Framework Preset: Other
   - Root Directory: `CGU_HACKATHON_FRESH_BUILD/frontend`
   - Build Command: (leave blank - static files)
   - Output Directory: `.` (current directory)
5. **Environment Variables:**
   - Add: `VITE_API_URL` = `https://[your-railway-url]` (from Step 1)
6. **Deploy** - Wait 1-2 minutes
7. **Get URL:** Vercel will show `https://[app].vercel.app`

### Option B: Vercel CLI

```bash
# Install CLI
npm install -g vercel

# Login
vercel login

# In frontend folder
cd C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD\frontend

# Deploy
vercel --prod

# Set environment variable
vercel env add VITE_API_URL production
# Enter: https://[your-railway-url]
```

---

## 🔧 STEP 3: UPDATE FRONTEND API URL

After getting Railway URL, update frontend:

1. **Option A: Update config.js**
   - Edit `frontend/config.js`
   - Change: `window.API_URL = 'https://[your-railway-url]'`
   - Commit and push
   - Vercel will auto-redeploy

2. **Option B: Use Vercel Environment Variable**
   - In Vercel dashboard → Settings → Environment Variables
   - Add: `VITE_API_URL` = `https://[your-railway-url]`
   - Redeploy

---

## ✅ STEP 4: TEST END-TO-END

1. **Open frontend:** `https://[vercel-url]`
2. **Fill form:**
   - Name: "Riverside Community Health Clinic"
   - Zip: "92501"
   - Mission: "Providing primary care to underserved families"
   - Focus: "Community Health"
   - Budget: "250000"
   - Staff: "6-20 staff"
3. **Submit** - Should see 5 matching grants
4. **Check browser console** for errors
5. **Fix any CORS issues** if needed

---

## 🆘 IF CORS ERRORS

Update Railway backend CORS:
1. Railway → Variables
2. Add: `CORS_ORIGINS` = `https://[your-vercel-url]`
3. Redeploy backend

---

## 📋 DEPLOYMENT CHECKLIST

- [ ] Backend deployed to Railway
- [ ] Backend URL working (health check passes)
- [ ] Frontend deployed to Vercel
- [ ] Frontend URL working (page loads)
- [ ] API URL updated in frontend
- [ ] End-to-end test passes
- [ ] Grants return with match scores
- [ ] No CORS errors
- [ ] No console errors

---

## 🎯 TARGET TIMELINE

- **3:00 PM:** Start deployment
- **3:15 PM:** Backend deployed
- **3:30 PM:** Frontend deployed
- **3:40 PM:** Testing complete
- **3:45 PM:** Ready for demo!

---

**DEPLOY NOW!** 🚀

