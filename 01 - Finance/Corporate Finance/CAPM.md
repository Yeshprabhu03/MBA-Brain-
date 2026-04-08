---
title: CAPM
tags: [finance, concept, investments, risk]
aliases: [Capital Asset Pricing Model, Security Market Line, SML]
---

# 📈 CAPM — Capital Asset Pricing Model

> **Definition**: CAPM describes the relationship between systematic risk (beta) and expected return for assets. It is used to price risky securities and compute the cost of equity in [[WACC]].

*Developed by: William Sharpe (Nobel Prize 1990), John Lintner, Jan Mossin*
*Key courses: **Wharton FNCE 611, Booth BUSF 35000, HBS Finance I***

---

## 📐 The Formula

$$r_e = r_f + \beta \cdot (r_m - r_f)$$

| Term | Meaning | Typical Value |
|------|---------|---------------|
| `re` | Expected return on asset | What we solve for |
| `rf` | Risk-free rate | ~4–5% (10-yr US Treasury) |
| `β` | Beta — systematic risk | 1.0 = market average |
| `(rm − rf)` | Equity Risk Premium (ERP) | ~5–6% historically |

---

## 🔑 Understanding Beta (β)

Beta measures **how much a stock moves relative to the market**:

| Beta | Interpretation |
|------|---------------|
| β = 0 | No correlation to market (e.g. T-bills) |
| β = 0.5 | Half as volatile as market |
| β = 1.0 | Moves in lockstep with market |
| β = 1.5 | 50% more volatile than market |
| β = 2.0 | Twice as volatile (e.g. small-cap tech) |
| β < 0 | Inversely correlated (e.g. gold sometimes) |

**High beta stocks**: Technology, startups, commodities  
**Low beta stocks**: Utilities, consumer staples, REITs (defensive)

---

## 🎯 The Security Market Line (SML)

The SML plots **expected return vs. beta** for all assets:

- **On the SML**: Fairly priced
- **Above the SML**: Undervalued (higher return than CAPM predicts) → **Buy**
- **Below the SML**: Overvalued → **Sell**

This is the foundation of alpha generation in active portfolio management.

---

## 📊 CAPM in Practice: Computing Cost of Equity

**Apple (hypothetical)**:
- β = 1.2 (from financial data providers)
- rf = 4.5% (current 10-year Treasury)
- ERP = 5.5% (Damodaran estimate)

$$r_e = 4.5\% + 1.2 \times 5.5\% = 11.1\%$$

→ This 11.1% feeds into [[WACC]] as the cost of equity component.

---

## 🔬 Levered vs. Unlevered Beta

When comparing companies with different capital structures, use the **Hamada equation** to lever/unlever beta:

$$\beta_L = \beta_U \times [1 + (1 - T) \times \frac{D}{E}]$$

**Process**:
1. Find comparable companies' levered betas
2. **Unlever** each beta to remove debt effects
3. Average unlevered betas
4. **Re-lever** at your company's target capital structure

---

## ⚠️ CAPM Limitations

| Limitation | Issue |
|-----------|-------|
| Single-factor model | Only beta matters for returns (empirically untrue) |
| Beta is backward-looking | Historical beta ≠ future beta |
| Normal distribution assumed | Returns are fat-tailed in reality |
| Market portfolio unobservable | We use S&P 500 as a proxy |
| Ignores liquidity, size effects | Fama-French adds size + value factors |

**Fama-French 3-Factor Model** addresses some limitations:
$$r = r_f + \beta_m(r_m-r_f) + \beta_s \cdot SMB + \beta_h \cdot HML$$

---

## 🔗 Connected Concepts

- [[WACC]] — CAPM's output is the cost of equity input
- [[Beta and Systematic Risk]] — deeper dive into β
- [[Efficient Market Hypothesis]] — the theoretical backdrop
- [[DCF Valuation]] — uses WACC (which uses CAPM)
- [[Portfolio Theory]] — Markowitz foundation for CAPM

---

## 🏫 School Context

- **Booth**: Fama-French originated here; CAPM taught with heavy critique
- **Wharton**: Rigorous derivation; applied to real portfolio construction
- **HBS**: Emphasizes *practitioner judgment* — e.g., which ERP to use

---

*← [[📊 Finance MOC]] | Related: [[WACC]] · [[Beta and Systematic Risk]] · [[DCF Valuation]]*
