# 🤖 BUILD CONVERSATIONAL CHAT (15 MIN)

## PASTE THIS IN CURSOR:

```
Build a simple conversational chat interface that replaces Mind Studio.

REQUIREMENTS:
1. Create chat UI with bot/user messages
2. Implement conversation flow from Samantha guide
3. Collect org data through questions
4. Call backend API with collected data
5. Display grant results in chat

FILES TO CREATE:
- frontend/chat.html (new chat page OR replace Mind Studio section)
- frontend/chat.js (conversation logic)
- frontend/chat.css (styling)

CONVERSATION FLOW (from Samantha guide):
Step 1: Greeting
Bot: "Hello! I'm EquityBridge, your AI grant advisor. I help health and environmental justice organizations in California find relevant grant funding opportunities. Tell me about your organization - what's your mission and what kind of work do you do?"

Step 2: Extract Mission & Focus
- User describes mission
- Detect focus area:
  * "health" if mentions: health, medical, clinic, wellness, maternal, community health
  * "environment" if mentions: environmental, conservation, air quality, water, climate, sustainability
  * "both" if mentions aspects of both
- Store mission text
Bot: "Thank you for sharing about your important work! I can see you're focused on [health/environment/both]. Where is your organization based? Please share your zip code or city/county."

Step 3: Extract Location
- Extract 5-digit zip code from response
- If no zip found, ask again
Bot: "Got it, [zip]! What's your organization's approximate annual budget? Just give me a ballpark figure."

Step 4: Extract Budget
- Parse budget from text:
  * "$250,000" → 250000
  * "250K" or "250k" → 250000
  * "quarter million" → 250000
  * Extract first number if unclear
Bot: "Perfect! Last question: How many people work with your organization? Just a rough count is fine."

Step 5: Extract Staff Size
- Categorize based on number:
  * 1-5 → "1-5"
  * 6-20 → "6-20"
  * 21-50 → "21-50"
  * 50+ → "50+"
Bot: "Excellent! Let me make sure I have everything:
Organization: [extracted from mission]
Location: [zip]
Focus: [health/environment/both]
Budget: $[budget]
Staff: [staff_size]
Does this look correct? (yes/no)"

Step 6: Confirmation
If user says "yes" or confirms:
Bot: "Perfect! Let me search for grants that match your organization... 🔍"
[Show loading spinner]
[Call API]

If user says "no":
Bot: "No problem! What would you like to correct? Just tell me what needs to be changed."

Step 7: Present Results
After API call:
Bot: "Great news! I found [count] grants that match your organization. Here are your top matches:"
[For each grant:]
"🎯 **[title]** ([match_score]% match)
**Funder:** [funder]
**Amount:** [amount]
**Deadline:** [deadline]
**Why this matches:** [match_reason]
**Eligibility:** [eligibility]
---"

TECHNICAL IMPLEMENTATION:

```javascript
// chat.js structure
const conversationState = {
  step: 0,
  data: {
    name: '',
    mission: '',
    focus_area: '',
    zip_code: '',
    annual_budget: 0,
    staff_size: ''
  }
};

const conversation = [
  {
    step: 0,
    botMessage: "Hello! I'm EquityBridge, your AI grant advisor...",
    handler: extractMission
  },
  {
    step: 1,
    handler: extractLocation
  },
  // ... etc
];

function extractMission(userInput) {
  // Keyword matching for focus area
  const text = userInput.toLowerCase();
  
  const healthKeywords = ['health', 'medical', 'clinic', 'wellness', 'maternal', 'community health', 'healthcare'];
  const envKeywords = ['environment', 'conservation', 'air quality', 'water', 'climate', 'sustainability', 'green'];
  
  const hasHealth = healthKeywords.some(kw => text.includes(kw));
  const hasEnv = envKeywords.some(kw => text.includes(kw));
  
  if (hasHealth && hasEnv) {
    conversationState.data.focus_area = 'both';
  } else if (hasHealth) {
    conversationState.data.focus_area = 'health';
  } else if (hasEnv) {
    conversationState.data.focus_area = 'environment';
  } else {
    conversationState.data.focus_area = 'health'; // default
  }
  
  conversationState.data.mission = userInput;
  
  return `Thank you for sharing about your important work! I can see you're focused on ${conversationState.data.focus_area}. Where is your organization based? Please share your zip code or city/county.`;
}

