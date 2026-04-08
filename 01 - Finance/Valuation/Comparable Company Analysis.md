---
title: Comparable Company Analysis
tags: [finance, valuation, concept]
aliases: [trading comps, public comps, comparable companies, EV/EBITDA]
---

# 🔍 Comparable Company Analysis (Trading Comps)

> **Definition**: A relative valuation methodology that values a company by comparing its financial metrics (revenue, EBITDA, earnings) to those of publicly-traded peer companies, using implied market multiples.

*Also called: "Comps," "Trading multiples," "Public comps"*
*Part of the standard IB valuation toolkit alongside [[DCF Valuation]] and Precedent Transactions.*

---

## 🔑 The Core Logic

**Principle**: Similar companies in the same industry should trade at similar multiples.

If Company A trades at **10× EBITDA** and Company B is identical, then Company B is also worth **~10× EBITDA**.

**Key assumption**: Capital markets are roughly efficient at pricing comparable companies.

---

## 📐 Step-by-Step Process

### Step 1: Select Comparable Companies
The most important (and most debated) step.

**Ideal comps are similar on**:
- Industry / subsector
- Business model (recurring revenue, transaction-based, etc.)
- Revenue scale (within 3–5× ideally)
- Geography
- Growth rate
- Margin profile
- Capital intensity

**Reality**: Perfect comps rarely exist. Use judgment; note differences in analysis.

---

### Step 2: Spread Key Financial Data

For each comp, collect **LTM (Last Twelve Months)** and forecast data:

| Metric | Trailing (LTM) | Forward (NTM) |
|--------|---------------|---------------|
| Revenue | ✓ | ✓ (consensus) |
| Gross Profit | ✓ | |
| EBITDA | ✓ | ✓ |
| EBIT | ✓ | |
| Net Income | ✓ | ✓ |
| EPS | ✓ | ✓ |

---

### Step 3: Calculate Market Multiples

**Enterprise Value (EV) multiples** (capital structure-neutral):

$$EV = \text{Market Cap} + \text{Net Debt} + \text{Minority Interest} - \text{Associates}$$

$$\text{Net Debt} = \text{Total Debt} - \text{Cash \& Equivalents}$$

| Multiple | Formula | Used For |
|---------|---------|---------|
| **EV/Revenue** | EV ÷ Revenue | Early-stage, high-growth companies |
| **EV/EBITDA** | EV ÷ EBITDA | Most common; eliminates D&A differences |
| **EV/EBIT** | EV ÷ EBIT | Capital-intensive businesses |
| **EV/FCF** | EV ÷ Free Cash Flow | Cash-generative mature businesses |

**Equity Value multiples** (levered):

| Multiple | Formula | Used For |
|---------|---------|---------|
| **P/E** | Price ÷ EPS | Banks, insurers, general companies |
| **P/B** | Price ÷ Book Value | Banks, asset-heavy companies |

---

### Step 4: Calculate Implied Valuation Range

Once you have the comp set multiples (e.g., EV/EBITDA range of 9.0× – 13.0×):

**Apply to your target company**:
$$\text{Implied EV} = \text{Target EBITDA} \times \text{Multiple Range}$$

$$\text{Implied Equity Value} = \text{Implied EV} - \text{Net Debt}$$

$$\text{Implied Share Price} = \frac{\text{Implied Equity Value}}{\text{Shares Outstanding}}$$

---

## 📊 Example: Software Company Comps

| Company | Revenue | EBITDA | EV | EV/Revenue | EV/EBITDA |
|---------|---------|--------|-----|-----------|----------|
| Salesforce | $30B | $5.4B | $190B | 6.3× | 35.2× |
| Workday | $7.2B | $1.1B | $52B | 7.2× | 47.3× |
| ServiceNow | $8.9B | $1.7B | $130B | 14.6× | 76.5× |
| HubSpot | $2.2B | $0.26B | $20B | 9.1× | 76.9× |
| **Median** | | | | **7.8×** | **62.0×** |

**Target company**: $500M revenue, $75M EBITDA
- **Implied EV at median revenue multiple**: $500M × 7.8× = **$3.9B**
- **Implied EV at median EBITDA multiple**: $75M × 62.0× = **$4.65B**

---

## ⚠️ Comps Limitations

| Limitation | Why It Matters |
|-----------|---------------|
| No two companies are identical | Adjustments are subjective |
| Market may misprice the sector | Comps capture sentiment, not value |
| LTM ≠ future performance | Forward comps require estimates |
| Control premium not included | Public comps undervalue acquisition targets |
| Wide range with few comps | Small samples = noisy output |

**Control premium**: In acquisitions, buyers pay 20–40% above trading comps — because buyers need to justify paying for control. Use **Precedent Transactions** for M&A pricing.

---

## 🔗 Connected Concepts

- [[DCF Valuation]] — Intrinsic value; paired with comps for the "football field"
- [[LBO Model]] — PE buyer's constraint on how much they can pay
- [[Investment Banking Overview]] — Comps are a core IB deliverable
- [[Capital Markets]] — Public market data is the source for comps
- [[WACC]] — DCF complement to comps-based valuation

---

*← [[📊 Finance MOC]] | Related: [[DCF Valuation]] · [[LBO Model]] · [[Investment Banking Overview]]*
