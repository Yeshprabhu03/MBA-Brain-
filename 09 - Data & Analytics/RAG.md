---
title: RAG
tags: [data-analytics, AI, operations]
aliases: [Retrieval-Augmented Generation, vector database]
---

# 📚 RAG (Retrieval-Augmented Generation)

> **Definition**: An AI framework that improves the quality of LLM-generated responses by grounding the model on external sources of knowledge. It retrieves facts from an external database and attaches them to the user's prompt before the LLM generates an answer.

*The foundational architecture for modern enterprise AI.*

---

## 🔑 The Problem RAG Solves

1. **Knowledge Cutoffs**: An LLM trained in 2023 knows nothing about a regulatory shift that happened yesterday.
2. **Proprietary Data**: Foundational models (like GPT-4) do not know your company's internal HR policies, API documentation, or private financial history.
3. **Hallucinations**: When an LLM doesn't know an answer, it often invents one.

**Retraining** a massive model on your private data costs millions of dollars and takes months. **RAG** solves this instantly and cheaply.

---

## ⚙️ How RAG Works

The process works in two main phases:

### Phase 1: Preparation (The Vector Database)
1. You take all your company's PDFs, Confluence pages, and Jira tickets.
2. An embedding model converts this text into mathematical vectors (numbers representing the "meaning" of the text).
3. These are stored in a **Vector Database** (e.g., Pinecone, Weaviate, Milvus).

### Phase 2: Generation (The RAG Flow)
1. **User asks a question**: *"What is our policy on remote work for engineers?"*
2. **Retrieval**: The system searches the Vector Database for the text chunks with a mathematical "meaning" closest to the user's question.
3. **Augmentation**: It finds the exact PDF paragraph about remote work and dynamically injects it into the prompt behind the scenes: 
   *(System prompt: "Answer the user using only the following text: [Inserted PDF Paragraph]")*
4. **Generation**: The LLM reads the injected context and generates a perfectly accurate, hallucination-free response, often with citations.

---

## 📊 Business Advantages

- **Cost**: Millions of times cheaper than training a custom model.
- **Accuracy**: Effectively eliminates hallucinations because the LLM is restricted to the retrieved facts.
- **Source Citations**: RAG systems can link directly to the exact source document, allowing humans to verify the AI's claims.
- **Access Control**: You can restrict the Vector Database so that an intern asking a question only retrieves public data, while a CFO retrieves private financial data.

---

## 🔗 Connected Concepts

- [[Large Language Models]] — The "Generation" part of RAG
- [[Prompt Engineering]] — How the retrieved data is structured in the context window
- [[AI Strategy]] — Using proprietary data to build moats

---

*← [[📉 Data & Analytics MOC]] | Related: [[Large Language Models]]*
