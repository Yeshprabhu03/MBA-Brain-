---
title: Inbox — Drop Zone
tags: [inbox, meta]
---

# 📥 Inbox — Drop Zone

> This is where raw material lands before it gets processed into proper vault notes.

---

## 📂 Where to Drop What

| Type of Content | Drop It In |
|----------------|-----------|
| HBS / Wharton / Stanford case studies (text) | `_Inbox/Cases/` |
| Textbook chapters or excerpts | `_Inbox/Textbook Excerpts/` |
| Articles, blog posts, HBR pieces | `_Inbox/Articles/` |
| Lecture slides / class notes | `_Inbox/Lecture Notes/` |
| PDF reading summaries | `_Reading/` |

---

## ✅ Supported Formats

| Format | What Happens |
|--------|-------------|
| `.md` (Markdown) | **Instantly live** — Obsidian shows it, Quartz publishes it on next push |
| `.txt` | Rename to `.md` → instantly works |
| `.pdf` | Quartz can **link** to it; Obsidian can **view** it with PDF plugin |
| Copy-pasted text | Paste into any `.md` file → works immediately |

---

## 🔄 Processing Workflow

When you drop something in:

1. **Raw drop**: Paste or save it in the right `_Inbox/` subfolder
2. **Tag it**: Add `tags: [inbox]` at the top so you can filter unprocessed notes
3. **Process later**: Convert it into a proper vault note using the [[Concept Template]] or [[Case Study Template]]
4. **Link it**: Add wikilinks to the relevant MOC (`[[📊 Finance MOC]]` etc.)
5. **Move it**: Move the finished note to the right subject folder
6. **Publish**: `git push` → site rebuilds in 2 minutes

---

## ⚡ Quick Drop (No Processing Needed)

If you just want to capture something fast without processing:

```markdown
# Title of Thing
tags: [inbox, source-author-name]

[Paste raw text here]

Source: [Book/Case/Article name, page number]
```

Even unprocessed notes will appear in Obsidian graph view and be searchable.

---

## 🔗 Navigation

- [[🏠 Dashboard]] ← Back to home
- [[How to Use This Vault]] ← Full guide
