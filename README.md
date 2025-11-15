# EquityBridge - CGU Hackathon Build
**Fresh Build - November 15, 2025**  
**Team:** Evren, Samantha, Toni, Albert  
**Demo Time:** 3:00 PM  
**Theme:** Health & Environmental Equity

---

## Project Structure

```
CGU_HACKATHON_FRESH_BUILD/
├── backend/               # FastAPI backend
│   ├── main.py           # API endpoints
│   ├── database.py       # Data storage
│   └── requirements.txt  # Python dependencies
├── frontend/             # Web interface
│   ├── index.html       # Main page
│   ├── styles.css       # Styling (accessible)
│   └── app.js           # Frontend logic
├── data/                # Data collection scripts
│   ├── scrape_990s.py   # Nonprofit data
│   └── scrape_grants.py # Grant data
└── docs/                # Documentation
    └── DEMO_SCRIPT.md   # Presentation notes
```

---

## Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** SQLite
- **Frontend:** HTML/CSS/JavaScript (accessible, WCAG 2.1 AA)
- **AI:** Mind Studio (agentic grant matching)
- **Mapping:** ArcGIS StoryMaps
- **Deploy:** Vercel (frontend) + Railway (backend)

---

## Getting Started

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python main.py
```

### 2. Data Collection
```bash
cd data
python scrape_990s.py
python scrape_grants.py
```

### 3. Frontend
Open `frontend/index.html` in browser (or use live server)

---

## Key Features to Build

1. **Geographic Grant Matching**
   - User inputs org profile (location, mission, budget)
   - AI matches relevant grants
   - Returns top 5 with explanations

2. **Accessibility First**
   - WCAG 2.1 AA compliance
   - Keyboard navigation
   - Screen reader compatible
   - High contrast colors

3. **ArcGIS Integration**
   - Embed tool in StoryMap
   - Show funding desert visualization
   - Interactive demo

---

## Timeline

- **Hour 1 (10:00-11:00):** Backend + data collection
- **Hour 2 (11:00-12:00):** Frontend + Mind Studio setup
- **Hour 3 (12:00-1:00):** Integration + ArcGIS StoryMap
- **Hour 4 (1:00-2:00):** Testing + accessibility
- **Hour 5 (2:00-3:00):** Demo prep + presentation

---

## Critical Rules

✅ **All code written from scratch during hackathon**  
✅ **Only open-source libraries**  
✅ **No proprietary IP from other projects**  
✅ **Clean git commit history**  

---

## Contact

Team coordination: [decide - Slack/Discord/Text]
