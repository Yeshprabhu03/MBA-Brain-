# 🌐 Publishing This Vault with Quartz + GitHub Pages

This guide walks you through publishing your MBA Second Brain as a public website using **Quartz 4** and **GitHub Pages** — completely free.

---

## 🔧 One-Time Setup (15 minutes)

### Step 1: Create a GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Name it `mba-brain` (or any name you like)
3. Set to **Public** (required for free GitHub Pages)
4. **Don't** add README or .gitignore (we already have them)
5. Click **Create repository**

### Step 2: Push This Vault to GitHub

In your terminal:
```bash
cd /Users/yeshwanth/MBA

# Add your GitHub repo as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/mba-brain.git

# Push to GitHub
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repo → **Settings** → **Pages**
2. Under "Source", select **GitHub Actions**
3. Save

### Step 4: Update Your Base URL

Edit `quartz.config.ts` and replace:
```ts
baseUrl: "your-github-username.github.io/mba-brain"
```
with your actual GitHub username:
```ts
baseUrl: "YOUR_USERNAME.github.io/mba-brain"
```

Commit and push this change:
```bash
git add quartz.config.ts
git commit -m "✅ Configure Quartz base URL"
git push
```

### Step 5: Watch It Deploy!

- Go to your repo → **Actions** tab
- Watch the "Deploy MBA Brain to GitHub Pages" workflow run
- Takes ~2–3 minutes on first run
- Your site will be live at: `https://YOUR_USERNAME.github.io/mba-brain/`

---

## 🔄 Daily Workflow

Every time you add notes in Obsidian:

```bash
cd /Users/yeshwanth/MBA
git add .
git commit -m "📝 Add notes on [topic]"
git push
```

GitHub Actions automatically rebuilds and redeploys your site within 2 minutes.

---

## 🤖 Optional: Auto-Push Script

Create a script for one-command publishing:

```bash
# Save as /Users/yeshwanth/MBA/publish.sh
#!/bin/bash
cd /Users/yeshwanth/MBA
git add .
git commit -m "📝 Update: $(date '+%Y-%m-%d %H:%M')"
git push
echo "✅ Published! Site rebuilding at GitHub Actions..."
```

Make it executable:
```bash
chmod +x publish.sh
```

Then just run `./publish.sh` whenever you want to publish.

---

## 🎨 Customizing the Site

### Change Colors / Fonts
Edit `quartz.config.ts` — the `theme` section controls all visual settings.

### Add Custom CSS
Create `custom.scss` in your vault root and add styles.

### Change the Homepage
The `00 - Home/🏠 Dashboard.md` file is your site's homepage.

---

## 📖 Quartz Documentation

Full docs at: [quartz.jzhao.xyz](https://quartz.jzhao.xyz)

### Key Features Enabled
- ✅ Full-text search
- ✅ Interactive graph view
- ✅ Wikilink support (`[[Note Name]]`)
- ✅ LaTeX math rendering
- ✅ Table of contents on every page
- ✅ Backlinks panel
- ✅ Dark/light mode toggle
- ✅ RSS feed for new notes
- ✅ Sitemap for SEO
- ✅ Tags and folder browsing

---

## 🌐 What the Published Site Looks Like

```
https://YOUR_USERNAME.github.io/mba-brain/
├── /                      → Dashboard (home)
├── /01-finance/           → Finance folder
├── /tags/finance/         → All finance-tagged notes
├── /graph/                → Interactive knowledge graph
└── /search?q=WACC         → Full-text search
```

---

*Built with [Quartz 4](https://quartz.jzhao.xyz) · Vault maintained with [Obsidian](https://obsidian.md)*
