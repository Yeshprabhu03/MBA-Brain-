---
title: A/B Testing
tags: [data-analytics, concept, experimentation]
aliases: [split testing, randomized experiment, controlled experiment]
---

# 🧪 A/B Testing

> **Definition**: A controlled experiment in which two (or more) versions of a feature, message, or design are shown to randomly assigned user groups to determine which performs better against a defined metric.

*Also known as: Split testing, Randomized Controlled Trial (RCT) in business contexts*
*Key courses: **Wharton MKTG 776, Booth BUSN 41201, HBS Analytics***

---

## 🔑 Why A/B Testing Matters

Before A/B testing, product decisions were made by:
- HiPPO (Highest Paid Person's Opinion)
- Focus groups (not real behavior)
- Intuition and experience

A/B testing replaces opinion with **causal evidence**.

**Famous examples**:
- Google tested 41 shades of blue for toolbar links → chose highest CTR shade → $200M in additional ad revenue
- Amazon tests hundreds of product page variations simultaneously
- Obama 2008 campaign used A/B testing on emails → raised $60M more than the control

---

## 📐 Experimental Design

### The Controlled Experiment Setup

```
All Users
    ↓ Random assignment
    ├── Control (A): Current version
    └── Treatment (B): New version
              ↓
    Measure metric for both groups
              ↓
    Statistical significance test
              ↓
    Decision: Ship B? Keep A?
```

**Key requirements**:
1. **Random assignment** — ensures groups are comparable
2. **Sufficient sample size** — enough statistical power
3. **Single variable change** — isolate the causal factor
4. **Pre-specified metric** — defined *before* running the test

---

## 📊 Key Statistical Concepts

### Statistical Significance (p-value)
- **p-value**: Probability of seeing results this extreme if there's actually no difference
- Convention: p < 0.05 (5% threshold) → "statistically significant"
- **What it means**: If p = 0.03, there's a 3% chance this result occurred by random chance

### Type I and Type II Errors

| Error | Definition | Consequence |
|-------|-----------|-------------|
| **Type I (False Positive)** | Detected effect that doesn't exist | Ship bad feature |
| **Type II (False Negative)** | Missed real effect | Kill good feature |
| α (alpha) | Type I error rate | Typically 5% |
| β (power) | 1 − Type II error rate | Typically 80% |

### Statistical Power
$$\text{Power} = 1 - \beta$$

**Sufficient power (80%)** requires:
- Large enough sample
- Sufficiently long test duration
- Large enough expected effect size

**Underpowered test** = dangerous: may conclude no difference when one exists.

---

## 🧮 Minimum Sample Size Formula

$$n = \frac{2 \cdot (z_{\alpha/2} + z_{\beta})^2 \cdot p(1-p)}{\delta^2}$$

Where:
- `p` = baseline conversion rate
- `δ` = minimum detectable effect (MDE) — the smallest change worth detecting
- `z_α/2` = 1.96 for 95% confidence
- `z_β` = 0.84 for 80% power

**Rule of thumb**: Use online calculators (Evan Miller, Optimizely) for actual calculations.

---

## ⚠️ A/B Testing Pitfalls

| Pitfall | Problem | Fix |
|---------|---------|-----|
| **Stopping early** | P-value fluctuates; stopping when favorable → false positives | Pre-register test duration |
| **Multiple testing** | Test 20 metrics, 1 will be significant by chance | Bonferroni correction or pre-specify primary metric |
| **Novelty effect** | Users explore new features briefly then revert | Run test long enough (2+ weeks) |
| **Network effects** | Your treatment users interact with control users | Cluster randomization |
| **Sample ratio mismatch** | Unequal split suggests logging bug | Check randomization before analyzing |
| **SUTVA violation** | Treatment affects control group | Use geo-randomization |

---

## 🚀 Advanced Techniques

### Multi-Armed Bandit
Instead of 50/50 split, dynamically allocate traffic to winners:
- Trade off exploration (learning) vs. exploitation (earning)
- Useful when tests are long and variants are many
- Used by: Netflix recommendations, Google Ads

### Sequential Testing
Test while the experiment runs using Bayesian updating:
- Can stop early with statistical validity
- Used by: Amazon, Microsoft

### Switchback Testing
For marketplace/logistics: alternate between A and B by time period
- Handles network interference between users

---

## 💼 What to A/B Test in Business

| Function | Examples |
|---------|----------|
| **Product** | Feature UX, onboarding flow, notification timing |
| **Marketing** | Email subject lines, ad creative, landing pages |
| **Pricing** | Discount levels, price anchoring, bundling |
| **Operations** | Warehouse layout, fulfillment routing |
| **Finance** | Credit approval criteria, fraud thresholds |

---

## 🔗 Connected Concepts

- [[Statistical Significance vs. Practical Significance]] — Both matter
- [[Hypothesis Testing]] — A/B testing is applied hypothesis testing
- [[Customer Lifetime Value]] — Testing impacts on long-term metrics
- [[Behavioral Economics Overview]] — What you're testing often exploits biases
- [[Growth Hacking]] — A/B testing is the foundation of growth

---

*← [[📉 Data & Analytics MOC]] | Related: [[Hypothesis Testing]] · [[Statistical Significance]] · [[Growth Hacking]]*
