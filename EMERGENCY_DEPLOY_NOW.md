# 🚨 EMERGENCY DEPLOYMENT - 3 HOURS TO DEMO

**Time:** 3:00 PM  
**Demo:** 6:00 PM  
**Status:** DEPLOYING NOW

---

## ⚡ FASTEST PATH (30 minutes total)

### OPTION 1: Deploy from Existing Repo (FASTEST - Recommended)

We'll deploy backend and frontend from the SAME repo (EquityBridge) but configure them separately.

---

## 🚀 STEP 1: DEPLOY BACKEND TO RAILWAY (15 min)

### A. Go to Railway
1. https://railway.app
2. Login (email or GitHub)

### B. Create New Project
1. Click **"New Project"** (or "+" icon)
2. Select **"Deploy from GitHub repo"**
3. If GitHub not connected:
   - Settings → Connected Accounts → Connect GitHub
   - Grant repository access
4. Select: **Evren-Arat-CGU/EquityBridge**

### C. Configure for Backend
Railway should auto-detect. If not:

**Settings → Deploy:**
- Root Directory: `CGU_HACKATHON_FRESH_BUILD` (or leave blank if repo root)
- Build Command: `cd backend && pip install -r requirements.txt`
- Start Command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`

**OR Railway will use:**
- `railway.json` (already configured)
- `Procfile` (already configured)

### D. Set Environment Variables
**Variables tab:**
- `CORS_ORIGINS` = `*` (we'll update later with frontend URL)

### E. Deploy & Get URL
1. Railway starts building automatically
2. Wait 2-3 minutes
3. Get URL: `https://[app-name].railway.app`
4. **COPY THIS URL!**

### F. Test Backend
```
https://[your-url].railway.app/
```
Should see: `{"status":"healthy"}`

**✅ BACKEND URL:** `https://________________.railway.app`

---

## 🚀 STEP 2: DEPLOY FRONTEND TO VERCEL (15 min)

### A. Go to Vercel
1. https://vercel.com
2. Login (email or GitHub)

### B. Create New Project
1. Click **"Add New..."** → **"Project"**
2. Select **"Import Git Repository"**
3. If GitHub not connected:
   - Settings → Git → Connect GitHub
   - Grant repository access
4. Select: **Evren-Arat-CGU/EquityBridge**

### C. Configure for Frontend
**Project Settings:**
- Root Directory: `CGU_HACKATHON_FRESH_BUILD/frontend`
- Framework Preset: **Other** (or leave auto-detect)
- Build Command: (leave blank - static files)
- Output Directory: `.` (current directory)

**OR Vercel will use:**
- `vercel.json` (already configured)

### D. Set Environment Variables
**Environment Variables:**
- `VITE_API_URL` = `https://[your-railway-url].railway.app`
- (Or we'll update frontend/config.js after deployment)

### E. Deploy & Get URL
1. Click **"Deploy"**
2. Wait 1-2 minutes
3. Get URL: `https://[project-name].vercel.app`
4. **COPY THIS URL!**

### F. Update Frontend API URL
After deployment, update `frontend/config.js`:
```javascript
window.API_URL = 'https://[your-railway-url].railway.app';
```

Then commit and push (Vercel will auto-redeploy).

**✅ FRONTEND URL:** `https://________________.vercel.app`

---

## 🧪 STEP 3: TEST END-TO-END (10 min)

### Test Flow:
1. Open frontend URL in browser
2. Fill out form:
   - Name: "Riverside Community Health Clinic"
   - Zip: "92501"
   - Mission: "Providing primary care to underserved families"
   - Focus: "Community Health"
   - Budget: "250000"
   - Staff: "6-20 staff"
3. Click "Find Matching Grants"
4. **Verify:** See 5 matching grants with scores

### If CORS Error:
- Update Railway backend: `CORS_ORIGINS` = `https://[your-vercel-url].vercel.app`
- Redeploy backend

### If API Error:
- Check Railway logs
- Verify backend URL is correct in frontend
- Test backend directly: `https://[railway-url]/api/match-grants`

---

## 📋 DEPLOYMENT CHECKLIST

### Backend (Railway):
- [ ] Project created
- [ ] Repository connected
- [ ] Build successful
- [ ] URL obtained
- [ ] Health check works
- [ ] API endpoint tested

### Frontend (Vercel):
- [ ] Project created
- [ ] Repository connected
- [ ] Root directory set to `frontend/`
- [ ] Environment variable set (Railway URL)
- [ ] Deploy successful
- [ ] URL obtained
- [ ] Frontend loads

### Integration:
- [ ] Frontend API URL updated
- [ ] CORS configured
- [ ] End-to-end test passes
- [ ] Grants return with scores

---

## 🆘 IF SOMETHING BREAKS

### Backend won't build:
- Check Railway logs
- Verify `backend/requirements.txt` exists
- Check Python version

### Frontend won't deploy:
- Check Vercel logs
- Verify `frontend/` folder structure
- Check `vercel.json` config

### CORS errors:
- Update Railway `CORS_ORIGINS` with Vercel URL
- Redeploy backend

### API not working:
- Test backend directly: `https://[railway-url]/api/match-grants`
- Check Railway logs for errors
- Verify database initializes on startup

---

## ⏰ TIME TRACKING

- **3:00 PM:** Start deployment
- **3:15 PM:** Backend deployed
- **3:30 PM:** Frontend deployed
- **3:40 PM:** Testing complete
- **3:45 PM:** Ready for demo prep

---

**LET'S DEPLOY NOW!** 🚀