function extractLocation(userInput) {
  const zipMatch = userInput.match(/\b\d{5}\b/);
  if (zipMatch) {
    conversationState.data.zip_code = zipMatch[0];
    return `Got it, ${zipMatch[0]}! What's your organization's approximate annual budget? Just give me a ballpark figure.`;
  } else {
    return "I need your 5-digit zip code. Could you share that?";
  }
}

function extractBudget(userInput) {
  // Parse various formats
  let budget = 0;
  
  // Remove $ and commas
  let cleaned = userInput.replace(/[$,]/g, '');
  
  // Handle "K" for thousands
  if (cleaned.toLowerCase().includes('k')) {
    const num = parseFloat(cleaned);
    budget = num * 1000;
  }
  // Handle "million"
  else if (cleaned.toLowerCase().includes('million')) {
    const num = parseFloat(cleaned);
    budget = num * 1000000;
  }
  // Extract first number
  else {
    const numMatch = cleaned.match(/\d+/);
    if (numMatch) {
      budget = parseInt(numMatch[0]);
    }
  }
  
  conversationState.data.annual_budget = budget;
  return "Perfect! Last question: How many people work with your organization? Just a rough count is fine.";
}

function extractStaffSize(userInput) {
  const num = parseInt(userInput);
  
  if (num <= 5) {
    conversationState.data.staff_size = '1-5';
  } else if (num <= 20) {
    conversationState.data.staff_size = '6-20';
  } else if (num <= 50) {
    conversationState.data.staff_size = '21-50';
  } else {
    conversationState.data.staff_size = '50+';
  }
  
  return `Excellent! Let me make sure I have everything:

Organization: ${conversationState.data.name || 'Your organization'}
Location: ${conversationState.data.zip_code}
Focus: ${conversationState.data.focus_area}
Budget: $${conversationState.data.annual_budget.toLocaleString()}
Staff: ${conversationState.data.staff_size}

Does this look correct? (yes/no)`;
}

async function callGrantAPI() {
  const response = await fetch('https://ideal-flow-production-2795.up.railway.app/api/match-grants', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      profile: conversationState.data
    })
  });
  
  const data = await response.json();
  return data.grants;
}
```

HTML STRUCTURE:
```html
<div id="chat-container">
  <div id="chat-messages"></div>
  <div id="chat-input-area">
    <input type="text" id="chat-input" placeholder="Type your answer...">
    <button id="chat-send">Send</button>
  </div>
</div>
```

CSS STYLING:
```css
#chat-container {
  max-width: 800px;
  margin: 2rem auto;
  border: 1px solid #ddd;
  border-radius: 12px;
  overflow: hidden;
  height: 600px;
  display: flex;
  flex-direction: column;
}

#chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 1.5rem;
  background: #f8f9fa;
}

.message {
  margin-bottom: 1rem;
  display: flex;
  gap: 0.75rem;
}

.message.bot {
  justify-content: flex-start;
}

.message.user {
  justify-content: flex-end;
}

.message-content {
  max-width: 70%;
  padding: 1rem 1.25rem;
  border-radius: 18px;
  line-height: 1.5;
}

.message.bot .message-content {
  background: white;
  border: 1px solid #e0e0e0;
  color: #2d3748;
}

.message.user .message-content {
  background: #667eea;
  color: white;
}

#chat-input-area {
  padding: 1rem;
  background: white;
  border-top: 1px solid #ddd;
  display: flex;
  gap: 0.75rem;
}

#chat-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 1px solid #ddd;
  border-radius: 24px;
  font-size: 1rem;
}

#chat-send {
  padding: 0.75rem 2rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 24px;
  cursor: pointer;
  font-weight: 600;
}

#chat-send:hover {
  background: #5568d3;
}

.loading {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #667eea;
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 1; }
}
```

INTEGRATION:
Option 1: Replace Mind Studio iframe section in index.html
Option 2: Create standalone chat.html page

Build it now - simple JavaScript, no external dependencies!
```
