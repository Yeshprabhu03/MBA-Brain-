---
title: Target Pregnancy Prediction
tags: [case-study, data-analytics, predictive-analytics, privacy]
---

# 📚 Target's Pregnancy Prediction Model

> **Core Lesson**: Predictive analytics can be so powerful it becomes socially intrusive — Target's pregnancy prediction model correctly identified pregnant customers and changed their shopping behavior before they announced publicly, raising profound questions about data ethics and consumer privacy.

*Reported by Charles Duhigg, NYT (2012); later in "The Power of Habit" (2012)*

---

## 📋 Case Overview

| Attribute | Detail |
|-----------|--------|
| **Company** | Target Corporation |
| **Analyst** | Andrew Pole (statistician, Target's Guest Marketing Analytics) |
| **Goal** | Identify pregnant shoppers to change their lifelong shopping habits |
| **Method** | Purchase pattern analysis → pregnancy prediction score |
| **Result** | Accurate enough to infer pregnancies before public announcement |
| **Controversy** | Teenage girl's pregnancy revealed to her father via targeted mailers |

---

## 🕰️ Background: Why Pregnancy?

**The strategic insight**: New parents are uniquely susceptible to **habit change**. When a baby arrives, exhausted parents can't maintain their shopping routines. They'll shop wherever is most convenient.

If Target can identify and reach pregnant customers **before the baby arrives**, they can become the default store for a new parent — a relationship worth ~$10,000+ in additional lifetime spend.

The challenge: Competitors (Babies R Us, Walmart) already had baby registries. Target needed to find pregnant customers BEFORE they registered.

---

## 📊 Building the Model

### Step 1: Identify the Signal
Target's statistician Andrew Pole noticed consistent purchase pattern shifts among customers who later registered in the baby registry:

Around **month 4–5 of pregnancy**, customers started buying:
- Unscented lotions (skin sensitivity increases)
- Large vitamin/supplement purchases (prenatal vitamins)
- Hand sanitizer and cotton balls (nesting behavior)
- Larger bags and totes
- Specific mineral supplements (calcium, magnesium, zinc combinations)

These signals appeared consistently BEFORE the customer registered for baby products.

### Step 2: The Pregnancy Prediction Score
Pole built a model that assigned each female customer a "pregnancy prediction score" — likelihood and estimated due date.

**Model inputs**: 25+ specific product categories and purchase timing patterns
**Model output**: 0–100 probability of current pregnancy + estimated trimester

**Accuracy**: High enough to send targeted "congratulations on your pregnancy" mailers to non-public pregnancies.

### Step 3: The Father Incident
A man walked into a Target in Minneapolis demanding to speak to a manager. His complaint: Target was sending pregnancy-related ads to his teenage daughter.

The manager apologized. Called back to apologize again later.

The father: "I had a talk with my daughter. It turns out there have been some activities in my house I haven't been completely aware of. She's due in August. I owe you an apology."

Target's model had correctly identified a pregnancy the girl's own father didn't know about.

---

## 🔐 The Privacy Problem

After the NYT article, Target faced public outrage:

**The core concern**: Companies can infer deeply personal life events (pregnancy, illness, divorce, financial trouble) from innocuous purchase patterns without the person's knowledge or consent.

**Target's response**: Disguised the pregnancy targeting by mixing pregnancy ads with random unrelated ads (lawn furniture, wine glasses) in the same mailer. The targeting was equally effective but less obviously surveillance-based.

**The ethics question uncovered**: 
- Is the problem the targeting, or the transparency about it?
- Should consumers have a right to opt out of predictive modeling?
- If a company can infer pregnancy, what else can be inferred?

---

## 📊 The Data Ethics Framework

| Consideration | Question |
|--------------|---------|
| **Consent** | Did customers agree to this use of their data when they gave their loyalty card? |
| **Harm** | Was anyone harmed by the prediction? (The father's case: actually yes) |
| **Transparency** | Could customers see what Target knew about them? |
| **Purpose limitation** | Is predicting pregnancy within the reasonable scope of a retailer's data use? |
| **Right to be wrong** | False positives exist. What happens when Target targets a non-pregnant woman? |

---

## 🔑 Key Lessons

1. **Behavioral data reveals what customers won't tell you** — Purchase patterns are honest; self-reported data is not
2. **Life transition moments are maximum marketing opportunity** — Habits change during major life events; reaching people then creates lasting loyalty
3. **Power of prediction creates ethical responsibility** — Just because you can infer something doesn't mean you should act on it
4. **Transparency can mitigate the "creep factor"** — Target's solution (mixing ads) shows that disclosed data use feels less invasive than covert profiling
5. **Accuracy creates new risks** — A model that works creates problems that don't exist when targeting is crude

---

## 🎓 Discussion Questions

1. Should Target have used the pregnancy prediction model? What conditions would make it ethical or unethical?
2. What are the obligations of companies when they infer sensitive personal information from behavioral data?
3. The EU GDPR requires "purpose limitation" — data collected for one purpose can't be repurposed. How would GDPR change Target's model?

---

## 🔗 Connected Concepts

- [[Regression Analysis]] — Logistic regression is the underlying model
- [[A/B Testing]] — Target A/B tested which ad mixes were less creepy
- [[Behavioral Economics Overview]] — Habit formation and the "habit loop" Target exploited
- [[Facebook Cambridge Analytica]] — Companion case: using behavioral data for targeting with consent questions
- [[Amazon Hiring Algorithm Bias]] — Companion: when algorithms create unintended consequences

---

*← [[📉 Data & Analytics MOC]] | [[📚 Case Studies MOC]]*