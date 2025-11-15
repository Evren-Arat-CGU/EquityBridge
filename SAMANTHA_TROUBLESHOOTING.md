# 🔧 MIND STUDIO TROUBLESHOOTING GUIDE

**For: Samantha**  
**Common Issues & Quick Fixes**

---

## 🚨 PROBLEM: Agent doesn't extract information

### Symptoms:
- User provides info but agent doesn't remember it
- Variables stay empty
- Agent asks for same info twice

### Solutions:

**1. Check User Input Configuration**
- Go to "User Inputs" in sidebar
- Make sure all 7 inputs are created
- Verify names match exactly (organization_name, zip_code, etc.)

**2. Check Node Configuration**
- Click on the node that should extract the info
- Look for "Extract" or "Save to variable" settings
- Make sure it's saving to the correct user input variable

**3. Add Explicit Instructions**
- In the node's AI instructions, add:
  ```
  Extract the [information] from the user's response.
  Save it to the variable [variable_name].
  Be flexible with phrasing.
  ```

---

## 🚨 PROBLEM: API call fails

### Symptoms:
- Agent tries to search but shows error
- "Failed to call function" message
- Results don't appear

### Solutions:

**1. Check if Backend is Running**
- Ask Evren: "Is the backend running?"
- He should have a window open with green text saying:
  ```
  Uvicorn running on http://127.0.0.1:8000
  ```
- If not, he needs to run: `START_BACKEND_NOW.bat`

**2. Check Function URL**
- Go to "Functions" → "find_matching_grants"
- URL should be: `http://localhost:8000/api/match-grants`
- Make sure there's no extra spaces or typos

**3. Check Parameter Mapping**
- In the function configuration, verify parameters are mapped:
  ```
  name → {{organization_name}}
  zip_code → {{zip_code}}
  mission → {{mission}}
  focus_area → {{focus_area}}
  annual_budget → {{annual_budget}}
  staff_size → {{staff_size}}
  ```

**4. Check Request Body**
- Should look exactly like:
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
- Note: annual_budget has NO quotes around `{{annual_budget}}` because it's a number

---

## 🚨 PROBLEM: Results don't display properly

### Symptoms:
- API call works but nothing shows
- Grants appear but formatting is broken
- Shows raw JSON or gibberish

### Solutions:

**1. Check Results Node Configuration**
- Make sure the node is set to display the API response
- Check if it's accessing the right fields

**2. Verify Response Format**
- The API returns:
  ```json
  {
    "organization": "...",
    "matches_found": 5,
    "grants": [ ... ]
  }
  ```
- Make sure you're accessing `grants` array correctly

**3. Use Simple Format First**
- Start with basic text:
  ```
  I found {{matches_found}} grants!
  
  First grant: {{grants[0].title}}
  ```
- Once that works, add more formatting

**4. Check Templating Syntax**
- Mind Studio might use different syntax than `{{variable}}`
- Check their docs for correct format
- Common alternatives:
  - `[variable]`
  - `${variable}`
  - `{variable}`

---

## 🚨 PROBLEM: Conversation gets stuck in loop

### Symptoms:
- Agent keeps asking same question
- Never progresses to next step
- Circles back to earlier questions

### Solutions:

**1. Check Node Connections**
- Look at the workflow canvas
- Make sure each node has a clear arrow to the next
- No loops back unless intentional

**2. Check Conditional Logic**
- If you have "if/else" branches, verify conditions are correct
- Make sure there's a path forward for all possible answers

**3. Add Exit Conditions**
- In confirmation nodes, add both paths:
  - YES path → Continue to API call
  - NO path → Ask what to change → Return to specific question

---

## 🚨 PROBLEM: Agent misunderstands user input

### Symptoms:
- User says "$250,000" but agent extracts "250" 
- User says "Riverside" but agent doesn't extract location
- Focus area is wrong

### Solutions:

**1. Add More Examples in AI Instructions**
```
Extract the budget from user's response. Handle these formats:
- "$250,000" → 250000
- "250K" → 250000  
- "about a quarter million" → 250000
- "two hundred fifty thousand" → 250000

If they give a range like "$200K-$300K", use the midpoint: 250000
```

**2. Add Validation**
- After extracting, have agent confirm:
  ```
  Just to confirm, your budget is about $250,000 - is that right?
  ```

**3. Be Flexible with Focus Area**
```
Determine focus area from their description:
- "health" if they mention: medical, clinic, health care, wellness, maternal health, community health, mental health
- "environment" if they mention: environmental, conservation, air quality, water, climate, pollution, sustainability
- "both" if they clearly work on both health and environment together
```

---

## 🚨 PROBLEM: Can't find where to add nodes

### Symptoms:
- Workflow canvas is blank or has few nodes
- Can't figure out how to add conversation steps

### Solutions:

