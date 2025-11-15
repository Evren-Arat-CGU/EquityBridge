# 🚨 DEPLOY NOW - STEP BY STEP (15 MINUTES EACH)

**Time:** 3:00 PM → Target: 3:45 PM  
**Repository:** https://github.com/Evren-Arat-CGU/EquityBridge

---

## 🚀 STEP 1: DEPLOY BACKEND TO RAILWAY (15 min)

### Quick Method (Web UI):

1. **Open:** https://railway.app/new
2. **Click:** "Deploy from GitHub repo"
3. **If GitHub not connected:**
   - Click "Connect GitHub"
   - Authorize Railway
   - **IMPORTANT:** Select "All repositories" or check "Evren-Arat-CGU/EquityBridge"
4. **Select repository:** `Evren-Arat-CGU/EquityBridge`
5. **Configure:**
   - **Root Directory:** Leave blank (or set to `CGU_HACKATHON_FRESH_BUILD` if needed)
   - Railway will auto-detect `railway.json` config
6. **Click:** "Deploy"
7. **Wait 2-3 minutes** for build
8. **Get URL:**
   - Click on your service
   - Go to "Settings" → "Networking"
   - Click "Generate Domain" or copy the provided URL
   - **URL looks like:** `https://equitybridge-production-xxxx.up.railway.app`
9. **Test:** Open URL in browser → Should see `{"status":"healthy"}`
10. **Copy URL** → You'll need it for Step 2

**✅ Backend URL:** `https://[YOUR-RAILWAY-URL].railway.app`

---

## 🚀 STEP 2: DEPLOY FRONTEND TO VERCEL (15 min)

### Quick Method (Web UI):

1. **Open:** https://vercel.com/new
2. **Click:** "Import Git Repository"
3. **If GitHub not connected:**
   - Click "Connect GitHub"
   - Authorize Vercel
   - Select repositories (or all)
4. **Select repository:** `Evren-Arat-CGU/EquityBridge`
5. **Configure Project:**
   - **Framework Preset:** Other
   - **Root Directory:** Click "Edit" → Set to: `CGU_HACKATHON_FRESH_BUILD/frontend`
   - **Build Command:** (leave blank - static files)
   - **Output Directory:** `.` (current directory)
6. **Environment Variables:**
   - Click "Environment Variables"
   - Add new variable:
     - **Name:** `VITE_API_URL`
     - **Value:** `https://[YOUR-RAILWAY-URL].railway.app` (from Step 1)
     - **Environments:** Production, Preview, Development (check all)
7. **Click:** "Deploy"
8. **Wait 1-2 minutes** for deployment
9. **Get URL:** Vercel will show `https://equitybridge.vercel.app` or similar
10. **Copy URL**

**✅ Frontend URL:** `https://[YOUR-VERCEL-URL].vercel.app`

---

## 🔧 STEP 3: UPDATE FRONTEND API CONFIG (2 min)

After getting Railway URL, update frontend to use it:

1. **Edit:** `frontend/config.js`
2. **Change line 3 to:**
   ```javascript
   window.API_URL = 'https://[YOUR-RAILWAY-URL].railway.app';
   ```
3. **Save and commit:**
   ```bash
   git add frontend/config.js
   git commit -m "Update API URL for production"
   git push
   ```
4. **Vercel will auto-redeploy** (takes 1-2 min)

---

## ✅ STEP 4: TEST END-TO-END (5 min)

1. **Open frontend:** `https://[YOUR-VERCEL-URL].vercel.app`
2. **Fill test form:**
   - **Organization Name:** "Riverside Community Health Clinic"
   - **Zip Code:** "92501"
   - **Mission:** "Providing primary care to underserved families"
   - **Focus Area:** "Community Health"
   - **Annual Budget:** "250000"
   - **Staff Size:** "6-20 staff"
3. **Click:** "Find Matching Grants"
4. **Expected:** See 5 grants with match scores
5. **Check browser console** (F12) for errors
6. **If CORS error:** See troubleshooting below

---

## 🆘 TROUBLESHOOTING

### CORS Error:
**Symptom:** Browser console shows "CORS policy" error

**Fix:**
1. Go to Railway dashboard
2. Click your service → "Variables"
3. Add new variable:
   - **Name:** `CORS_ORIGINS`
   - **Value:** `https://[YOUR-VERCEL-URL].vercel.app`
4. **Redeploy** backend (Railway auto-redeploys on variable change)

### Backend Not Starting:
**Check Railway logs:**
1. Railway dashboard → Your service → "Deployments"
2. Click latest deployment → "View Logs"
3. Look for errors

**Common fixes:**
- Ensure `railway.json` exists (✅ already done)
- Check Python version (Railway auto-detects)

### Frontend Not Loading:
**Check Vercel logs:**
1. Vercel dashboard → Your project → "Deployments"
2. Click latest deployment → "View Function Logs"

**Common fixes:**
- Ensure `vercel.json` exists (✅ already done)
- Check Root Directory is set to `CGU_HACKATHON_FRESH_BUILD/frontend`

---

## 📋 DEPLOYMENT CHECKLIST

- [ ] Backend deployed to Railway
- [ ] Backend URL working (`/` returns `{"status":"healthy"}`)
- [ ] Backend URL copied
- [ ] Frontend deployed to Vercel
- [ ] Environment variable `VITE_API_URL` set in Vercel
- [ ] Frontend URL working (page loads)
- [ ] `config.js` updated with Railway URL
- [ ] Frontend redeployed
- [ ] End-to-end test passes
- [ ] Grants return with match scores
- [ ] No CORS errors
- [ ] No console errors

---

## 🎯 FINAL REPORT

After deployment, fill this out:

**Backend URL:** `https://[RAILWAY-URL].railway.app`  
**Frontend URL:** `https://[VERCEL-URL].vercel.app`  
**Status:** ✅ Working / ❌ Errors (describe)

---

**START NOW!** 🚀

