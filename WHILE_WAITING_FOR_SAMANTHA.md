# ⏰ WHAT TO DO WHILE WAITING FOR SAMANTHA

**Current Status:** Samantha working on Mind Studio  
**Your Window:** ~20-30 minutes  
**Priority:** Test everything, prepare for deployment

---

## 🚨 CRITICAL (Do First - 5 minutes)

### 1. Verify Backend is Running ⚠️
```bash
# Check if backend window is open
# Or test:
curl http://localhost:8000/
```

**If NOT running:**
```bash
START_BACKEND_NOW.bat
```

**Why:** Backend MUST be running when Samantha tests at ~1:30 PM!

---

### 2. Test End-to-End Flow (10 minutes)

**Test the form path:**
1. Open `frontend/index.html` in browser
2. Fill out form:
   - Name: "Riverside Community Health Clinic"
   - Zip: "92501"
   - Mission: "Providing primary care to underserved families"
   - Focus: "Community Health"
   - Budget: "250000"
   - Staff: "6-20 staff"
3. Click "Find Matching Grants"
4. **Verify:** You see 5 matching grants with scores

**If it doesn't work:**
- Check backend is running
- Check browser console for errors
- Fix any issues immediately

---

## ✅ IMPORTANT (Do Next - 15 minutes)

### 3. Verify Deployment Accounts

**Railway:**
- [ ] Go to: https://railway.app
- [ ] Check if logged in
- [ ] If not: Sign up/login (2 min)

**Vercel:**
- [ ] Go to: https://vercel.com
- [ ] Check if logged in
- [ ] If not: Sign up/login (2 min)

**Install CLIs:**
```bash
npm install -g @railway/cli vercel
```

**Verify:**
```bash
VERIFY_ACCOUNTS.bat
```

---

### 4. Test Local Build

```bash
TEST_LOCAL_BUILD.bat
```

**Should show:**
- [OK] Backend dependencies
- [OK] Backend imports successfully
- [OK] Frontend files exist
- [OK] Database exists

---

### 5. Prepare Demo Data

**Create a test organization profile:**
- Name: "Riverside Community Health Clinic"
- Location: "92501" (Riverside, CA)
- Mission: "Providing primary care to underserved families"
- Focus: "health"
- Budget: 250000
- Staff: "6-20"

**Save this for:**
- Samantha's testing
- Your demo presentation
- Quick reference

---

## 🎯 NICE TO HAVE (If Time Permits)

### 6. Review Presentation Script

**Read:** `DEMO_PRESENTATION_SCRIPT.md`

**Practice:**
- Time yourself (should be ~5 minutes)
- Practice transitions
- Know your talking points

---

### 7. Test Accessibility

**Keyboard Navigation:**
- Tab through the form
- Verify all fields are accessible
- Check focus indicators

**Screen Reader:**
- If you have NVDA/JAWS, test it
- Or use browser's built-in screen reader
- Verify ARIA labels work

---

### 8. Check Database

**Verify grants are loaded:**
```bash
# Check database has grants
python backend/check_database.py
```

**Should show:** 21 grants loaded

---

## 📋 CHECKLIST SUMMARY

**Must Do (20 minutes):**
- [ ] Backend running and tested
- [ ] Frontend tested end-to-end
- [ ] Deployment accounts verified
- [ ] Local build tested
- [ ] Demo data prepared

**Should Do (10 minutes):**
- [ ] Review presentation script
- [ ] Test accessibility basics
- [ ] Verify database

**Nice to Have:**
- [ ] Practice presentation
- [ ] Full accessibility audit
- [ ] Polish UI

---

## 🎯 PRIORITY ORDER

1. **Backend running** (CRITICAL - 2 min)
2. **Test form → API → results** (CRITICAL - 10 min)
3. **Verify deployment accounts** (IMPORTANT - 5 min)
4. **Test local build** (IMPORTANT - 2 min)
5. **Prepare demo data** (IMPORTANT - 2 min)
6. **Review presentation** (NICE - 10 min)

---

## ⚠️ IF SOMETHING BREAKS

**Backend not working:**
- Check errors in backend window
- Restart: `START_BACKEND_NOW.bat`
- Check database exists

**Frontend not working:**
- Check browser console
- Verify backend is running
- Check API URL in `frontend/app.js`

**Deployment issues:**
- See `DEPLOYMENT_READY.md`
- Check account status
- Verify CLIs installed

---

## 📞 WHEN SAMANTHA FINISHES

**She'll need:**
1. Backend URL: `http://localhost:8000/api/match-grants`
2. Test data (you'll have this ready)
3. Your availability to troubleshoot

**You'll need:**
1. Embed code from her
2. Agent URL
3. Then start deployment immediately

---

**Focus on testing and preparation - you have ~20-30 minutes!** ⏰

