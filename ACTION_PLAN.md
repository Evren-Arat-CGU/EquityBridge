# 🚀 EQUITYBRIDGE - 5-HOUR HACKATHON ACTION PLAN
**Project Coordinator: Evren**  
**Demo Time: 3:00 PM**  
**Current Time: [CHECK TIME]**  
**Status: Foundation Phase**

---

## 📊 CURRENT PROJECT STATE ASSESSMENT

### ✅ What's Already Built:
- **Project Structure**: Complete folder structure (backend, frontend, data, docs)
- **Backend Skeleton**: FastAPI app with placeholder endpoints (`/api/match-grants`, `/api/grants`)
- **Frontend UI**: Complete HTML form with accessibility features (WCAG 2.1 AA compliant)
- **Database Schema**: Defined in `database.py` (grants, nonprofits tables)
- **Sample Data**: 3 sample grants in `database.py` (not yet loaded)
- **Frontend JavaScript**: Form submission logic ready, API integration ready
- **Styling**: Complete CSS with accessibility features

### ❌ What's Missing (Critical):
1. **Database Connection**: Backend not connected to SQLite database
2. **Grant Matching Logic**: Only placeholder/sample data returned
3. **Sample Data Loading**: Database needs to be initialized with sample grants
4. **Mind Studio Integration**: Not yet connected (AI matching)
5. **End-to-End Testing**: No verification that form → API → results works
6. **ArcGIS StoryMap**: Not yet created
7. **Deployment**: Not deployed (needed for StoryMap embedding)

### ⚠️ Blockers/Decisions Needed:
- **Mind Studio API Key**: Do we have credentials? (Check with team)
- **Deployment Platform**: Railway (backend) + Vercel (frontend) - accounts ready?
- **Sample Data Strategy**: Use database.py samples OR generate more realistic data?

---

## 🎯 PRIORITIZED 5-HOUR ACTION PLAN

### **HOUR 1: FOUNDATION (10:00-11:00 AM)**
**Goal: Get basic matching working with sample data**

#### Tasks:
1. **Initialize Database** (5 min)
   - Run `python backend/database.py` to create database
   - Verify `equitybridge.db` exists with sample grants
   - **Agent: Backend Agent** OR **Me (Project Coordinator)**

2. **Connect Database to API** (15 min)
   - Update `backend/main.py` to load database on startup
   - Create database query functions
   - Replace placeholder `/api/match-grants` with real database queries
   - **Agent: Backend Agent**

3. **Basic Matching Algorithm** (20 min)
   - Simple matching: filter by focus_area, geographic eligibility
   - Score grants based on: focus_area match, location match, budget fit
   - Return top 5 matches
   - **Agent: Backend Agent**

4. **Test End-to-End** (15 min)
   - Start backend: `cd backend && python main.py`
   - Open frontend in browser
   - Submit test form
   - Verify results display
   - **Agent: Testing Agent** OR **Me**

5. **Fix Critical Bugs** (5 min)
   - Fix any connection issues
   - Ensure CORS works
   - **Agent: Backend Agent**

**Hour 1 Success Criteria:**
- ✅ Backend serves real grant data from database
- ✅ Form submission returns matching grants
- ✅ Results display on frontend
- ✅ At least 3 sample grants in database

---

### **HOUR 2: CORE FEATURES (11:00 AM-12:00 PM)**
**Goal: Add AI matching and improve data quality**

#### Tasks:
1. **Expand Sample Data** (10 min)
   - Add 10-15 more realistic grants to database
   - Mix of health, environment, both
   - Various geographic eligibilities (federal, CA, county-specific)
   - **Agent: Data Agent** OR **Me**

2. **Mind Studio Integration** (25 min)
   - Get Mind Studio API credentials (check with team)
   - Create Mind Studio agent/prompt for grant matching
   - Update `/api/match-grants` to call Mind Studio for:
     - Mission statement analysis
     - Better match explanations
     - Semantic matching beyond keywords
   - **Agent: Backend Agent**

