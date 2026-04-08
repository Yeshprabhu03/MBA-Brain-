# 🎓 MBA Second Brain: Decentralized Knowledge Graph

**Live Deployment:** [https://Yeshprabhu03.github.io/MBA-Brain-/](https://Yeshprabhu03.github.io/MBA-Brain-/)

Welcome to the **MBA Knowledge Vault** repository. This project is a comprehensive, decentralized Map of Content (MOC) built to structure, search, and visualize core MBA concepts and business case studies. 

It transforms a raw collection of markdown notes into an interactive, globally accessible digital garden powered by an automated CI/CD pipeline.

---

## 🛠️ The Tech Stack

*   **Authoring & Data Layer:** [Obsidian](https://obsidian.md/) (Local-first Markdown, Zettelkasten methodology)
*   **Data Engineering & Automation:** Python (RegEx, File-system traversing), Agentic LLMs
*   **Static Site Generator (SSG):** [Quartz 4](https://quartz.jzhao.xyz/) (React, Node.js v22, TypeScript)
*   **CI/CD Pipeline:** GitHub Actions
*   **Hosting:** GitHub Pages

---

## 🏗️ Architecture & Development Lifecycle

### Phase 1: Architecture & Structural Design (Obsidian)
**The Goal:** Create a "Second Brain" that naturally surfaces connections between disparate business concepts.
*   Instead of a rigid, traditional folder structure, this vault relies on a **Map of Content (MOC)** architecture, categorizing MBA knowledge into 10 distinct subjects (e.g., Finance, Strategy, Operations).
*   Utilized Obsidian's Markdown-based `[[wikilink]]` system to create highly interconnected nodes, ensuring every Case Study inherently links back to core theoretical business frameworks, creating a resilient and decentralized database structure.

### Phase 2: Data Engineering & Automation (Python + Agentic AI)
**The Goal:** Scale the database from an empty skeleton to a high-fidelity knowledge vault, mapping out over 300 highly specific business topics.
*   Executed automated graph-analysis to locate **"Ghost Nodes"**—links that existed contextually but lacked underlying markdown files.
*   Wrote custom **Python** ingestion and processing scripts. Leveraged Agentic LLMs to batch-generate and populate >180 dense concept notes and >100 case study notes. 
*   Scripts traversed the directory tree, injected generated markdown into the correct subject folders, and applied RegEx to ensure strict link hygiene (e.g., safely escaping characters and handling directory path discrepancies).

### Phase 3: Web Compilation (Quartz 4 / TypeScript)
**The Goal:** Transform complex, local Markdown files into a lightweight, interactive, and public-facing website.
*   Integrated the vault with **Quartz 4**, a highly optimized SSG. 
*   Quartz, running on Node.js and React, natively parses Obsidian's unique syntax (tags, wikilinks, YAML frontmatter). It strips out local, private directories and compiles the markdown into standardized HTML/CSS.
*   It also renders the complex multi-dimensional relationships between notes into an interactive, front-end D3.js network graph visible on the live site.

### Phase 4: Continuous Deployment (GitHub Actions)
**The Goal:** Establish a frictionless deployment pipeline where modifying a local `.md` file instantly updates the live web application.
*   Engineered a CI/CD pipeline using a **GitHub Actions `.yml` workflow**. 
*   Every `git push` to the `main` branch triggers an automated Ubuntu runner. The runner initializes Node.js 22, clones the open-source Quartz engine, parses the latest Markdown files from this repository, builds the static website, and pushes the production assets directly to **GitHub Pages**.

---

## 📂 Repository Structure Highlights
*   **`00 - Home/` & `[01-10] - Subject Folders/`**: The core data structures holding the actual markdown nodes.
*   **`.github/workflows/deploy.yml`**: The CI/CD instructions powering the automated website build.
*   **`quartz.config.ts`**: The TypeScript configuration dictating how the SSG ignores system files and renders the user interface.

*Created and maintained by Yeshwanth.*
