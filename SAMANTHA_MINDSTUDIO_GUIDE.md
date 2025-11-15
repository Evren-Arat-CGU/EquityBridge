# 🤖 MIND STUDIO SETUP GUIDE - EquityBridge Grant Advisor
## Complete Instructions for Building the Conversational AI Agent

**For: Samantha**  
**Project: EquityBridge - CGU Hackathon**  
**Time Required: 45-60 minutes**  
**Goal: Build conversational AI that helps nonprofits find grants**

---

## 📋 TABLE OF CONTENTS

1. [Overview - What You're Building](#overview)
2. [Step 1: Rename Agent](#step-1-rename)
3. [Step 2: Set Up Functions (API Call)](#step-2-functions)
4. [Step 3: Configure User Inputs](#step-3-user-inputs)
5. [Step 4: Build the Workflow](#step-4-workflow)
6. [Step 5: Test the Agent](#step-5-testing)
7. [Step 6: Publish & Get Embed Code](#step-6-publish)
8. [Troubleshooting](#troubleshooting)

---

## 🎯 OVERVIEW {#overview}

### What You're Building:

**EquityBridge Grant Advisor** - A conversational AI that:
- Chats naturally with nonprofit organizations
- Extracts information about their organization through conversation
- Calls our backend API to find matching grants
- Presents grant matches with relevance scores
- Guides users through next steps

### How It Works:

```
User: "Hi, I need help finding grants"
Agent: "I'm EquityBridge! Tell me about your organization's mission"
User: "We run a health clinic in Riverside serving low-income families"
Agent: "That's wonderful work! What's your annual budget?"
User: "$250,000"
Agent: "How many staff members do you have?"
User: "8 people"
Agent: "Let me find grants for you..."
[Calls API with extracted information]
Agent: "I found 5 grants! Here's your best match:
       CDC Healthy Communities Program (95% match)
       $50,000-$250,000, Deadline: June 2025
       Why: Perfect match for community health in California..."
```

### Technical Architecture:

```
Mind Studio Agent → Extracts data from conversation
                  ↓
               Calls API: POST /api/match-grants
                  ↓
           Backend (already built) → Returns matching grants
                  ↓
           Mind Studio → Presents results conversationally
```

---

## 📝 STEP 1: RENAME YOUR AGENT {#step-1-rename}

### Instructions:

1. At the top of the screen, you'll see "Untitled AI Agent"
2. Click on it to rename
3. Change to: **EquityBridge Grant Advisor**
4. Click anywhere else to save

**✅ Checkpoint:** Title bar now shows "EquityBridge Grant Advisor"

---

## ⚙️ STEP 2: SET UP FUNCTIONS (API CALL) {#step-2-functions}

This is where we configure the API call to our backend.

### 2.1 Open Functions Panel

1. In the left sidebar, click **"Functions"** (has a ⚡ icon)
2. Click **"+ Add Function"** or **"New Function"** button

### 2.2 Configure the Function

**Function Name:**
```
find_matching_grants
```

**Description:**
```
Calls the EquityBridge API to find grants matching the organization's profile
```

### 2.3 Configure the API Call

**Method:**
```
POST
```

**URL:**
```
http://localhost:8000/api/match-grants
```

**IMPORTANT NOTE:** After we deploy the backend, we'll change this to the live URL (like https://equitybridge.railway.app/api/match-grants). For now, use localhost for testing.

**Headers:**
Click "Add Header" and enter:
```
Key: Content-Type
Value: application/json
```

### 2.4 Define Input Parameters

The function needs these inputs (extracted from conversation):

Click "Add Parameter" for each:

| Parameter Name | Type | Required | Description |
|---------------|------|----------|-------------|
| `name` | String | Yes | Organization name |
| `zip_code` | String | Yes | Zip code (5 digits) |
| `county` | String | No | County name |
| `mission` | String | Yes | Organization mission statement |
| `focus_area` | String | Yes | "health", "environment", or "both" |
| `annual_budget` | Number | Yes | Annual budget in dollars |
| `staff_size` | String | Yes | "1-5", "6-20", "21-50", or "50+" |

### 2.5 Request Body Template

In the "Request Body" section, enter this JSON:

```json
{
  "name": "{{name}}",
  "zip_code": "{{zip_code}}",
  "county": "{{county}}",
  "mission": "{{mission}}",
  "focus_area": "{{focus_area}}",
  "annual_budget": {{annual_budget}},
  "staff_size": "{{staff_size}}"
}
```

**Note:** The `{{variable}}` syntax tells Mind Studio to insert the actual values.

### 2.6 Expected Response Format

Mind Studio needs to know what the API returns. Configure the response:

**Response Type:** JSON

**Sample Response:**
```json
{
  "organization": "Riverside Community Health Clinic",
  "matches_found": 5,
  "grants": [
    {
      "grant_id": 1,
      "title": "CDC Healthy Communities Program",
      "funder": "Centers for Disease Control",
      "amount": "$50,000 - $250,000",
      "deadline": "2025-06-30",
      "match_score": 95.0,
      "match_reason": "Perfect focus area match (health). Grant amount aligns with your organization size.",
      "eligibility": "California-eligible"
    }
  ]
}
```

### 2.7 Save the Function

Click **"Save"** or **"Create"** button.

**✅ Checkpoint:** You should now see "find_matching_grants" in your Functions list.

---

## ✍️ STEP 3: CONFIGURE USER INPUTS {#step-3-user-inputs}

This tells Mind Studio what information to extract from the conversation.

### 3.1 Open User Inputs Panel

1. In the left sidebar, click **"User Inputs"** (has a ✍️ icon)
2. Click **"+ Add Input"** for each variable below

### 3.2 Add These User Inputs:

**Input 1: Organization Name**
```
Name: organization_name
Type: Text
Description: The name of the nonprofit organization
Example: "Riverside Community Health Clinic"
```

**Input 2: Zip Code**
```
Name: zip_code
Type: Text
Description: Organization's zip code (5 digits)
Example: "92501"
Validation: Must be 5 digits
```

**Input 3: County (Optional)**
```
Name: county
Type: Text
Description: County where organization is located
Example: "Riverside"
Required: No
```

**Input 4: Mission**
```
Name: mission
Type: Text (Long)
Description: Organization's mission statement or description of work
Example: "Providing primary care and maternal health services to low-income families"
```

**Input 5: Focus Area**
```
Name: focus_area
Type: Choice/Select
Options:
  - health
  - environment
  - both
Description: Organization's primary focus area
```

**Input 6: Annual Budget**
```
Name: annual_budget
Type: Number
Description: Organization's annual budget in dollars
Example: 250000
Minimum: 0
```

**Input 7: Staff Size**
```
Name: staff_size
Type: Choice/Select
Options:
  - 1-5
  - 6-20
  - 21-50
  - 50+
Description: Number of staff members
```

**✅ Checkpoint:** You should have 7 user inputs defined.

---

## 🔄 STEP 4: BUILD THE WORKFLOW {#step-4-workflow}

This is where you create the conversation flow.

### 4.1 Open Main Workflow

1. In the left sidebar, under **"Workflows"**, click **"Main.flow"**
2. You'll see a visual canvas with nodes and connections

### 4.2 Understanding the Workflow Canvas

- **Nodes** = Steps in the conversation
- **Connections** = Flow from one step to another
- **Toolbar** = Add new nodes (usually at top or side)

### 4.3 Build This Flow:

I'll describe each node you need to add. Look for buttons like "Add Message", "Add Question", "Add Action", etc.

---

#### NODE 1: Greeting Message

**Type:** Message/Text Response  
**Content:**
```
Hello! I'm EquityBridge, your AI grant advisor. 

I help health and environmental justice organizations in California find relevant grant funding opportunities.

Tell me about your organization - what's your mission and what kind of work do you do?
```

**Configuration:**
- This is the opening message
- Should connect to next node (asking about mission)

---

#### NODE 2: Extract Mission & Focus

**Type:** Question/Input Collection  
**What to ask:**
```
[User will respond to greeting with their mission]
```

**Extract:**
- User Input: `mission` (from their response)
- User Input: `focus_area` (analyze if they mention health/environment/both)

**AI Instruction for this node:**
```
Extract the organization's mission from the user's response. 
Determine if their focus is:
- "health" if they mention: health, medical, clinic, wellness, maternal, community health
- "environment" if they mention: environmental, conservation, air quality, water, climate, sustainability
- "both" if they mention aspects of both health and environment

Save to mission and focus_area variables.
```

**Follow-up Message:**
```
Thank you for sharing about your important work! I can see you're focused on [repeat their focus area]. 

Where is your organization based? Please share your zip code or city/county.
```

---

#### NODE 3: Extract Location

**Type:** Question/Input Collection  
**Extract:**
- User Input: `zip_code`
- User Input: `county` (if mentioned)

**AI Instruction:**
```
Extract the zip code (5 digits) from the user's response.
If they mention a county name, extract that too.
If they only mention a city, ask for zip code.
```

**Follow-up Message:**
```
Got it, [location]! 

What's your organization's approximate annual budget? Just give me a ballpark figure.
```

---

#### NODE 4: Extract Budget

**Type:** Question/Input Collection  
**Extract:**
- User Input: `annual_budget`

**AI Instruction:**
```
Extract the budget amount from the user's response.
Handle various formats:
- "$250,000" → 250000
- "250K" → 250000
- "about a quarter million" → 250000
- "two hundred fifty thousand" → 250000

If they give a range, use the midpoint.
If unclear, ask for clarification.
```

**Follow-up Message:**
```
Perfect! Last question: How many people work with your organization? Just a rough count is fine.
```

---

#### NODE 5: Extract Staff Size

**Type:** Question/Input Collection  
**Extract:**
- User Input: `staff_size`

**AI Instruction:**
```
Extract staff count and categorize:
- 1-5 people → "1-5"
- 6-20 people → "6-20"
- 21-50 people → "21-50"
- 50+ people → "50+"

Be flexible with phrasing:
- "8 staff" → "6-20"
- "just me and 2 volunteers" → "1-5"
- "about 30 people" → "21-50"
```

**Also extract if not already collected:**
- User Input: `organization_name` (if they haven't mentioned it, ask now)

**Follow-up Message:**
```
Excellent! Let me make sure I have everything:

Organization: [organization_name]
Location: [zip_code] ([county if provided])
Focus: [focus_area]
Budget: $[annual_budget]
Staff: [staff_size]

Does this look correct?
```

---

#### NODE 6: Confirmation & API Call

**Type:** Condition/Branch

**If user confirms (yes/correct/looks good):**
→ Proceed to API call

**If user wants to change something:**
→ Loop back to ask what needs correction

**For "Yes" path:**

**Message:**
```
Perfect! Let me search for grants that match your organization...
```

**Action:** Call Function `find_matching_grants`

**Function Parameters:**
```
name: {{organization_name}}
zip_code: {{zip_code}}
county: {{county}}
mission: {{mission}}
focus_area: {{focus_area}}
annual_budget: {{annual_budget}}
staff_size: {{staff_size}}
```

---

#### NODE 7: Present Results

**Type:** Message/Response with API Data

**Content:**
```
Great news! I found {{matches_found}} grants that match your organization.

Here are your top matches:

{{#each grants[:3]}}
🎯 **{{title}}** ({{match_score}}% match)

**Funder:** {{funder}}
**Amount:** {{amount}}
**Deadline:** {{deadline}}

**Why this matches:** {{match_reason}}

**Eligibility:** {{eligibility}}

---
{{/each}}

{{#if matches_found > 3}}
I have {{matches_found - 3}} more grants to share. Would you like to see them?
{{/if}}

Would you like more details on any of these grants, or help understanding how to apply?
```

**Note:** The exact syntax depends on how Mind Studio handles API responses. You might need to use their specific templating language.

---

#### NODE 8: Follow-up Questions

**Type:** Question/Branch

**Handle these user intents:**
- "Tell me more about [grant name]" → Provide details
- "How do I apply?" → Give application guidance
- "Show me more grants" → Display remaining grants
- "What if none of these work?" → Provide alternative suggestions
- "Thank you / I'm done" → Closing message

---

#### NODE 9: Closing Message

**Type:** Message

**Content:**
```
I'm glad I could help you find grant opportunities! 

Remember:
- Review deadlines carefully
- Read all eligibility requirements
- Don't hesitate to reach out to funders with questions

Good luck with your applications! Your work makes a real difference in the community. 💚
```

---

### 4.4 Connect All Nodes

Make sure each node flows to the next:
```
Start → Greeting → Mission → Location → Budget → Staff → 
Confirmation → API Call → Results → Follow-up → End
```

**✅ Checkpoint:** Your workflow should have ~9 nodes connected in sequence.

---

## 🧪 STEP 5: TEST THE AGENT {#step-5-testing}

### 5.1 Use the Preview/Test Feature

1. Look for a **"Preview"** or **"Test"** button (usually top-right)
2. Click it to open a test chat window

### 5.2 Run This Test Conversation:

**You type:**
```
Hi
```

**Agent should respond:**
```
Hello! I'm EquityBridge, your AI grant advisor...
Tell me about your organization - what's your mission and what kind of work do you do?
```

**You type:**
```
We're a community health clinic in Riverside providing primary care and maternal health services to low-income families
```

**Agent should:**
- Extract mission
- Identify focus_area as "health"
- Ask about location

**You type:**
```
92501
```

**Agent should:**
- Extract zip_code
- Ask about budget

**You type:**
```
About $250,000
```

**Agent should:**
- Extract budget as 250000
- Ask about staff

**You type:**
```
We have 8 staff members
```

**Agent should:**
- Extract staff_size as "6-20"
- Confirm all details
- Ask if correct

**You type:**
```
Yes, that's correct
```

**Agent should:**
- Call the API function
- Display matching grants with scores

### 5.3 What to Check:

**✅ Agent extracts all information correctly**
- Organization name captured
- Zip code is 5 digits
- Focus area is health/environment/both
- Budget is a number
- Staff size is in correct format

**✅ API call happens**
- Loading message appears
- No error messages
- Results appear after a moment

**✅ Results display properly**
- Grant titles show
- Match scores show (0-100%)
- Match reasons explain why
- Formatted nicely and readable

### 5.4 If Something Breaks:

**Agent doesn't extract information:**
- Check User Input configurations
- Check AI instructions in each node

**API call fails:**
- Make sure backend is running (ask Evren/team)
- Check function URL is correct
- Verify parameter mapping

**Results don't display:**
- Check the templating syntax in results node
- Verify API is returning data in expected format

---

## 🚀 STEP 6: PUBLISH & GET EMBED CODE {#step-6-publish}

### 6.1 Publish the Agent

1. Click **"Publish"** button (top-right)
2. Confirm any settings
3. Wait for "Published successfully" message

### 6.2 Get the Embed Code

1. Look for **"Share"** or **"Embed"** option
2. Copy the embed code (usually looks like HTML/iframe)
3. It will look something like:

```html
<iframe
  src="https://mindstudio.ai/embed/your-agent-id"
  width="100%"
  height="600px"
  frameborder="0">
</iframe>
```

### 6.3 Save This Information:

**Agent URL:** [copy the URL]
**Embed Code:** [copy the full iframe code]

**Give these to Evren so he can:**
- Add it to the frontend website
- Embed it in the ArcGIS StoryMap
- Test the full integration

---

## 🛠️ TROUBLESHOOTING {#troubleshooting}

### Problem: Agent doesn't understand user input

**Solution:**
- Add more examples in the AI instructions
- Use more flexible extraction logic
- Add clarifying questions when uncertain

---

### Problem: API call returns error

**Possible causes:**
1. Backend isn't running
   - Ask Evren to run: `START_BACKEND_NOW.bat`
2. URL is wrong
   - Check if it's `http://localhost:8000/api/match-grants`
3. Parameters don't match
   - Verify all 7 parameters are being sent correctly

---

### Problem: Results show but formatting is broken

**Solution:**
- Check the templating syntax in the results node
- Make sure you're accessing the API response fields correctly
- Test with simple text first, then add formatting

---

### Problem: Conversation gets stuck in a loop

**Solution:**
- Check your node connections
- Make sure conditional branches are set up correctly
- Add explicit exit conditions

---

## 📊 FINAL CHECKLIST

Before calling it done:

### Configuration:
- [ ] Agent renamed to "EquityBridge Grant Advisor"
- [ ] Function `find_matching_grants` created and configured
- [ ] All 7 user inputs defined
- [ ] Workflow has all 9 nodes
- [ ] Nodes are connected in correct order

### Testing:
- [ ] Test conversation completes successfully
- [ ] All data extracted correctly
- [ ] API call works
- [ ] Results display properly
- [ ] Match scores show (should be 0-100%)
- [ ] Follow-up questions work

### Publishing:
- [ ] Agent published successfully
- [ ] Embed code copied
- [ ] Agent URL saved
- [ ] Shared with team

---

## 🎯 SUCCESS CRITERIA

**You'll know it's working when:**

1. ✅ User can chat naturally with the agent
2. ✅ Agent extracts org info through conversation
3. ✅ API call happens automatically
4. ✅ Grants appear with match scores
5. ✅ Agent explains WHY each grant matches
6. ✅ Conversation feels natural, not robotic

---

## 💡 TIPS FOR SUCCESS

### Do's:
- ✅ Test frequently as you build each node
- ✅ Use the preview feature constantly
- ✅ Start simple, add complexity gradually
- ✅ Save your work often
- ✅ Take screenshots of your workflow for documentation

### Don'ts:
- ❌ Don't build the whole thing before testing
- ❌ Don't skip the User Inputs configuration
- ❌ Don't forget to connect nodes properly
- ❌ Don't use overly complex branching at first

---

## 📞 NEED HELP?

**Ask Evren or the team:**
- Backend API not responding
- Need the live deployment URL (after Railway deployment)
- Questions about what data the API returns

**Mind Studio Resources:**
- Getting Started Video (in the Welcome screen)
- Mind Studio University
- Product Documentation
- Community Forum

---

## 🎉 WHEN YOU'RE DONE:

**Tell the team:**
1. "Mind Studio agent is published!"
2. Share the embed code
3. Share the agent URL
4. Demo it working!

**The team can then:**
- Embed it on the website
- Add it to the StoryMap
- Test the full flow
- Polish the conversation

---

## 📝 NOTES SECTION

Use this space to track:
- Issues you encountered
- Solutions you found
- Ideas for improvements
- Questions for the team

---

**Good luck building! This is the core innovation of EquityBridge - the conversational AI that makes grant discovery accessible to everyone.** 🚀

---

**Document Version:** 1.0  
**Created for:** Samantha @ CGU Hackathon  
**Last Updated:** November 15, 2025