3. **Improve Matching Algorithm** (15 min)
   - Combine database filtering + Mind Studio AI scoring
   - Weight: 40% database match, 60% AI match score
   - Generate better match_reason explanations
   - **Agent: Backend Agent**

4. **Enhanced Results Display** (10 min)
   - Add grant details (description, website link)
   - Improve match score visualization
   - Add "Learn More" buttons
   - **Agent: Frontend Agent**

**Hour 2 Success Criteria:**
- ✅ 10+ grants in database
- ✅ Mind Studio integrated (or fallback if unavailable)
- ✅ Better matching quality with explanations
- ✅ Results look professional

---

### **HOUR 3: INTEGRATION & POLISH (12:00-1:00 PM)**
**Goal: Connect everything and prepare for StoryMap**

#### Tasks:
1. **Accessibility Audit** (15 min)
   - Test keyboard navigation (Tab through form)
   - Test with screen reader (NVDA/JAWS)
   - Fix any critical issues
   - **Agent: Accessibility Agent**

2. **Error Handling** (10 min)
   - Add user-friendly error messages
   - Handle API failures gracefully
   - Add loading states
   - **Agent: Frontend Agent**

3. **Deployment Prep** (20 min)
   - Prepare backend for Railway deployment
   - Prepare frontend for Vercel deployment
   - Create deployment scripts/configs
   - **Agent: Backend Agent** + **Frontend Agent**

4. **ArcGIS StoryMap Planning** (15 min)
   - Plan StoryMap structure (4 sections)
   - Prepare demo narrative
   - Identify what to embed
   - **Agent: Me (Project Coordinator)** + **Samantha (UX)**

**Hour 3 Success Criteria:**
- ✅ Accessibility verified (keyboard + screen reader)
- ✅ Error handling in place
- ✅ Deployment configs ready
- ✅ StoryMap plan documented

---

### **HOUR 4: DEPLOYMENT & STORYMAP (1:00-2:00 PM)**
**Goal: Get live URLs and create StoryMap**

#### Tasks:
1. **Deploy Backend** (15 min)
   - Deploy to Railway
   - Get backend URL
   - Test deployed API
   - **Agent: Backend Agent**

2. **Deploy Frontend** (15 min)
   - Update `app.js` with production API URL
   - Deploy to Vercel
   - Get frontend URL
   - Test deployed frontend
   - **Agent: Frontend Agent**

3. **Create ArcGIS StoryMap** (25 min)
   - Section 1: Problem (funding deserts)
   - Section 2: Solution (EquityBridge)
   - Section 3: Demo (embed live app)
   - Section 4: Impact & Future
   - **Agent: Samantha (UX)** + **Me**

4. **Integration Testing** (5 min)
   - Test embedded app in StoryMap
   - Verify all features work in embedded context
   - **Agent: Testing Agent**

**Hour 4 Success Criteria:**
- ✅ Backend live on Railway
- ✅ Frontend live on Vercel
- ✅ StoryMap created with embedded demo
- ✅ Everything works in StoryMap

---

### **HOUR 5: DEMO PREP (2:00-3:00 PM)**
**Goal: Practice and polish for presentation**

#### Tasks:
1. **Final Testing** (15 min)
   - Run through complete demo scenario
   - Test with different org profiles
   - Fix any last-minute bugs
   - **Agent: Testing Agent**

2. **Demo Script** (15 min)
   - Write 5-minute presentation script
   - Identify key talking points
   - Prepare demo data (test org profile)
   - **Agent: Me (Project Coordinator)** + **Team**

3. **Polish & Documentation** (15 min)
   - Update README with setup instructions
   - Document any known limitations
   - Create quick demo guide
   - **Agent: Me**

4. **Practice Run** (15 min)
   - Full demo practice
   - Time the presentation
   - Practice transitions
   - **Agent: Entire Team**

**Hour 5 Success Criteria:**
- ✅ Demo script ready
- ✅ Test scenario works perfectly
- ✅ Presentation practiced
- ✅ Team ready for judges