**1. Look for "+" Button**
- Usually in toolbar or on the canvas
- Might say "Add Node", "Add Step", "Add Message"

**2. Right-click on Canvas**
- Some interfaces use right-click to add nodes

**3. Check Toolbar**
- Look for icons like:
  - 💬 Message/Response
  - ❓ Question
  - ⚡ Action/Function
  - 🔀 Condition/Branch

**4. Use Drag-and-Drop**
- Some have a panel with node types you drag onto canvas

---

## 🚨 PROBLEM: Test preview doesn't work

### Symptoms:
- Click "Preview" but nothing happens
- Chat window appears but won't respond
- Can't type in test chat

### Solutions:

**1. Check if Agent is Saved**
- Make sure you saved your workflow
- Look for "Unsaved changes" warning
- Save before testing

**2. Check if There's a Start Node**
- Workflow needs a clear entry point
- Make sure first node is connected

**3. Refresh Preview**
- Close preview window
- Save workflow
- Open preview again

**4. Check Browser Console**
- Press F12 to open developer tools
- Look for error messages
- Share them with team if you see red errors

---

## 🚨 PROBLEM: Can't publish agent

### Symptoms:
- "Publish" button is grayed out
- Errors when trying to publish
- Says "Not ready to publish"

### Solutions:

**1. Check for Incomplete Nodes**
- All nodes need to be configured
- Look for red warning icons on nodes
- Fill in any missing required fields

**2. Test First**
- Run through test conversation successfully
- Make sure it completes without errors
- Then try publishing

**3. Check Required Settings**
- Some platforms require:
  - Agent name (not "Untitled")
  - Agent description
  - At least one complete workflow path

---

## 🚨 PROBLEM: Variables aren't being passed to function

### Symptoms:
- API call happens but returns errors
- Backend says "missing required field"
- Some variables are null/empty

### Solutions:

**1. Check Variable Names Match**
- User Input: `organization_name`
- Function Parameter: `name`
- Make sure mapping is: `name` → `{{organization_name}}`

**2. Verify All Required Variables Collected**
- Before calling function, confirm you've collected:
  - ✅ organization_name
  - ✅ zip_code
  - ✅ mission
  - ✅ focus_area
  - ✅ annual_budget
  - ✅ staff_size

**3. Add Debug Message**
- Before API call, add a message showing variables:
  ```
  About to search with:
  Name: {{organization_name}}
  Zip: {{zip_code}}
  Focus: {{focus_area}}
  Budget: {{annual_budget}}
  Staff: {{staff_size}}
  ```
- This helps you see what's actually being collected

---

## 💡 GENERAL TIPS

### If You're Really Stuck:

1. **Start Over with One Node**
   - Create just the greeting
   - Test it
   - Add one node at a time
   - Test after each addition

2. **Use Simple Version First**
   - Get basic flow working
   - Add complexity later
   - Don't try to build everything perfectly first time

3. **Check Mind Studio Documentation**
   - They should have tutorials
   - Look for "Getting Started" guides
   - Community forum might have similar issues

4. **Ask the Team**
   - Evren can help with backend/API issues
   - Mind Studio judges might have guidance
   - Share screenshots of errors

---

## 📋 QUICK DIAGNOSTIC CHECKLIST

When something isn't working, check these in order:

- [ ] Is backend running? (Ask Evren)
- [ ] Are all user inputs defined?
- [ ] Are nodes connected in correct order?
- [ ] Did you save your changes?
- [ ] Are variable names spelled correctly?
- [ ] Is the function URL correct?
- [ ] Have you tested with preview?
- [ ] Are all required fields filled in function config?

---

## 🆘 EMERGENCY RESET

If things are really broken and you need to start over:

1. **Export Your Work**
   - Look for "Export" or "Download" option
   - Save a backup

2. **Create New Agent**
   - Start fresh with new agent
   - Copy/paste working parts from old one

3. **Use Templates**
   - Mind Studio might have conversation templates
   - Start from template and modify

---

## 📞 WHO TO ASK

**Evren/Team for:**
- Backend not running
- API errors
- What data the API returns
- Deployment questions

**Mind Studio Resources for:**
- How to use the workflow builder
- Syntax for templates
- Node configuration
- Platform-specific features

**Judges for:**
- Mind Studio account issues
- Platform limits or features
- Best practices

---

## ✅ WORKING CORRECTLY LOOKS LIKE:

You'll know it's working when:

1. ✅ Agent asks questions one at a time
2. ✅ User can answer naturally (not forced format)
3. ✅ Agent confirms it understood correctly
4. ✅ API call happens smoothly
5. ✅ Grants appear with scores 0-100%
6. ✅ Match reasons make sense
7. ✅ Conversation feels natural

---

**You've got this!** Most issues are simple configuration problems with simple fixes. Work methodically, test frequently, and ask for help when stuck. 🚀
