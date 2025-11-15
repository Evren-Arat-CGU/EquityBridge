# EquityBridge Logo Usage Guide

## Logo Files

**Location:**
- `frontend/equitybridge-logo.png` (18KB PNG)

**Specifications:**
- Format: PNG with transparency
- Colors: Teal (#0891b2) + Gold (#f59e0b)
- Design: Bridge icon with location pin
- Size: Scalable from 32px to 500px

---

## Usage in Different Contexts

### 1. Website Header (Already Implemented)
```html
<img src="equitybridge-logo.png" alt="EquityBridge Logo" class="logo">
```

CSS:
```css
.logo {
    width: 80px;
    height: 80px;
    object-fit: contain;
}
```

### 2. Mind Studio Chat Widget
- Upload logo in Mind Studio settings
- Recommended size: 60x60px
- Use as avatar or header icon

### 3. ArcGIS StoryMap
- Upload as header image
- Recommended: 200x200px for story header
- Or 400x400px for full-width hero

### 4. GitHub Repository
- Set as repository social preview
- Go to: Settings → Options → Social preview
- Upload the logo

### 5. Favicon (Browser Tab Icon)
To create favicon:
1. Resize logo to 32x32px
2. Convert to .ico format
3. Add to HTML: `<link rel="icon" href="favicon.ico">`

---

## Brand Colors

**Primary Teal:** #0891b2  
**Accent Gold:** #f59e0b  
**Use for:** Backgrounds, buttons, highlights

---

## Quick Reference

**For presentations:** Use full logo with "Grants Adviser" tagline  
**For small spaces:** Icon only (just the bridge)  
**For dark backgrounds:** Logo works well (has good contrast)  
**For light backgrounds:** Logo works perfectly (primary design)

---

## File Locations in Project

```
CGU_HACKATHON_FRESH_BUILD/
├── frontend/
│   ├── equitybridge-logo.png  ← Main logo file
│   ├── index.html             ← Logo already integrated
│   └── styles.css             ← Logo styles defined
```

---

**Logo is ready to use throughout the project!** ✅
