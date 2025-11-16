# 🗺️ ARCGIS STORYMAP CREATION GUIDE

**Time Remaining:** ~2 hours until demo  
**Status:** ⏳ TO DO

---

## 🎯 WHAT IS A STORYMAP?

An ArcGIS StoryMap is an interactive presentation that tells your project's story using maps, images, and text. It's perfect for the hackathon demo!

---

## 📋 STORYMAP STRUCTURE (4 SECTIONS)

### Section 1: The Problem
- **Title:** "The Grant Discovery Challenge"
- **Content:**
  - Health and environmental justice organizations struggle to find relevant grants
  - Funding deserts exist in underserved communities
  - Time-consuming manual search process
- **Visual:** Map showing funding distribution (use your LA County map)

### Section 2: The Solution
- **Title:** "EquityBridge: AI-Powered Grant Discovery"
- **Content:**
  - AI chat interface for natural conversation
  - Geographic visualization of grant opportunities
  - Accessible design (WCAG 2.1 AA)
- **Visual:** Screenshot of the app interface

### Section 3: The Demo
- **Title:** "See It In Action"
- **Content:**
  - Embedded live demo of the application
  - Walkthrough of a grant search
  - Show matching results and map
- **Visual:** Embedded iframe of `https://equity-bridge.vercel.app/`

### Section 4: The Impact
- **Title:** "Empowering Communities"
- **Content:**
  - How EquityBridge helps organizations find funding
  - Real-world use cases
  - Future potential
- **Visual:** Impact statistics or testimonials

---

## 🚀 HOW TO CREATE THE STORYMAP

### Step 1: Access ArcGIS StoryMaps

1. Go to: https://storymaps.arcgis.com/
2. Sign in with your ArcGIS account
3. Click **"Create a new story"**

### Step 2: Choose Template

- Select **"Sidecar"** or **"Map Tour"** template
- Or use **"Cascade"** for a scrolling experience

### Step 3: Add Content

**For each section:**

1. Click **"Add"** → **"Text"** or **"Image"**
2. Add your content
3. For the demo section, click **"Add"** → **"Embed"**
   - Paste: `<iframe src="https://equity-bridge.vercel.app/" width="100%" height="800" frameborder="0"></iframe>`

### Step 4: Add Your Map

1. Click **"Add"** → **"Map"**
2. Choose **"Create a new map"** or **"Use existing map"**
3. If using existing:
   - Search for: "LA County Grant Funding Distribution"
   - Or use your Feature Service URL:
     - `https://services.arcgis.com/hVnyNvwbpFFPDV5j/arcgis/rest/services/LA_County_Grant_Funding_Distribution/FeatureServer/0`

### Step 5: Publish

1. Click **"Publish"** (top right)
2. Set visibility to **"Public"** or **"Organization"**
3. Copy the share URL

---

## 📝 QUICK COPY-PASTE CONTENT

### Section 1: The Problem

**Title:** The Grant Discovery Challenge

**Text:**
```
Health and environmental justice organizations face a critical challenge: finding grant funding that matches their mission and needs. 

Traditional grant discovery is:
- Time-consuming manual research
- Overwhelming information overload
- Geographic funding gaps (funding deserts)
- Limited accessibility for smaller organizations

This map shows the distribution of grant funding across Los Angeles County, revealing areas where organizations struggle to access resources.
```

### Section 2: The Solution

**Title:** EquityBridge: AI-Powered Grant Discovery

**Text:**
```
EquityBridge revolutionizes grant discovery with:

🤖 AI-Powered Matching
Natural language conversation with our grant advisor AI

🗺️ Geographic Visualization
See grant opportunities on an interactive map

♿ Accessible Design
WCAG 2.1 AA compliant for all users

⚡ Fast & Free
No sign-up required, instant results
```

### Section 3: The Demo

**Title:** See It In Action

**Text:**
```
Try EquityBridge yourself! Use the embedded application below to:

1. Chat with our AI grant advisor
2. Or fill out the form
3. See matching grants with scores
4. Explore the geographic distribution

[Embedded app will appear here]
```

**Embed Code:**
```html
<iframe 
    src="https://equity-bridge.vercel.app/" 
    width="100%" 
    height="800" 
    frameborder="0"
    title="EquityBridge Live Demo">
</iframe>
```

### Section 4: The Impact

**Title:** Empowering Communities

**Text:**
```
EquityBridge helps organizations:

✅ Find relevant grants faster
✅ Understand funding opportunities geographically
✅ Access resources regardless of technical expertise
✅ Bridge the gap between need and funding

Built for the CGU Hackathon 2025 - Health & Environmental Equity theme.
```

---

## ⚡ QUICK START (15 MINUTES)

1. **Sign in to ArcGIS StoryMaps** (5 min)
2. **Create new story** → Choose template (2 min)
3. **Add 4 sections** with copy-paste content above (5 min)
4. **Embed the live app** in Section 3 (2 min)
5. **Add your LA County map** to Section 1 (1 min)
6. **Publish and share** (1 min)

---

## 🔗 LINKS YOU'LL NEED

- **StoryMaps:** https://storymaps.arcgis.com/
- **Live App:** https://equity-bridge.vercel.app/
- **Backend API:** https://ideal-flow-production-2795.up.railway.app/
- **LA County Map:** https://services.arcgis.com/hVnyNvwbpFFPDV5j/arcgis/rest/services/LA_County_Grant_Funding_Distribution/FeatureServer/0

---

## ✅ CHECKLIST

- [ ] StoryMap created
- [ ] 4 sections added
- [ ] Live app embedded
- [ ] LA County map added
- [ ] Published and shareable
- [ ] URL copied for presentation

---

**Time Estimate:** 15-30 minutes  
**Priority:** HIGH (needed for presentation)

