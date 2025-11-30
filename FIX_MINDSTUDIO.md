# 🔧 MIND STUDIO IFRAME FIX

## Problem
Mind Studio blocks iframe embedding (security policy). Chat won't load.

## Quick Fix (2 minutes)

### Replace the iframe with a button that opens Mind Studio in new window:

**In `frontend/index.html`, find this section (around line 54):**

```html
<div id="mindstudio-embed" class="mindstudio-container">
    <!-- Mind Studio AI Agent Embed -->
    <iframe 
        src="https://mindstudio.ai/embed/2701765f-ff7f-4445-b6c8-dd2f96b1b872" 
        width="100%" 
        height="600" 
        frameborder="0"
        title="Grant Advisor AI Chat"
        allow="microphone; camera">
    </iframe>
</div>
```

**Replace it with:**

```html
<div id="mindstudio-embed" class="mindstudio-container">
    <div class="mindstudio-button-container">
        <p class="intro-text">Click below to open our AI Grant Advisor in a new window:</p>
        <a 
            href="https://mindstudio.ai/embed/2701765f-ff7f-4445-b6c8-dd2f96b1b872" 
            target="_blank"
            rel="noopener noreferrer"
            class="cta-button mindstudio-launch"
            role="button">
            🤖 Launch AI Grant Advisor
        </a>
        <p class="helper-text">The AI advisor will open in a new tab. Have a conversation about your organization to find matching grants!</p>
    </div>
</div>
```

**In `frontend/styles.css`, add this styling:**

```css
.mindstudio-button-container {
    text-align: center;
    padding: 3rem 2rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 12px;
    color: white;
}

.mindstudio-button-container .intro-text {
    color: white;
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
}

.mindstudio-launch {
    display: inline-block;
    background: white;
    color: #667eea;
    padding: 1rem 2.5rem;
    border-radius: 50px;
    font-size: 1.2rem;
    font-weight: bold;
    text-decoration: none;
    transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.mindstudio-launch:hover,
.mindstudio-launch:focus {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    text-decoration: none;
}

.helper-text {
    color: rgba(255,255,255,0.9);
    margin-top: 1rem;
    font-size: 0.95rem;
}
```

## Redeploy (1 minute)

```bash
cd frontend
vercel --prod
```

Done! Now the AI chat opens in a new window instead of trying to embed.

## Alternative: Get Proper Embed Code

Ask Samantha to get the **actual embed code** from Mind Studio:
1. In Mind Studio, click "Share" or "Publish"
2. Look for "Embed Code" option
3. Copy the full HTML snippet
4. Use that instead of the iframe we guessed

The proper embed code might work where our iframe failed.
