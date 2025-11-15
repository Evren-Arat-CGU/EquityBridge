# EquityBridge - Quick Start Guide

## Setup (5 minutes)

### 1. Backend Setup

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Create database with sample data
python database.py

# Start server
python main.py
```

Server runs at: `http://localhost:8000`

### 2. Frontend Setup

```bash
cd frontend

# Option 1: Use Python's built-in server
python -m http.server 3000

# Option 2: Just open index.html in browser
# (Update API_URL in app.js if not using localhost:8000)
```

Frontend runs at: `http://localhost:3000`

### 3. Test It Works

1. Open browser to `http://localhost:3000`
2. Fill in organization form
3. Click "Find Matching Grants"
4. Should see sample grants appear

---

## Development Workflow

### Adding Real Grant Data

```bash
cd data

# Scrape nonprofits (optional - for visualization)
python scrape_990s.py

# Scrape grants (required - for matching)
python scrape_grants.py
```

### Modifying Matching Algorithm

Edit `backend/main.py`:

```python
@app.post("/api/match-grants")
async def match_grants(profile: OrganizationProfile):
    # Add your matching logic here
    # - Query database
    # - Score grants
    # - Return top 5
```

### Styling Changes

Edit `frontend/styles.css` - all styles use CSS variables for easy theming

---

## Deployment (When Ready)

### Backend → Railway

```bash
# Railway CLI
railway init
railway up
```

### Frontend → Vercel

```bash
# Vercel CLI
vercel
```

Update `frontend/app.js` with deployed backend URL.

---

## Integration with ArcGIS StoryMaps

1. Deploy frontend to get public URL (e.g., `https://equitybridge.vercel.app`)
2. In ArcGIS StoryMaps, add "Embed" block
3. Paste your URL
4. Adjust iframe size as needed

---

## Mind Studio Integration (TODO)

1. Create Mind Studio agent
2. Set up workflow:
   - Input: Organization profile
   - Process: Query grants, score matches
   - Output: Top 5 grants with explanations
3. Get API endpoint
4. Update `backend/main.py` to call Mind Studio API

---

## Troubleshooting

**Backend won't start:**
- Check Python version (3.9+)
- Verify all dependencies installed
- Check if port 8000 is available

**Frontend can't reach backend:**
- Verify backend is running at localhost:8000
- Check CORS settings in main.py
- Update API_URL in app.js if needed

**No grants showing:**
- Run `python backend/database.py` to create sample data
- Check browser console for errors
- Verify API is returning data (visit http://localhost:8000/api/grants)

---

## Next Steps

- [ ] Add real grant data
- [ ] Implement matching algorithm
- [ ] Integrate Mind Studio
- [ ] Test accessibility (WCAG 2.1 AA)
- [ ] Create ArcGIS StoryMap
- [ ] Deploy to production
- [ ] Practice demo presentation
