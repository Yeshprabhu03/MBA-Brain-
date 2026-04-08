---
title: Amazon Hiring Algorithm Bias
tags: [case-study, data-analytics, inbox]
---

# 📚 Amazon Hiring Algorithm Bias

> **Core Lesson**: Algorithmic bias, fairness

---

## 📋 Overview

| Attribute | Detail |
|-----------|--------|
| **Subject** | Data Analytics |
| **Core Lesson** | Algorithmic bias, fairness |
| **Source** | HBS / Top MBA Case |

---

## 🕰️ Background

In 2018, it was revealed that Amazon abandoned an experimental AI hiring tool after discovering it was biased against women. The algorithm, trained on 10 years of resumes (mostly from men), learned that 'masculine' language and participation in 'women's chess clubs' were negative signals for success in software engineering roles.

---

## ❓ The Central Problem

How does 'garbage in, garbage out' create systemic bias in machine learning? The case examines the technical and ethical challenges of using historical data to predict future performance.

---

## 📊 Analysis

The Technical Trap: ML models identify patterns. If historical 'success' was 90% male, the model assumes 'maleness' is a feature of success. Even after removing 'Gender' as a field, the model found 'proxies' (language, hobbies, schools) that correlated with gender. Amazon tried to 'fix' the weights, but they couldn't guarantee it would be truly neutral. Result: They scrapped the project. It shows that AI can automate and scale existing human biases rather than removing them.

---

## 🔑 Key Lessons

1. Historical data is often biased; models trained on it will institutionalize that bias
2. Removing protected attributes (gender, race) is not enough—algorithms find 'proxies' that correlate with those attributes
3. Auditability is a requirement for high-stakes AI (hiring, lending, parole)
4. AI should be a 'decision support' tool, not a 'decision maker' in human-centric processes

---

## 🎓 Discussion Questions

1. How can a data scientist 'de-bias' a dataset without losing predictive power?
2. Should companies use AI for screening at all if bias is inherent in historical data?
3. What was the legal and PR risk of Amazon continuing the project?

---

## 🔗 Connected Concepts

- [[Ethics & ESG]] — AI Fairness
- [[Regression Analysis]] — Feature selection and proxy variables
- [[Probability & Statistics]] — Sampling bias

---

*← [[📉 Data & Analytics MOC]] | [[📚 Case Studies MOC]]*