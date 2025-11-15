# 🚀 DEPLOY BACKEND TO RAILWAY VIA GITHUB - NOW

**Repository:** https://github.com/Evren-Arat-CGU/EquityBridge  
**Method:** Deploy from GitHub (easiest)

---

## ⚡ QUICK STEPS (5 minutes)

### Step 1: Go to Railway
1. Go to: https://railway.app
2. Click "Login" or "Start a New Project"
3. Sign in with GitHub (fastest)

### Step 2: Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Authorize Railway to access your GitHub
4. Select repository: **Evren-Arat-CGU/EquityBridge**

### Step 3: Configure Deployment
Railway should auto-detect it's a Python project. If not:

1. **Root Directory:** Set to `CGU_HACKATHON_FRESH_BUILD` (or leave blank if repo root)
2. **Build Command:** `pip install -r backend/requirements.txt`
3. **Start Command:** `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`

### Step 4: Set Environment Variables
In Railway dashboard, go to Variables tab:
- `PORT` - Railway sets this automatically
- `HOST` - Set to `0.0.0.0` (or leave default)
- `CORS_ORIGINS` - Set to `*` for now (or your frontend URL later)

### Step 5: Deploy
1. Railway will automatically deploy
2. Wait for build to complete (~2-3 minutes)
3. Get your URL from Railway dashboard
4. Test: `https://[your-app].railway.app/`

---

## 🔧 IF AUTO-DETECTION DOESN'T WORK

### Manual Configuration:

**Create `railway.json` in repo root:**
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS",
    "buildCommand": "cd backend && pip install -r requirements.txt"
  },
  "deploy": {
    "startCommand": "cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT"
  }
}
```

**Or use Procfile:**
```
web: cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## 📋 CHECKLIST

- [ ] Logged into Railway
- [ ] Connected GitHub account
- [ ] Selected EquityBridge repository
- [ ] Configured build/start commands
- [ ] Set environment variables
- [ ] Deployment started
- [ ] Got Railway URL
- [ ] Tested backend URL

---

## 🧪 TEST AFTER DEPLOYMENT

1. **Health Check:**
   ```
   https://[your-app].railway.app/
   ```
   Should return: `{"status":"healthy"}`

2. **API Docs:**
   ```
   https://[your-app].railway.app/docs
   ```

3. **Test Endpoint:**
   ```
   POST https://[your-app].railway.app/api/match-grants
   ```

---

## ⚠️ IMPORTANT NOTES

- **Database:** SQLite file won't persist on Railway. You may need to:
  - Use Railway's volume storage, OR
  - Initialize database on startup, OR
  - Use external database (PostgreSQL)

- **CORS:** Update CORS_ORIGINS with your frontend URL after Vercel deployment

- **Environment:** Railway sets PORT automatically - don't override it

---

**Let's deploy NOW!** 🚀

