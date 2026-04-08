---
title: Marriott Corporation - The Cost of Capital
tags: [case-study, finance, wacc, capital-structure]
---

# 📚 Marriott Corporation: The Cost of Capital

> **Core Lesson**: How to calculate divisional WACC for a multi-business company — and why using a single company-wide hurdle rate leads to value-destroying capital allocation decisions.

*Classic HBS case — one of the most-taught finance cases globally*
*Authors: Richard Ruback & W. Carl Kester, HBS (1988)*

---

## 📋 Case Overview

| Attribute | Detail |
|-----------|--------|
| **Company** | Marriott Corporation |
| **Year** | 1987–88 |
| **Business Lines** | Lodging (hotels), Contract Services, Restaurants |
| **Decision** | What hurdle rate (WACC) to use for each division's capital budgeting |
| **Protagonist** | Dan Cohrs, VP of Project Finance |

---

## 🏨 Background

Marriott operated three business lines with fundamentally different risk profiles:
- **Lodging**: Hotels (Marriott, Courtyard, Residence Inn) — cyclical, capital-intensive
- **Contract Services**: Airport food/beverage, facilities management — stable, recession-resistant
- **Restaurants**: Roy Rogers, Hot Shoppes — consumer discretionary

**Marriott's financial strategy**: Aggressive debt use (tax shields), asset-light model (develop then sell hotels, retain management contracts), rapid growth through capital deployment.

**The core question**: Should Marriott use one WACC for the entire company, or different hurdle rates for each division?

---

## ❓ The Central Problem

Using a **single company-wide WACC** for capital budgeting creates systematic errors:
- One WACC too low for high-risk projects → managers accept projects that don't compensate for risk
- One WACC too high for low-risk projects → managers reject value-creating safe projects

**Example of the misallocation**:
- Contract Services has a low-risk, stable cash flow business worth funding at ~9.8%
- Using company WACC of ~11.9% means rejecting good contract services projects
- Meanwhile, risky lodging projects need to clear ~12%, not 11.9%

**Solution**: Each division needs its own hurdle rate reflecting its own systematic risk.

---

## 📊 Calculating Divisional WACC — Step by Step

$$WACC = \frac{E}{V} \times r_e + \frac{D}{V} \times r_d \times (1-T)$$

### Step 1: Cost of Debt ($r_d$) — Government Rate + Spread
Marriott uses government bond rate + a division-specific spread:

| Division | Spread Above Treasury |
|---------|----------------------|
| Lodging | +1.10% |
| Contract Services | +1.40% |
| Restaurants | +1.80% |

With 10-year Treasury at 8.72%: Lodging debt cost = 9.82%, etc.

### Step 2: Cost of Equity via CAPM
$$r_e = r_f + \beta_L \times (r_m - r_f)$$
- Risk-free rate ($r_f$): 8.72% (10-year US Treasury)
- Equity risk premium: 7.43% (historical average)
- Beta: Must be estimated from **comparable public companies**

### Step 3: The Beta Process (Hardest Part)
Each division's beta comes from pure-play public companies:

```
1. Find comparable public companies for each division
2. Get their levered betas (from stock data)
3. UNLEVER each beta to remove their capital structure:
   βu = βL ÷ [1 + (1−T) × (D/E)]
4. Average the unlevered (asset) betas
5. RE-LEVER using Marriott's target D/E for that division:
   βL = βu × [1 + (1−T) × (D/E)]
6. Use in CAPM to get divisional cost of equity
```

### Step 4: Target Capital Structure
Marriott uses **target** (not current) capital structure:

| Division | Target Debt % |
|---------|--------------|
| Lodging | 74% |
| Contract Services | 40% |
| Restaurants | 42% |

---

## 🧮 Worked Example: Lodging Division

| Step | Calculation | Result |
|------|-------------|--------|
| Asset beta from hotel comps | Unlever comparable hotel company betas | ~0.41 |
| Re-lever at 74% debt (D/E=2.85, T=44%) | 0.41 × [1 + 0.56 × 2.85] | **1.07** |
| Cost of equity (CAPM) | 8.72 + 1.07 × 7.43 | **16.7%** |
| Cost of debt | 8.72 + 1.10 | **9.82%** |
| Divisional WACC | 0.26×16.7% + 0.74×9.82%×(1−0.44) | **≈ 8.7%** |

---

## 🔑 Key Lessons

1. **Divisional hurdle rates** — A conglomerate must use separate WACCs; one rate destroys value
2. **WACC is forward-looking** — Use *target* capital structure, not current
3. **Beta = business risk + financial risk** — Unlever/re-lever when comparing across firms
4. **Market values, not book values** — Use market cap and market debt for E and D in weights
5. **Pure-play comparables** — Best approach to estimate beta when the division isn't separately traded

---

## 🎓 Discussion Questions

1. Why is using a single company-wide WACC for capital budgeting harmful?
2. What are the challenges in estimating divisional betas from comparable companies?
3. Should Marriott use book-value or market-value weights? Why?
4. What is the appropriate risk-free rate — T-bill or T-bond? Why?
5. Why does Marriott use **target** capital structure, not current?

---

## 🔗 Connected Concepts

- [[WACC]] — The core concept this case teaches
- [[CAPM]] — Used to estimate cost of equity
- [[Capital Structure]] — Target D/E drives divisional WACC
- [[DCF Valuation]] — WACC is the discount rate
- [[Comparable Company Analysis]] — Source of pure-play betas

---

*← [[📚 Case Studies MOC]] | [[📊 Finance MOC]]*
