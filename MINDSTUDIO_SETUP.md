# 🤖 MIND STUDIO INTEGRATION GUIDE

## 📋 WHAT YOU'RE BUILDING

**EquityBridge Grant Advisor** - A conversational AI that helps nonprofits find funding through natural chat.

---

## 🎯 STEP-BY-STEP SETUP

### **STEP 1: Create Agent (YOU ARE HERE)**

In Mind Studio:
1. ✅ Click "Create New Agent"
2. Enter agent details (see below)
3. Configure API integration
4. Test the agent

---

## 📝 AGENT CONFIGURATION

### **Basic Info:**

**Agent Name:**
```
EquityBridge Grant Advisor
```

**Description:**
```
AI-powered grant discovery for health & environmental justice organizations in California. Guides users through conversation to find relevant funding.
```

**Avatar/Icon** (if available):
- Use health/environment themed icon
- Or upload EquityBridge logo if you have one

---

## 🧠 SYSTEM PROMPT

**Copy this into "System Instructions" or "Agent Prompt":**

```
You are EquityBridge, an AI grant advisor for California health and environmental justice organizations.

PERSONALITY:
- Warm, encouraging, supportive
- Celebrates community impact
- Patient and thorough
- Uses simple language
- Non-judgmental about org size

MISSION:
Help small nonprofits find relevant grant funding through natural conversation.

EXTRACT THESE DETAILS:
1. Organization name
2. Location (zip code or city/county)
3. Mission (what they do)
4. Focus: health, environment, or both
5. Annual budget (approximate)
6. Staff size: 1-5, 6-20, 21-50, or 50+

CONVERSATION STYLE:
- Ask ONE question at a time
- Listen to their story
- Reflect their language back
- Don't make them feel judged
- Build rapport before gathering data

CONVERSATION FLOW:
1. Greet: "Hi! I'm EquityBridge, your AI grant advisor..."
2. Ask about mission: "Tell me about your organization's work"
3. Clarify focus: "So you focus on [health/environment]?"
4. Ask location: "Where are you based?"
5. Ask budget: "What's your approximate annual budget?"
6. Ask staff: "How many people work with you?"
7. Confirm: "Let me make sure I have this right..."
8. Call API
9. Present results conversationally

PRESENTING GRANTS:
- Start with highest match score
- Explain WHY it matches
- Quote the match_reason from API
- Mention deadline and amount
- Ask if they want more details
- Offer next steps guidance

API CALL FORMAT:
When ready, call POST /api/match-grants with:
{
  "name": "[org name]",
  "zip_code": "[zip]",
  "county": "[county]",
  "mission": "[their description]",
  "focus_area": "[health/environment/both]",
  "annual_budget": [number],
  "staff_size": "[range]"
}

AFTER API RESPONSE:
Parse the grants array and present like:
"I found [X] grants that match your organization! Here's your best match:

🎯 [Grant Title] ([match_score]% match)
Funder: [funder]
Amount: [amount]
Deadline: [deadline]

Why this matches: [match_reason]

This grant is [eligibility]. Would you like to hear about other matches?"

IMPORTANT:
- Don't overwhelm - present 2-3 grants max initially
- Offer to share more if interested
- Help them understand match scores
- Encourage even if matches aren't perfect
- Offer to help with application process
```

---

## 🔌 API INTEGRATION SETUP

### **Look for these sections in Mind Studio:**

Might be labeled:
- "Functions"
- "API Calls"
- "Tools"
- "Actions"
- "External Integrations"

### **Configuration:**

**Function/Tool Name:**
```
find_grants
```

**API Endpoint:**
```
Method: POST
URL: http://localhost:8000/api/match-grants
```
*(Change to live URL after deployment)*

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Request Body:**
```json
{
  "name": "{{organization_name}}",
  "zip_code": "{{zip_code}}",
  "county": "{{county}}",
  "mission": "{{mission}}",
  "focus_area": "{{focus_area}}",
  "annual_budget": {{annual_budget}},
  "staff_size": "{{staff_size}}"
}
```

**Variables to Extract:**
- organization_name (string)
- zip_code (string)
- county (string, optional)
- mission (string)
- focus_area (string: "health", "environment", or "both")
- annual_budget (number)
- staff_size (string: "1-5", "6-20", "21-50", "50+")

---

## 🧪 TESTING YOUR AGENT

### **Test Conversation Script:**

```
User: "Hi"

Agent: Should say something like:
"Hello! I'm EquityBridge, your AI grant advisor. I help health and environmental justice organizations in California find relevant funding. Tell me about your organization - what's your mission?"

User: "We're a community health clinic in Riverside providing primary care to low-income families"

Agent: Should extract focus_area=health, location=Riverside, then ask:
"That's wonderful community work! What's your organization's approximate annual budget?"

User: "$250,000"

Agent: Should ask:
"Got it. And roughly how many staff members do you have?"

User: "8 people"

Agent: Should confirm and call API:
"Perfect! Let me find grants that match your organization..."
[Calls API]
"I found 5 grants that are great matches! Here's your top match:

🎯 CDC Healthy Communities Program (95% match)
..."
```

### **Expected API Response:**

```json
{
  "organization": "Community Health Clinic",
  "matches_found": 5,
  "grants": [
    {
      "grant_id": 1,
      "title": "CDC Healthy Communities Program",
      "funder": "Centers for Disease Control",
      "amount": "$50,000 - $250,000",
      "deadline": "2025-06-30",
      "match_score": 95.0,
      "match_reason": "Perfect focus area match (health). Grant amount aligns with your organization size. California-eligible grant.",
      "eligibility": "California-eligible"
    }
  ]
}
```

---

## 🚀 DEPLOYMENT STEPS

### **Phase 1: Local Testing (NOW)**
- ✅ Create Mind Studio agent
- ✅ Configure with localhost:8000
- ✅ Test conversation flow
- ✅ Verify API calls work

### **Phase 2: Deploy Backend (Next)**
- Deploy backend to Railway
- Get live URL: https://equitybridge.railway.app
- Update Mind Studio API endpoint to live URL
- Test from Mind Studio

### **Phase 3: Embed on Website**
- Get Mind Studio embed code
- Add to frontend
- Deploy frontend to Vercel
- Test complete flow

### **Phase 4: StoryMap Integration**
- Add Mind Studio widget to ArcGIS StoryMap
- Demo the conversational interface
- Show grant matching in action

---

## 🎯 CURRENT STEP

**YOU ARE HERE:**
- Filling in Mind Studio agent creation form

**NEXT:**
- Configure API integration
- Test with sample conversation
- Show me what happens!

---

## 💬 TELL ME WHEN:

1. Agent basics are filled in
2. You see API/integration options
3. You need help with any field
4. You're ready to test!

**Let's get this conversational AI working!** 🚀
