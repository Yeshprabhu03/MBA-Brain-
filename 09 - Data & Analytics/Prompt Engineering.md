---
title: Prompt Engineering
tags: [data-analytics, AI, skills]
aliases: [prompt design, prompting]
---

# ✍️ Prompt Engineering

> **Definition**: The practice of designing, refining, and optimizing inputs (prompts) to effectively communicate with Large Language Models in order to achieve highly accurate, specific, and desirable outputs.

*Increasingly viewed as a core business skill across disciplines.*

---

## 🔑 The Core Idea

Large Language Models are incredibly powerful, but they operate on literal instructions. A vague prompt yields a generic, hallucinated, or unhelpful response. Prompt engineering is effectively "programming in natural language."

### The "Anatomy" of a Perfect Prompt
A professional, enterprise-grade prompt typically contains 5 elements:
1. **Persona**: "Act as a senior management consultant at McKinsey..."
2. **Task**: "...analyze this Q3 earnings transcript..."
3. **Context**: "...our firm is considering acquiring this company and we are worried about their supply chain exposure in Asia..."
4. **Format**: "...output the analysis as a markdown table with three columns..."
5. **Constraints**: "...do not use jargon, keep the summary under 500 words, and only use facts explicitly stated in the text."

---

## 🛠️ Advanced Prompting Techniques

### 1. Few-Shot Prompting
Instead of just asking the AI to do something (zero-shot), you provide 2 or 3 completed examples inside the prompt. This forces the model to mimic the exact tone, style, and structure of your targets.

### 2. Chain-of-Thought (CoT) Prompting
Adding the phrase *"Let's think step by step"* to the end of a prompt. This forces the LLM to output its intermediate reasoning. By breaking the problem down, mathematical and logical accuracy skyrockets.

### 3. Tree of Thoughts
Asking the AI to generate multiple different possible approaches to a problem, evaluate the pros and cons of each, and then select the best one before executing.

### 4. RAG-Augmented Prompting
Retrieval-Augmented Generation (see [[RAG]]). The prompt is dynamically injected with external factual data from a database right before being sent to the LLM. 

---

## ⚠️ Pitfalls to Avoid

- **Vagueness**: "Write a blog post about finance."
- **Assuming Context**: The AI doesn't know your company's history unless you tell it.
- **Negative Constraints**: AI struggles with "Do not do X". It is much better to formulate positively: "Instead of X, do Y."

---

## 🔗 Connected Concepts

- [[Large Language Models]] — The engines you are prompting
- [[RAG]] — How enterprises scale prompting automatically
- [[Generative AI Business Uses]] — Where these skills are applied

---

*← [[📉 Data & Analytics MOC]] | Related: [[Large Language Models]]*
