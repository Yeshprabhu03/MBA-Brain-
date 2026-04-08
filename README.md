# 🎓 MBA Brain — Open Knowledge Vault

> A free, public second brain mapping everything taught at the world's top MBA programs.
> Built with Obsidian. Published with Quartz. Automated with Python + AI.

**🌐 Live Site → [Yeshprabhu03.github.io/MBA-Brain-](https://Yeshprabhu03.github.io/MBA-Brain-/)**
<img width="1024" height="551" alt="image" src="https://github.com/user-attachments/assets/0627a7fe-7071-4bc5-b6d9-8163de40d4d2" />
<img width="1024" height="616" alt="image" src="https://github.com/user-attachments/assets/a5b44d92-5b85-494c-9c9d-bf1344712bfb" />



---

## What This Is

Most MBA knowledge sits locked behind $200K tuition, paywalled case studies, and proprietary course packs. This vault changes that.

**MBA Brain** is a structured, interconnected knowledge graph covering the full curriculum of programs like HBS, Wharton, Booth, Kellogg, and Stanford GSB — broken down into 10 subject areas, 100+ case studies, 180+ framework notes, and a live interactive graph showing how every concept connects.

It is designed to be genuinely useful for:
- Self-learners who want rigorous business education without the debt
- MBA students building a reference system alongside their coursework
- Product managers, consultants, and founders who need sharp mental models fast
- Anyone preparing for case interviews, strategy roles, or executive leadership

---

## The 10 Subject Areas

| # | Subject |
|---|---|
| 01 | 📊 Finance |
| 02 | 🎯 Strategy |
| 03 | 📣 Marketing |
| 04 | ⚙️ Operations |
| 05 | 👥 Organizational Behavior |
| 06 | 📒 Accounting |
| 07 | 📈 Economics |
| 08 | 🚀 Entrepreneurship |
| 09 | 📉 Data & Analytics |
| 10 | ⚖️ Ethics & ESG |

Each subject has a Map of Content (MOC) that links every framework, case study, and concept note within that domain.

---

## What's Inside

- **180+ Concept Notes** — every major framework, model, and theory taught across top programs (Porter's Five Forces, DCF, Blue Ocean Strategy, Business Model Canvas, Psychological Safety, Theory of Constraints, and more)
- **100+ Case Studies** — landmark business cases mapped to the frameworks they teach (Netflix vs. Blockbuster, Toyota Production System, Enron, Airbnb's Early Days, and more)
- **School Profiles** — HBS, Wharton, Booth, Kellogg, Stanford GSB, Columbia — covering each program's pedagogy, signature curriculum, and philosophy
- **Interactive Graph** — a live D3.js knowledge graph showing the connections between every note in the vault
- **Dataview Dashboards** — queryable tables that surface frameworks by subject, mastery level, and school origin

---

## How It Was Built

### Phase 1 — Vault Architecture (Obsidian)
Built on a Map of Content (MOC) methodology using Obsidian's `[[wikilink]]` system. Every case study links back to the frameworks it teaches. Every framework links forward to the cases that apply it. No isolated notes.

### Phase 2 — Content at Scale (Python + Agentic AI)
Wrote Python scripts to traverse the directory tree, detect ghost nodes (contextual links without underlying files), and batch-generate content. Used agentic LLMs to populate 280+ dense notes with accurate, school-referenced content. Applied regex for link hygiene and path consistency.

### Phase 3 — Web Compilation (Quartz 4)
Integrated with Quartz 4, a React/TypeScript static site generator that natively parses Obsidian syntax — wikilinks, tags, YAML frontmatter — and compiles everything into a fast, interactive website with a live knowledge graph.

### Phase 4 — CI/CD Pipeline (GitHub Actions)
Every `git push` to `main` triggers an automated Ubuntu runner that builds and deploys the full site to GitHub Pages. A local markdown edit becomes a live update within minutes.

---

## Tech Stack

| Layer | Tool |
|---|---|
| Authoring | Obsidian (Markdown, Zettelkasten) |
| Automation | Python, Agentic LLMs |
| Static Site Generator | Quartz 4 (React, TypeScript, Node.js 22) |
| Graph Rendering | D3.js |
| CI/CD | GitHub Actions |
| Hosting | GitHub Pages |

---

## Repository Structure

```
MBA-Brain-/
├── 00 - Home/                  # Dashboard and navigation hub
├── 01 - Finance/               # DCF, WACC, LBO, capital structure...
├── 02 - Strategy/              # Porter, Blue Ocean, VRIO, disruption...
├── 03 - Marketing/             # STP, CLV, brand strategy...
├── 04 - Operations/            # Lean, TOC, supply chain...
├── 05 - Organizational Behavior/
├── 06 - Accounting/
├── 07 - Economics/
├── 08 - Entrepreneurship/
├── 09 - Data & Analytics/
├── 10 - Ethics & ESG/
├── 11 - Case Studies/          # 100+ landmark cases
├── 12 - Frameworks & Models/   # 180+ concept notes
├── 13 - Schools & Professors/  # HBS, Wharton, Booth, Kellogg, GSB, Columbia
├── Templates/                  # Obsidian note templates
├── .github/workflows/          # CI/CD deploy pipeline
└── quartz.config.ts            # SSG configuration
```

---

## Using This Vault Locally

Clone and open in Obsidian for the full local experience — graph view, Dataview queries, Canvas maps, and all plugin functionality.

```bash
git clone https://github.com/Yeshprabhu03/MBA-Brain-.git
```

Then open the folder as a vault in Obsidian. Install recommended plugins: Dataview, Templater, Canvas, Excalidraw.

---

## Contributing

This is a living knowledge base. If you find errors, missing frameworks, or want to add a case study — open a pull request. All contributions welcome.

---

## License

All content is open and free to use for learning purposes.

---

*Built by [Yeshwanth](https://github.com/Yeshprabhu03)*
