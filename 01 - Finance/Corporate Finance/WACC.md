---
title: WACC
tags: [finance, concept, valuation, corporate-finance]
aliases: [Weighted Average Cost of Capital, cost of capital]
---

# 🔢 WACC — Weighted Average Cost of Capital

> **Definition**: WACC is the average rate a company is expected to pay to finance its assets — a blended cost of debt and equity, weighted by their proportions.

*The discount rate in almost every [[DCF Valuation]] model.*

*Key course: **Wharton FNCE 611, HBS Finance I, Booth BUSF 33001***

---

## 📐 The Formula

$$WACC = \frac{E}{V} \cdot r_e + \frac{D}{V} \cdot r_d \cdot (1 - T)$$

| Variable | Meaning |
|----------|---------|
| `E` | Market value of equity |
| `D` | Market value of debt |
| `V` | E + D (total firm value) |
| `re` | Cost of equity |
| `rd` | Cost of debt (pre-tax) |
| `T` | Corporate tax rate |
| `(1-T)` | Tax shield on debt |

---

## 🔑 Why the Tax Shield?

Interest payments are **tax deductible** — which means the government subsidizes part of debt financing. If the tax rate is 25% and interest cost is 6%, the **after-tax cost of debt is only 4.5%**.

This is why companies prefer some debt in their capital structure (up to a point) → see [[Capital Structure]].

---

## 📊 Computing Each Component

### 1. Cost of Equity (re) — via CAPM

$$r_e = r_f + \beta \cdot (r_m - r_f)$$

- `rf` = risk-free rate (10-year US Treasury, e.g. 4.5%)
- `β` = company's beta (sensitivity to market)
- `(rm − rf)` = equity risk premium (historical ~5-6%)

**Example**: β = 1.2, rf = 4.5%, ERP = 5.5%
→ `re = 4.5% + 1.2 × 5.5% = 11.1%`

### 2. Cost of Debt (rd)

Use the company's current borrowing rate or yield-to-maturity on outstanding bonds.
- Often estimated from credit rating + spread tables
- Typical range: 4–8% for investment-grade companies

### 3. Weights

Always use **market values**, not book values:
- `E` = share price × shares outstanding
- `D` = current market value of all debt

---

## 🧮 Full WACC Example

Company: 60% equity / 40% debt, T = 25%, re = 11%, rd = 6%

$$WACC = 0.60 \times 11\% + 0.40 \times 6\% \times (1 - 0.25)$$
$$WACC = 6.6\% + 1.8\% = 8.4\%$$

### 💻 Practitioner Python Implementation

```python
def calculate_wacc(equity_val, debt_val, cost_equity, cost_debt, tax_rate):
    """Calculates the Weighted Average Cost of Capital"""
    total_val = equity_val + debt_val
    
    # Weights
    w_e = equity_val / total_val
    w_d = debt_val / total_val
    
    # After-tax cost of debt
    after_tax_debt = cost_debt * (1 - tax_rate)
    
    # WACC Calculation
    wacc = (w_e * cost_equity) + (w_d * after_tax_debt)
    
    return wacc

# Example inputs (in millions)
e_val = 600   # 60% weight
d_val = 400   # 40% weight
r_e = 0.11    # Cost of equity via CAPM
r_d = 0.06    # YTM on debt
t = 0.25      # Corporate tax rate

wacc_result = calculate_wacc(e_val, d_val, r_e, r_d, t)
print(f"Proprietary WACC: {wacc_result:.2%}")
# Output: Proprietary WACC: 8.40%
```

---

## 🎯 What WACC Tells Us

- **WACC = minimum required return** for a project to create value
- Projects earning > WACC create shareholder value
- Projects earning < WACC destroy value
- **IRR > WACC** → accept the project

---

## ⚠️ Common WACC Mistakes

| Mistake | Correct Approach |
|---------|-----------------|
| Using book value weights | Use market value weights |
| Using coupon rate for debt cost | Use yield-to-maturity |
| Using historical beta without thought | Adjust for leverage (Hamada equation) |
| Wrong tax rate | Use marginal tax rate, not effective |
| Circular reference in model | Use iterative calculation or break the circle |

---

## 🔄 WACC Sensitivity

Even small changes in WACC drastically affect valuations:

| WACC | DCF Value |
|------|-----------|
| 8% | $180M |
| 10% | $140M |
| 12% | $112M |

This is why analysts always present WACC sensitivity tables alongside DCF models.

---

## 🔗 Connected Concepts

- [[DCF Valuation]] — WACC is the discount rate
- [[CAPM]] — how re is calculated
- [[Capital Structure]] — how D/E ratio is chosen
- [[Beta and Systematic Risk]] — the β input
- [[Efficient Market Hypothesis]] — context for risk-free rate choice

---

## 🏫 School Context

- **Wharton**: Derives WACC rigorously from Modigliani-Miller propositions
- **HBS**: Emphasis on *judgment* — which beta to use, whether to lever/unlever
- **Columbia**: Heavy use in value investing context; Graham disciples very suspicious of high WACCs on growth stocks

---

*← [[📊 Finance MOC]] | Related: [[DCF Valuation]] · [[CAPM]] · [[Capital Structure]]*
