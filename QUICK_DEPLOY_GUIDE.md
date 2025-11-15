# ⚡ QUICK DEPLOY GUIDE - 30 MINUTES

**Repository:** https://github.com/Evren-Arat-CGU/EquityBridge  
**Status:** Ready to deploy

---

## 🚀 DEPLOY BACKEND (Railway) - 10 min

1. **Go to:** https://railway.app/new
2. **Click:** "Deploy from GitHub repo"
3. **Connect GitHub** if needed (authorize, select repositories)
4. **Select:** `Evren-Arat-CGU/EquityBridge`
5. **Deploy** (Railway auto-detects `railway.json`)
6. **Get URL:** Settings → Networking → Generate Domain
7. **Test:** Open URL → Should see `{"status":"healthy"}`
8. **Copy URL** → Save it!

**Backend URL:** `https://[YOUR-URL].railway.app`

---

## 🚀 DEPLOY FRONTEND (Vercel) - 10 min

1. **Go to:** https://vercel.com/new
2. **Click:** "Import Git Repository"
3. **Connect GitHub** if needed
4. **Select:** `Evren-Arat-CGU/EquityBridge`
5. **Configure:**
   - **Root Directory:** `CGU_HACKATHON_FRESH_BUILD/frontend`
   - **Framework:** Other
6. **Environment Variables:**
   - Add: `VITE_API_URL` = `https://[YOUR-RAILWAY-URL].railway.app`
7. **Deploy**
8. **Get URL:** Vercel shows it after deployment

**Frontend URL:** `https://[YOUR-URL].vercel.app`

---

## 🔧 UPDATE API URL (5 min)

**Option 1: Run script**
```bash
UPDATE_API_URL.bat
# Enter Railway URL when prompted
git add frontend/config.js
git commit -m "Update API URL for production"
git push
```

**Option 2: Manual edit**
- Edit `frontend/config.js`
- Change to: `window.API_URL = 'https://[YOUR-RAILWAY-URL].railway.app';`
- Commit and push

---

## ✅ TEST (5 min)

1. Open frontend URL
2. Fill form with test data
3. Submit → Should see 5 grants
4. Check console (F12) for errors

---

## 🆘 IF CORS ERROR

**Railway → Variables → Add:**
- `CORS_ORIGINS` = `https://[YOUR-VERCEL-URL].vercel.app`
- Backend auto-redeploys

---

**DONE!** 🎉

