---
title: Customer Lifetime Value
tags: [marketing, finance, concept]
aliases: [CLV, LTV, customer lifetime value]
---

# 💎 Customer Lifetime Value (CLV)

> **Definition**: The total net profit a company expects to earn from a customer over the entire duration of their relationship. CLV is the single most important metric for understanding the economics of a customer business.

*Key courses: **Kellogg MKTG 431, Wharton MKTG 611, HBS Marketing***

---

## 📐 Core Formulas

### Simple CLV (Non-discounted)
$$CLV = \text{Avg Revenue/Customer/Year} \times \text{Gross Margin \%} \times \text{Avg Customer Lifetime (years)}$$

**Or equivalently:**
$$CLV = \frac{\text{Avg Revenue/Customer/Year} \times \text{Gross Margin \%}}{\text{Churn Rate}}$$

### Discounted CLV (More rigorous)
$$CLV = \sum_{t=1}^{T} \frac{m \times r^t}{(1+d)^t}$$

Where:
- `m` = margin per period (revenue × gross margin)
- `r` = retention rate per period
- `d` = discount rate (cost of capital)
- `T` = time horizon

---

## 🧮 Worked Example

**SaaS Company:**
- Monthly subscription: $100/month
- Gross margin: 70%
- Monthly churn: 2% (so retention = 98%)
- Discount rate: 10% annually (0.8%/month)

**Average Customer Lifetime** = 1 / churn rate = 1 / 0.02 = **50 months**

**Simple CLV** = $100 × 70% × 50 months = **$3,500**

**Discounted CLV** ≈ $3,500 / (1 + discount effect) ≈ ~**$2,800–$3,200**

---

## 💼 The LTV/CAC Ratio

**The most important unit economics metric in any subscription/recurring revenue business.**

$$\frac{LTV}{CAC} = \frac{\text{Customer Lifetime Value}}{\text{Customer Acquisition Cost}}$$

| Ratio | Interpretation |
|-------|---------------|
| < 1 | Every customer costs more to acquire than they're worth → **Death spiral** |
| 1–3 | Marginal — barely profitable, need to improve |
| **3** | **Healthy — rule of thumb benchmark** |
| 5+ | Leaving money on the table — invest more in growth |

**Payback Period** = CAC / (Monthly Revenue × Gross Margin %)
- Good benchmark: < 12 months for SaaS

---

## 📊 CLV by Cohort

Never look at CLV as a single number — break it down by acquisition cohort:

| Cohort | Month Acquired | 12-Mo CLV | 24-Mo CLV | Churn Rate |
|--------|---------------|-----------|-----------|-----------|
| 2022-Q1 | Q1 2022 | $850 | $1,400 | 3.2% |
| 2023-Q1 | Q1 2023 | $920 | $1,580 | 2.8% |
| 2024-Q1 | Q1 2024 | $980 | TBD | 2.5% |

**Good sign**: More recent cohorts have higher CLV and lower churn (product improving + better targeting).

---

## 🎯 Strategic Implications

### CLV Informs These Decisions:

**1. How much to spend on acquisition (CAC ceiling)**
If CLV = $500, paying $400 CAC = terrible business. If CLV = $5,000, $400 CAC = great business.

**2. Which customer segments to target**
High-CLV segments deserve more investment. Low-CLV may not be worth serving.

**3. Pricing strategy**
Raising prices may reduce acquisition volume but dramatically increase CLV.

**4. Retention investment**
Reducing churn from 5% → 3% increases CLV by 67%. Retention is often more valuable than acquisition.

**5. Product roadmap**
Build features that serve high-CLV customers, not just most vocal ones.

---

## ⚠️ CLV Pitfalls

| Mistake | Impact |
|---------|--------|
| Using revenue instead of margin | Overstates CLV — use gross margin |
| Not discounting future cash flows | Overstates CLV for long horizon |
| Using average when segments vary wildly | Hides the actual composition |
| Ignoring referral value | Underestimates CLV for advocates |
| Treating CLV as fixed | It changes with retention/pricing |

---

## 🔗 Connected Concepts

- [[STP Framework]] — Target segments with highest CLV
- [[Net Promoter Score]] — High NPS customers often have highest CLV
- [[Customer Acquisition Cost]] — CLV/CAC is the key ratio
- [[Pricing Strategies]] — Price changes dramatically affect CLV
- [[Unit Economics]] — CLV is the core unit economic

---

*← [[📣 Marketing MOC]] | Related: [[STP Framework]] · [[Net Promoter Score]] · [[Customer Acquisition Cost]]*
