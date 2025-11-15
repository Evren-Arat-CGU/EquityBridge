# 📋 MIND STUDIO - QUICK COPY/PASTE REFERENCE

**For: Samantha - EquityBridge Mind Studio Setup**

Use this as your quick reference while building. Just copy/paste from here!

---

## 🏷️ AGENT NAME
```
EquityBridge Grant Advisor
```

---

## 📝 AGENT DESCRIPTION
```
AI-powered grant discovery for health & environmental justice organizations. Guides users through natural conversation to find relevant funding.
```

---

## ⚙️ FUNCTION CONFIGURATION

### Function Name:
```
find_matching_grants
```

### Function Description:
```
Calls the EquityBridge API to find grants matching the organization's profile
```

### API Details:
```
Method: POST
URL: http://localhost:8000/api/match-grants
Header: Content-Type: application/json
```

### Request Body:
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

---

## ✍️ USER INPUTS (Add all 7)

### 1. Organization Name
```
Name: organization_name
Type: Text
Description: The name of the nonprofit organization
Example: "Riverside Community Health Clinic"
```

### 2. Zip Code
```
Name: zip_code
Type: Text
Description: Organization's zip code (5 digits)
Example: "92501"
```

### 3. County
```
Name: county
Type: Text
Description: County where organization is located
Example: "Riverside"
Required: No
```

### 4. Mission
```
Name: mission
Type: Text (Long)
Description: Organization's mission statement
Example: "Providing primary care to low-income families"
```

### 5. Focus Area
```
Name: focus_area
Type: Choice
Options: health, environment, both
Description: Organization's primary focus area
```

### 6. Annual Budget
```
Name: annual_budget
Type: Number
Description: Organization's annual budget in dollars
Example: 250000
```

### 7. Staff Size
```
Name: staff_size
Type: Choice
Options: 1-5, 6-20, 21-50, 50+
Description: Number of staff members
```

---

## 💬 CONVERSATION NODE MESSAGES

### Node 1: Greeting
```
Hello! I'm EquityBridge, your AI grant advisor. 

I help health and environmental justice organizations in California find relevant grant funding opportunities.

Tell me about your organization - what's your mission and what kind of work do you do?
```

### Node 2: After Mission (Extract focus)
```
Thank you for sharing about your important work! I can see you're focused on [focus area]. 

Where is your organization based? Please share your zip code or city/county.
```

### Node 3: After Location
```
Got it, [location]! 

What's your organization's approximate annual budget? Just give me a ballpark figure.
```

### Node 4: After Budget
```
Perfect! Last question: How many people work with your organization? Just a rough count is fine.
```

### Node 5: Confirmation
```
Excellent! Let me make sure I have everything:

Organization: [organization_name]
Location: [zip_code]
Focus: [focus_area]
Budget: $[annual_budget]
Staff: [staff_size]

Does this look correct?
```

### Node 6: Before API Call
```
Perfect! Let me search for grants that match your organization...
```

### Node 7: Results (adjust syntax to Mind Studio's format)
```
Great news! I found [matches_found] grants that match your organization.

Here are your top matches:

[Loop through first 3 grants:]
🎯 **[grant.title]** ([grant.match_score]% match)

**Funder:** [grant.funder]
**Amount:** [grant.amount]
**Deadline:** [grant.deadline]

**Why this matches:** [grant.match_reason]

**Eligibility:** [grant.eligibility]

---

Would you like more details on any of these grants, or help understanding how to apply?
```

### Node 8: Closing
```
I'm glad I could help you find grant opportunities! 

Remember:
- Review deadlines carefully
- Read all eligibility requirements
- Don't hesitate to reach out to funders with questions

Good luck with your applications! Your work makes a real difference in the community. 💚
```

---

## 🧪 TEST SCRIPT

**Use this to test your agent:**

```
You: Hi
Agent: [Should greet and ask about mission]

You: We're a community health clinic in Riverside providing primary care to low-income families
Agent: [Should ask about location]

You: 92501
Agent: [Should ask about budget]

You: $250,000
Agent: [Should ask about staff]

You: 8 staff members
Agent: [Should confirm details]

You: Yes that's correct
Agent: [Should call API and show grants with match scores]
```

**Expected result:** 5 grants with scores around 80-95%

---

## 🎯 QUICK WORKFLOW STRUCTURE

```
1. Greeting Message
   ↓
2. Extract Mission & Focus
   ↓
3. Extract Location (zip code)
   ↓
4. Extract Budget
   ↓
5. Extract Staff Size & Org Name
   ↓
6. Confirm Details
   ↓ (if yes)
7. Call API Function (find_matching_grants)
   ↓
8. Display Results
   ↓
9. Follow-up Questions
   ↓
10. Closing
```

---

## ⚠️ IMPORTANT NOTES

1. **API URL:** Currently `http://localhost:8000/api/match-grants`
   - After backend is deployed, Evren will give you the live URL
   - You'll need to update the function with the new URL

2. **Testing:** Make sure Evren has the backend running before testing
   - Ask him to run: `START_BACKEND_NOW.bat`

3. **Syntax:** The exact templating syntax (like `{{variable}}` or `[variable]`) depends on Mind Studio
   - Use whatever Mind Studio's documentation shows
   - The logic is the same, just the syntax might differ

4. **Save Often:** Mind Studio should auto-save, but click save periodically

---

## 📞 WHEN TO ASK FOR HELP

**Ask Evren/team if:**
- Backend API isn't responding during tests
- You need the deployed URL (after Railway deployment)
- You're not sure what format the API returns

**Use Mind Studio resources if:**
- You need help with the visual workflow builder
- You're stuck on syntax or configuration
- You want to see examples

---

## ✅ DONE CHECKLIST

Before saying you're done:

- [ ] Agent renamed
- [ ] Function created with API call
- [ ] All 7 user inputs configured
- [ ] Workflow built with ~9-10 nodes
- [ ] Test conversation works end-to-end
- [ ] API call succeeds and returns grants
- [ ] Results display with match scores
- [ ] Agent published
- [ ] Embed code copied and shared with team

---

**Good luck! You've got this!** 🚀

This is the core feature that makes EquityBridge special - the conversational AI that helps small nonprofits find funding without needing to navigate complex databases.
