# 🤖 INTEGRATE MIND STUDIO - QUICK GUIDE

**Status:** Ready to integrate  
**Backend URL:** `https://ideal-flow-production-2795.up.railway.app`  
**Frontend URL:** `https://equity-bridge.vercel.app/`

---

## 📋 WHAT YOU NEED FROM SAMANTHA

**Ask Samantha for:**
1. **Mind Studio Embed Code** (iframe or script tag)
2. **Agent URL** (for reference)

**Example of what you might get:**
```html
<iframe 
  src="https://mindstudio.ai/embed/your-agent-id" 
  width="100%" 
  height="600"
  frameborder="0">
</iframe>
```

**OR a script tag:**
```html
<script src="https://mindstudio.ai/embed/your-agent-id.js"></script>
```

---

## 🔧 HOW TO INTEGRATE

### Step 1: Get the Embed Code from Samantha

Ask her: "Can you share the Mind Studio embed code? I need the iframe or script tag."

---

### Step 2: Add to Frontend

**File to edit:** `frontend/index.html`

**Find this section (around line 41-47):**
```html
<div id="mindstudio-embed" class="mindstudio-container">
    <!-- Mind Studio embed will be inserted here by Samantha -->
    <div class="placeholder-message">
        <p>Mind Studio AI agent will be embedded here.</p>
        <p class="note">Samantha is setting this up now!</p>
    </div>
</div>
```

**Replace with:**
```html
<div id="mindstudio-embed" class="mindstudio-container">
    <!-- Mind Studio embed code from Samantha -->
    [PASTE SAMANTHA'S EMBED CODE HERE]
</div>
```

---

### Step 3: Update Backend URL in Mind Studio

**Tell Samantha:**
- Backend URL: `https://ideal-flow-production-2795.up.railway.app`
- API Endpoint: `https://ideal-flow-production-2795.up.railway.app/api/match-grants`
- She needs to update her Mind Studio agent to use this URL instead of localhost

---

### Step 4: Test Locally

1. Open `frontend/index.html` in your browser
2. Click "Chat with AI" tab
3. Verify Mind Studio widget appears
4. Test a conversation

---

### Step 5: Deploy to Vercel

1. Commit the changes:
   ```bash
   git add frontend/index.html
   git commit -m "Add Mind Studio embed code"
   git push
   ```

2. Vercel will auto-deploy (1-2 minutes)

3. Test on live site: `https://equity-bridge.vercel.app/`

---

## 🎯 QUICK INTEGRATION (If you have the code)

**Just replace lines 41-47 in `frontend/index.html` with:**

```html
<div id="mindstudio-embed" class="mindstudio-container">
    <!-- Replace this comment with Samantha's embed code -->
    [PASTE CODE HERE]
</div>
```

**Then commit and push!**

---

## ✅ CHECKLIST

- [ ] Get embed code from Samantha
- [ ] Add embed code to `frontend/index.html` (replace placeholder)
- [ ] Tell Samantha to update Mind Studio with Railway backend URL
- [ ] Test locally
- [ ] Commit and push
- [ ] Test on live site

---

**Once you have the embed code from Samantha, paste it in and we'll deploy!** 🚀

