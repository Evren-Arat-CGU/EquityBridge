# 🚀 DATA COLLECTION - QUICK START

## ✅ EASIEST WAY (Windows)

**Just double-click this file:**
```
RUN_ALL.bat
```

That's it! It will:
1. ✅ Initialize database
2. ✅ Fetch 40+ grants
3. ✅ Fetch 40+ nonprofits

Takes 3-5 minutes total.

---

## 📋 STEP-BY-STEP (If you prefer)

Run these in order (double-click each):

### Step 1: Initialize Database
```
1_INIT_DATABASE.bat
```
Creates the database with sample data.

### Step 2: Fetch Grants
```
2_FETCH_GRANTS.bat
```
Gets federal grants (Grants.gov API) + California foundation grants.

### Step 3: Fetch Nonprofits
```
3_FETCH_NONPROFITS.bat
```
Gets California nonprofit data (ProPublica API).

---

## 🐍 MANUAL (Command Line)

If batch files don't work:

```bash
# Step 1: Database
cd backend
python database.py
cd ..

# Step 2: Grants
cd data
python fetch_grants_working.py

# Step 3: Nonprofits
python fetch_nonprofits_working.py
```

---

## 📊 WHAT YOU'LL GET

After running data collection:

- **~40-50 grants** (federal + California foundations)
- **~40-50 nonprofits** (California health/environment orgs)
- **SQLite database** ready for API queries

---

## ⚠️ TROUBLESHOOTING

### "Python not found"
- Make sure Python is installed
- Make sure Python is in your PATH
- Try: `python --version`

### "API timeout" or "Connection error"
- Internet connection might be slow
- APIs might be rate-limiting
- Try running again (scripts handle errors gracefully)
- Worst case: You'll still have sample data from database.py

### "Database error"
- Make sure you're in the right folder
- Check that backend/equitybridge.db exists
- Try deleting equitybridge.db and running 1_INIT_DATABASE.bat again

---

## 💡 NEXT STEPS

After data collection is complete:

1. **Start the backend:**
   ```bash
   cd backend
   python main.py
   ```

2. **Open the frontend:**
   - Open `frontend/index.html` in your browser
   - OR use Live Server in VS Code

3. **Test matching:**
   - Fill in organization profile
   - Click "Find Grants"
   - See results!

---

## 📝 SCRIPT DETAILS

### `fetch_grants_working.py`
- Uses Grants.gov REST API
- Searches for health equity + environmental justice grants
- Adds realistic California foundation grants
- Saves to `grants` table

### `fetch_nonprofits_working.py`
- Uses ProPublica Nonprofit Explorer API
- Searches California orgs (health, environment, community)
- Gets financial data (990 forms)
- Saves to `nonprofits` table

### `RUN_ALL_DATA_COLLECTION.py`
- Master script that runs everything
- Handles errors gracefully
- Shows progress and summary

---

**Ready? Double-click `RUN_ALL.bat` and let it run! 🚀**
