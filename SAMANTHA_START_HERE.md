# 🎯 SAMANTHA - START HERE!

**Your Mission:** Build the EquityBridge conversational AI agent in Mind Studio

**Time:** 45-60 minutes  
**Current Status:** Mind Studio account open, ready to build

---

## 📚 YOUR DOCUMENTS (Read in This Order)

### 1️⃣ **SAMANTHA_MINDSTUDIO_GUIDE.md** ← **MAIN GUIDE**
**Read this FIRST!**

This is the complete, step-by-step guide with:
- Detailed instructions for every step
- What you're building and why
- All configurations needed
- Testing instructions
- Publishing steps

**Time to read:** 10-15 minutes  
**Time to build:** 30-45 minutes

---

### 2️⃣ **SAMANTHA_QUICK_REFERENCE.md** ← **COPY/PASTE CHEATSHEET**
**Keep this open while building!**

This has all the text you need to copy/paste:
- Agent name and description
- All conversation messages
- Function configuration
- User input definitions
- Test script

**Use:** When you need to copy exact text without searching through the main guide

---

### 3️⃣ **SAMANTHA_TROUBLESHOOTING.md** ← **WHEN STUCK**
**Reference when something breaks!**

Common problems and solutions:
- Agent doesn't extract info
- API call fails
- Results don't display
- Conversation loops
- Can't find buttons/options

**Use:** When something isn't working and you need quick fixes

---

## 🚀 QUICK START (If You Want to Jump In)

### Step 1: Rename Agent
- Click "Untitled AI Agent" at top
- Change to: **EquityBridge Grant Advisor**

### Step 2: Set Up Function (API Call)
- Click "Functions" in sidebar
- Add new function: `find_matching_grants`
- Configure API endpoint: `POST http://localhost:8000/api/match-grants`
- See Quick Reference for exact config

### Step 3: Add User Inputs
- Click "User Inputs" in sidebar
- Add all 7 variables (organization_name, zip_code, mission, focus_area, annual_budget, staff_size, county)
- See Quick Reference for exact definitions

### Step 4: Build Workflow
- Click "Main.flow" under Workflows
- Build conversation flow (~9 nodes)
- See Main Guide for complete flow structure

### Step 5: Test & Publish
- Use Preview to test
- Fix any issues (see Troubleshooting guide)
- Publish when working
- Get embed code for team

---

## ✅ SUCCESS CHECKLIST

**Before you call it done:**

- [ ] Agent renamed to "EquityBridge Grant Advisor"
- [ ] Function configured with correct API endpoint
- [ ] All 7 user inputs defined
- [ ] Workflow built with ~9-10 connected nodes
- [ ] Test conversation works end-to-end
- [ ] API successfully returns grants with match scores
- [ ] Results display properly formatted
- [ ] Agent published
- [ ] Embed code copied and shared with Evren

---

## 🆘 NEED HELP?

**Ask Evren/Team:**
- Backend API not working
- Need deployed URL (after deployment)
- Questions about what the API returns

**Use Troubleshooting Guide:**
- Something in Mind Studio not working
- Configuration issues
- Testing problems

**Mind Studio Resources:**
- "Getting Started Video" (in Welcome screen)
- Mind Studio University
- Product Documentation

---

## 🎯 YOUR GOAL

**Build a conversational AI that:**
1. Chats naturally with nonprofit users
2. Extracts their organization info through conversation
3. Calls the EquityBridge API
4. Shows matching grants with relevance scores
5. Explains why each grant matches
6. Guides users through next steps

**This is the CORE innovation of EquityBridge!**

It's what makes us different from "just another grant search database."

---

## ⏰ TIME BREAKDOWN

**Estimate your time:**
- Reading main guide: 10-15 min
- Setting up function & inputs: 10-15 min
- Building workflow: 20-30 min
- Testing & debugging: 10-15 min
- Publishing: 5 min

**Total: 45-75 minutes**

Don't rush - test frequently as you build!

---

## 💡 PRO TIPS

1. **Read the main guide first** - don't just jump in
2. **Keep the quick reference open** - saves time searching
3. **Test after every few nodes** - easier to debug
4. **Save frequently** - Mind Studio should auto-save but be safe
5. **Use the troubleshooting guide** - common issues have quick fixes
6. **Ask for help early** - don't spin your wheels for 30 minutes

---

## 📂 FILE LOCATIONS

All your documents are in:
```
C:\Users\evren\GRANTBRIDGE_OPEN_SOURCE\CGU_HACKATHON_FRESH_BUILD\
```

- **SAMANTHA_MINDSTUDIO_GUIDE.md** - Main instructions
- **SAMANTHA_QUICK_REFERENCE.md** - Copy/paste reference
- **SAMANTHA_TROUBLESHOOTING.md** - Problem solving

---

## 🎉 WHEN YOU'RE DONE

**Tell the team:**
1. "Mind Studio agent is published!" 🎉
2. Share the agent URL
3. Share the embed code (for website/StoryMap)
4. Demo it working!

**They'll:**
- Embed it on the frontend
- Add it to the ArcGIS StoryMap
- Test the full integration
- Polish and prepare for demo

---

## 🚀 YOU'VE GOT THIS!

This is the centerpiece of our hackathon project. The conversational AI is what makes EquityBridge special and accessible to small organizations who struggle with complex grant databases.

**Take your time, build it right, test thoroughly, and create something amazing!**

---

**Ready? Open SAMANTHA_MINDSTUDIO_GUIDE.md and let's build!** 📖

---

**Questions before you start? Ask now!**  
**Otherwise, dive into the main guide and start building!** 🚀
