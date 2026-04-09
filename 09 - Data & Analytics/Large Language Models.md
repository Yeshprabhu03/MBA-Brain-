---
title: Large Language Models
tags: [data-analytics, AI, concept]
aliases: [LLM, GenAI, foundation models]
---

# 🤖 Large Language Models (LLMs)

> **Definition**: Deep learning algorithms that can recognize, summarize, translate, predict, and generate text and other content based on knowledge gleaned from massive datasets.

*Key for understanding the current tech supercycle at: **Stanford GSB, MIT Sloan***

---

## 🔑 The Core Idea

Traditional software is deterministic (if `A` then `B`). LLMs are probabilistic—they predict the next most likely token (word/fragment) based on billions of parameters trained on vast swaths of the internet.

### How They Work
1. **Pre-training**: The model ingests a massive corpus of text to learn grammar, facts, and reasoning capabilities.
2. **Fine-tuning**: The model is adapted to specific tasks (e.g., following instructions, acting as a chatbot, answering legal queries).
3. **Inference**: The model generates responses to user prompts in real-time.

---

## 📊 Business Applications

LLMs shift the paradigm of computing from *graphical user interfaces* to *conversational user interfaces*.

| Capability | Business Use Case |
|------------|----------------|
| **Text Generation** | Automating email drafts, marketing copy, and report writing. |
| **Summarization** | Distilling 50-page earnings transcripts into 1-page executive summaries. |
| **Classification** | Sorting customer support tickets by urgency and sentiment. |
| **Code Generation** | Assisting software engineers via tools like GitHub Copilot (increasing productivity by 30-50%). |
| **Translation** | Real-time, highly contextual cross-border communication. |

---

## ⚠️ Challenges & Limitations

- **Hallucinations**: LLMs sometimes confidently invent facts. They are text-prediction engines, not databases of truth.
- **Context Window**: They can only "remember" a certain amount of text per conversation (though this is expanding rapidly).
- **Data Privacy**: Inputting sensitive corporate data into public APIs (like standard ChatGPT) can lead to data leaks if not managed through enterprise agreements.
- **Compute Costs**: Training and running inference on these models requires massive GPU clusters, leading to high operational costs.

---

## 🔗 Connected Concepts

- [[Generative AI Business Uses]] — Specific functional applications
- [[AI Strategy]] — How to build moats using LLMs
- [[RAG]] — How to ground LLMs in factual corporate data
- [[Prompt Engineering]] — How to extract optimal performance
- [[AI Governance]] — Managing the risks of LLM deployment

---

*← [[📉 Data & Analytics MOC]] | Related: [[Generative AI Business Uses]] · [[AI Strategy]]*