---

## 👥 AGENT DELEGATION MATRIX

| Task | Primary Agent | Backup |
|------|--------------|--------|
| Database setup | Backend Agent | Me |
| API endpoints | Backend Agent | - |
| Grant matching logic | Backend Agent | - |
| Mind Studio integration | Backend Agent | - |
| Frontend UI updates | Frontend Agent | - |
| Accessibility fixes | Accessibility Agent | Frontend Agent |
| Sample data generation | Data Agent | Me |
| Testing & QA | Testing Agent | Me |
| Deployment | Backend/Frontend Agents | - |
| StoryMap creation | Samantha + Me | - |
| Demo prep | Me + Team | - |

---

## 🚨 RISK MITIGATION

### Risk 1: Mind Studio API unavailable
**Mitigation:** Build fallback matching algorithm (database-only) first, add AI as enhancement

### Risk 2: Deployment takes too long
**Mitigation:** Use localhost for demo if needed, deploy as time allows

### Risk 3: Not enough sample data
**Mitigation:** Use database.py samples + generate 5-10 more quickly

### Risk 4: Accessibility issues found late
**Mitigation:** Build accessibility in from start (already done), audit early (Hour 3)

### Risk 5: StoryMap integration fails
**Mitigation:** Have standalone demo ready, StoryMap is bonus

---

## ✅ IMMEDIATE NEXT ACTIONS (DO NOW)

### **Action 1: Initialize Database** (2 minutes)
```bash
cd CGU_HACKATHON_FRESH_BUILD/backend
python database.py
```
**Who:** Me (Project Coordinator) - Quick task

### **Action 2: Connect Database to API** (15 minutes)
Update `backend/main.py` to:
- Import database connection
- Load grants from database on startup
- Query database in `/api/match-grants` endpoint
- Return real grant data

**Who:** Backend Agent

### **Action 3: Test Basic Flow** (5 minutes)
- Start backend: `python backend/main.py`
- Open `frontend/index.html` in browser
- Submit test form
- Verify results appear

**Who:** Testing Agent or Me

---

## 📋 DECISION LOG

### Decisions Needed:
1. **Mind Studio Credentials**: Do we have API key? (Check with team NOW)
2. **Deployment Accounts**: Railway + Vercel accounts ready? (Check NOW)
3. **Sample Data Volume**: 10 grants enough, or need 20+? (Decide Hour 1)

### Decisions Made:
- ✅ Use SQLite (simple, no setup)
- ✅ Use sample data first, real data later
- ✅ Accessibility built-in from start
- ✅ FastAPI + HTML/CSS/JS stack

---

## 🎯 SUCCESS METRICS CHECKLIST

Before 3 PM presentation, verify:

- [ ] Backend runs and serves API
- [ ] Database has 10+ grants
- [ ] Form submission works
- [ ] Grant matching returns results
- [ ] Results display correctly
- [ ] Keyboard navigation works
- [ ] Screen reader tested (at least once)
- [ ] Error handling works
- [ ] Demo scenario prepared
- [ ] Presentation script ready
- [ ] StoryMap created (bonus)
- [ ] App deployed (bonus)

---

## 📞 ESCALATION PATH

**If stuck:**
1. Try for 5 minutes
2. Ask specialized agent
3. Ask me (Project Coordinator)
4. Simplify/remove feature if blocking
5. Document limitation for demo

**Remember:** Working demo > Perfect code

---

## 🚀 LET'S BUILD!

**Your immediate next step:**

1. **Run database initialization:**
   ```bash
   cd CGU_HACKATHON_FRESH_BUILD/backend
   python database.py
   ```

2. **Then tell Backend Agent:**
   > "Connect the database to the API. Update `/api/match-grants` to query the SQLite database and return real grants. Use the sample grants from database.py."

3. **Test it:**
   - Start backend
   - Submit form
   - Verify results

**We're building! Let's go! 🚀**

---

*Last Updated: [Current Time]*  
*Next Review: End of Hour 1*

