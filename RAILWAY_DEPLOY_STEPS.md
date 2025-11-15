# 🚀 RAILWAY DEPLOYMENT STEPS - DO NOW

**Repository:** https://github.com/Evren-Arat-CGU/EquityBridge  
**Status:** Config files updated and pushed to GitHub

---

## ⚡ DEPLOY NOW (5 minutes)

### 1. Go to Railway
**URL:** https://railway.app

### 2. Login/Sign Up
- Click "Login" or "Start a New Project"
- **Use "Login with GitHub"** (fastest!)
- Authorize Railway

### 3. Create New Project
**Where to find it:**
- Look for **"New Project"** button (usually big button on dashboard)
- OR **"+"** icon in top right → "New Project"
- OR **"New"** dropdown in top navigation → "Project"
- OR try direct link: https://railway.app/new

**Then:**
- Select **"Deploy from GitHub repo"**
- If prompted, authorize Railway to access GitHub
- Find and select: **Evren-Arat-CGU/EquityBridge**

### 4. Railway Will Auto-Detect
Railway should automatically:
- Detect Python project
- Use `railway.json` config
- Start building

**If it doesn't auto-detect:**
- Go to Settings → Deploy
- Root Directory: `CGU_HACKATHON_FRESH_BUILD` (or leave blank)
- Build Command: `cd backend && pip install -r requirements.txt`
- Start Command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`

### 5. Wait for Deployment
- Watch the build logs
- Should take 2-3 minutes
- Look for: "Deployment successful"

### 6. Get Your URL
- Railway will show your app URL
- Format: `https://[app-name].railway.app`
- **Copy this URL!**

### 7. Test It
Open in browser:
```
https://[your-app].railway.app/
```

Should see:
```json
{"status":"healthy","service":"EquityBridge API","version":"1.0.0"}
```

---

## 🔧 ENVIRONMENT VARIABLES (Optional)

In Railway dashboard → Variables:
- `CORS_ORIGINS` = `*` (for now, update later with frontend URL)
- `HOST` = `0.0.0.0` (usually not needed)
- `PORT` = Railway sets this automatically

---

## ✅ AFTER DEPLOYMENT

1. **Test backend:**
   - Health: `https://[url]/`
   - API docs: `https://[url]/docs`
   - Test endpoint: `https://[url]/api/match-grants`

2. **Update frontend:**
   - Update `frontend/config.js` with Railway URL
   - Or set `window.API_URL` to Railway URL

3. **Share with Samantha:**
   - Give her the Railway URL
   - She'll update Mind Studio to use it

---

## 🆘 TROUBLESHOOTING

**Build fails:**
- Check build logs in Railway
- Verify `backend/requirements.txt` exists
- Check Python version (Railway uses 3.11+)

**App won't start:**
- Check start command is correct
- Verify PORT is set (Railway does this)
- Check logs for errors

**Database issues:**
- SQLite file won't persist on Railway
- Database will be recreated on startup (from database.py)
- This is fine for demo!

---

**GO TO RAILWAY NOW AND DEPLOY!** 🚀

