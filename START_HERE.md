# START HERE - EquityBridge Hackathon Setup

## ⚡ 5-Minute Quickstart

You have **5 agents** and **automation scripts** ready. Here's your gameplan:

---

## 🎯 STEP 1: Set Up Cursor Agents (2 minutes)

1. **Open Cursor**
2. **Open this folder:**
   ```
   C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD
   ```

3. **Create agents** (one at a time):
   - Open `docs/CURSOR_AGENTS.md`
   - Copy each agent prompt
   - In Cursor: Click "+" for new agent
   - Paste prompt
   - Name it (backend-developer, frontend-developer, etc.)

4. **You now have 5 specialized agents:**
   - Backend Agent
   - Frontend Agent
   - Data Agent
   - Testing Agent
   - Accessibility Agent

---

## 🤖 STEP 2: Create Automation Scripts (1 minute)

Tell me via MCP:

> **"Create priority scripts 1-3"**

I'll build:
1. Sample Data Generator → Test without waiting for real data
2. Database Setup → One-command database creation
3. Quick Test Script → Verify everything works

**OR** pick specific scripts from `docs/MCP_AUTOMATION.md`

---

## 🚀 STEP 3: Start Building (NOW)

### Option A: Test with sample data (FASTEST)
```
1. Tell me: "Create Sample Data Generator"
2. Run it: python scripts/generate_sample_data.py
3. Use Backend Agent to build API
4. Use Frontend Agent to build interface
5. Test with sample data
6. Replace with real data later
```

### Option B: Get real data first
```
1. Tell me: "Create Grants.gov fetcher"
2. Tell me: "Create nonprofit data fetcher"
3. Run both scripts (takes ~10 minutes)
4. Use Backend Agent to build API
5. Use Frontend Agent to build interface
```

**Recommendation: Option A** - Test fast, add real data later

---

## 📋 WORKFLOW EXAMPLE

### Hour 1: Foundation (RIGHT NOW)
```
1. Create automation scripts (me via MCP)
2. Backend Agent: "Build FastAPI skeleton"
3. Data Agent: "Run sample data generator" 
4. Frontend Agent: "Create basic HTML structure"
```

### Hour 2: Core Features
```
1. Backend Agent: "Implement matching algorithm"
2. Frontend Agent: "Build org profile form"
3. Testing Agent: "Test form submission"
```

### Hour 3: Integration
```
1. Backend Agent: "Connect Mind Studio API"
2. Frontend Agent: "Display grant results"
3. Testing Agent: "Test end-to-end flow"
```

### Hour 4: Accessibility
```
1. Accessibility Agent: "Run WCAG compliance check"
2. Frontend Agent: "Fix accessibility issues"
3. Testing Agent: "Test with screen reader"
```

### Hour 5: Demo Prep
```
1. Testing Agent: "Run final tests"
2. All Agents: "Fix any bugs"
3. Practice your presentation
```

---

## 🎨 ARCGIS STORYMAP INTEGRATION

### When you're ready (Hour 4):

1. **Deploy your app:**
   - Tell me: "Create deployment scripts"
   - Deploy backend to Railway
   - Deploy frontend to Vercel
   - Get live URLs

2. **Create StoryMap:**
   - 4 sections (problem, solution, demo, impact)
   - Embed your app in section 3
   - Takes ~30 minutes

3. **Integration:**
   - Just paste your Vercel URL into StoryMap
   - Done! Your tool lives inside the story

**Guide:** See `QUICKSTART.md` for details

---

## 💡 PRO TIPS

### Using Agents:
- **One task at a time** - "Build the API endpoint for X"
- **Switch agents for different domains** - Don't use Backend Agent for CSS
- **Tell agents what was just done** - Provide context when switching

### Using MCP (Me):
- **I create scripts and automation** - Data fetching, testing, setup
- **You build features in Cursor** - API endpoints, UI, logic
- **We work in parallel** - Faster together!

### Time Management:
- **First 3 hours: Core functionality** - Must work!
- **Hour 4: Polish and accessibility** - Make it shine
- **Hour 5: Demo prep** - Practice your pitch

---

## 🆘 IF THINGS BREAK

### Backend not starting?
→ Check `backend/requirements.txt` installed
→ Check `backend/.env` file exists
→ Ask Backend Agent: "Debug startup error"

### Frontend not loading?
→ Check `frontend/index.html` opens in browser
→ Check browser console for errors
→ Ask Frontend Agent: "Fix loading issues"

### No data showing?
→ Check `data/` folder has JSON files
→ Check backend is loading data
→ Ask Testing Agent: "Debug data flow"

### Accessibility issues?
→ Ask Accessibility Agent: "Run WCAG audit"
→ Fix critical issues first (keyboard, screen reader)
→ Document remaining for "future work"

---

## 📞 GET HELP

**From Agents:**
- Ask them specific questions
- Give them context
- Tell them what's not working

**From Me (MCP):**
- "Create script for X"
- "Read file Y and debug"
- "Generate test data for Z"

**From Team:**
- Samantha: UX and StoryMap
- Toni & Albert: Based on their strengths

---

## ✅ SUCCESS CHECKLIST

Before 3 PM presentation:

□ App runs on localhost
□ Sample data loaded OR real data loaded
□ Org profile form works
□ Grant matching returns results
□ Results display on screen
□ Keyboard navigation works
□ Screen reader tested (at least once)
□ Demo scenario prepared
□ Presentation practiced
□ StoryMap created (optional but recommended)

---

## 🎯 YOUR FIRST ACTIONS

Right now, do these three things:

1. **Tell me:** "Create priority scripts 1-3"
2. **Open Cursor** in the fresh build folder
3. **Create the 5 agents** from `docs/CURSOR_AGENTS.md`

Then you're ready to build! 🚀

---

**Questions? Ask me or check:**
- `docs/CURSOR_AGENTS.md` - All agent prompts
- `docs/MCP_AUTOMATION.md` - Scripts I can create
- `QUICKSTART.md` - Technical details
- `README.md` - Project overview

**Let's build this! What do you want to tackle first?**
