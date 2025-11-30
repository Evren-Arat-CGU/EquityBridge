# 🤖 BUILD SIMPLE CONVERSATIONAL CHAT (20 MIN)

## PASTE THIS IN CURSOR:

```
URGENT - Build simple conversational grant finder (20 min deadline)

Create a rule-based chat interface that collects org info through guided conversation.

REQUIREMENTS:
1. Chat UI with messages (bot + user)
2. Input field for user responses
3. Conversation flow (7 steps):
   - Ask name
   - Ask zip code
   - Ask mission
   - Ask focus (health/environment/both)
   - Ask budget
   - Ask staff size
   - Call backend API with collected data
   - Display grant results in chat

FILES TO CREATE/MODIFY:
- frontend/chat.js (new) - Conversation logic
- frontend/chat.css (new) - Chat styling
- frontend/index.html - Replace Mind Studio section with chat div

CONVERSATION FLOW LOGIC:
```javascript
const conversation = [
  {
    step: 0,
    bot: "Hi! I'm EquityBridge, your grant advisor. What's your organization's name?",
    field: 'name',
    validate: (val) => val.length > 0
  },
  {
    step: 1,
    bot: "Great! What's your zip code?",
    field: 'zip_code',
    validate: (val) => /^\d{5}$/.test(val)
  },
  {
    step: 2,
    bot: "Tell me about your organization's mission.",
    field: 'mission',
    validate: (val) => val.length > 10
  },
  {
    step: 3,
    bot: "What's your main focus area?\n• Type 'health' for health services\n• Type 'environment' for environmental work\n• Type 'both' for both areas",
    field: 'focus_area',
    validate: (val) => ['health', 'environment', 'both'].includes(val.toLowerCase())
  },
  {
    step: 4,
    bot: "What's your annual budget? (just the number, like 250000)",
    field: 'annual_budget',
    validate: (val) => !isNaN(val) && val > 0,
    transform: (val) => parseInt(val)
  },
  {
    step: 5,
    bot: "How many staff members do you have?\n• Type '1-5', '6-20', '21-50', or '50+'",
    field: 'staff_size',
    validate: (val) => ['1-5', '6-20', '21-50', '50+'].includes(val)
  }
];
```

CHAT HTML STRUCTURE:
```html
<div id="chat-container">
  <div id="chat-messages"></div>
  <div id="chat-input-container">
    <input type="text" id="chat-input" placeholder="Type your answer...">
    <button id="chat-send">Send</button>
  </div>
</div>
```

STYLING (chat.css):
- Chat messages container with scroll
- Bot messages (left, gray background)
- User messages (right, blue background)
- Input at bottom (sticky)
- Clean, accessible design

FEATURES:
- Bot asks questions one at a time
- User types answer
- Validates input before moving to next question
- Shows error if invalid ("Please enter a valid zip code")
- After all questions: calls backend API
- Displays grant results in chat format
- Accessible (keyboard nav, ARIA labels)

BACKEND INTEGRATION:
After final question, call:
POST https://ideal-flow-production-2795.up.railway.app/api/match-grants
Body: { profile: { collected_data } }

Display results as chat messages:
"I found 5 grants that match your organization! Here are the top matches:

🎯 CDC Healthy Communities Program (95% match)
Funder: CDC
Amount: $50,000 - $250,000
Deadline: June 30, 2025
[View Details Button]

[Show more grants...]"

REPLACE Mind Studio iframe section in index.html with this chat div.

Build it now - 20 minutes!
```
