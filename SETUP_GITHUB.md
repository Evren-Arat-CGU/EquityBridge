# 🔗 CONNECT GITHUB TO PROJECT

**Quick setup guide to connect your GitHub account to EquityBridge**

---

## 🚀 QUICK SETUP (5 minutes)

### Step 1: Create GitHub Repository

1. Go to: https://github.com/new
2. Repository name: `equitybridge` (or your choice)
3. Description: "Grant discovery platform for health & environmental equity - CGU Hackathon 2025"
4. Visibility: **Public** (for hackathon) or Private
5. **DO NOT** initialize with README, .gitignore, or license (we have these)
6. Click "Create repository"

### Step 2: Connect Local Project

**Option A: If repository doesn't exist yet (First time)**

```bash
cd CGU_HACKATHON_FRESH_BUILD

# Initialize git (if not already)
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit: EquityBridge hackathon project"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/equitybridge.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Option B: If repository already exists**

```bash
cd CGU_HACKATHON_FRESH_BUILD

# Check current remote
git remote -v

# Update remote URL (replace YOUR_USERNAME)
git remote set-url origin https://github.com/YOUR_USERNAME/equitybridge.git

# Push
git push -u origin main
```

---

## 📋 DETAILED STEPS

### 1. Check Git Status

```bash
cd CGU_HACKATHON_FRESH_BUILD
git status
```

### 2. Initialize Repository (if needed)

```bash
git init
```

### 3. Configure Git (if first time)

```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### 4. Add Files

```bash
# Add all files
git add .

# Or add specific files
git add backend/ frontend/ docs/ *.md
```

### 5. Commit

```bash
git commit -m "Initial commit: EquityBridge hackathon project

- Backend API with grant matching
- Frontend with accessible UI
- Database with 21 grants
- Deployment configs ready
- Documentation complete"
```

### 6. Connect to GitHub

```bash
# Add remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Verify remote
git remote -v
```

### 7. Push to GitHub

```bash
# Set main branch
git branch -M main

# Push
git push -u origin main
```

---

## 🔐 AUTHENTICATION

### Option 1: Personal Access Token (Recommended)

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Name: "EquityBridge Hackathon"
4. Expiration: 90 days (or your choice)
5. Scopes: Check `repo` (full control)
6. Generate token
7. **Copy token** (you won't see it again!)

When pushing, use token as password:
```bash
git push -u origin main
# Username: YOUR_USERNAME
# Password: [paste token]
```

### Option 2: GitHub CLI (Easier)

```bash
# Install GitHub CLI
winget install GitHub.cli

# Login
gh auth login

# Then push normally
git push -u origin main
```

### Option 3: SSH (Advanced)

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add to GitHub: https://github.com/settings/keys
# Copy public key: cat ~/.ssh/id_ed25519.pub

# Use SSH URL
git remote set-url origin git@github.com:YOUR_USERNAME/REPO_NAME.git
```

---

## ✅ VERIFY CONNECTION

```bash
# Check remote
git remote -v

# Should show:
# origin  https://github.com/YOUR_USERNAME/REPO_NAME.git (fetch)
# origin  https://github.com/YOUR_USERNAME/REPO_NAME.git (push)

# Test connection
git fetch origin
```

---

## 📝 .GITIGNORE

Already created! It excludes:
- `__pycache__/`
- `*.db` (database files)
- `.env` (environment variables)
- `node_modules/`
- IDE files

**Note:** Database file is excluded. You may want to:
- Keep it local only, OR
- Add a sample database to repo, OR
- Document how to create it

---

## 🚨 TROUBLESHOOTING

### "Repository not found"
- Check repository name and username
- Verify repository exists on GitHub
- Check you have access

### "Authentication failed"
- Use Personal Access Token instead of password
- Or use GitHub CLI: `gh auth login`

### "Permission denied"
- Check SSH key is added to GitHub
- Or use HTTPS with token

### "Large files"
- Database file might be large
- Consider adding to .gitignore
- Or use Git LFS for large files

---

## 🎯 QUICK COMMANDS REFERENCE

```bash
# Status
git status

# Add files
git add .

# Commit
git commit -m "Your message"

# Push
git push

# Pull
git pull

# Check remote
git remote -v

# View commits
git log --oneline
```

---

## 📦 WHAT TO COMMIT

**Include:**
- ✅ All source code (backend/, frontend/)
- ✅ Configuration files (Procfile, railway.json, vercel.json)
- ✅ Documentation (*.md files)
- ✅ Scripts (*.bat files)
- ✅ .gitignore

**Exclude (already in .gitignore):**
- ❌ Database files (*.db)
- ❌ Environment variables (.env)
- ❌ Python cache (__pycache__/)
- ❌ Node modules (if any)

---

**Ready to connect! Follow the steps above.** 🚀

