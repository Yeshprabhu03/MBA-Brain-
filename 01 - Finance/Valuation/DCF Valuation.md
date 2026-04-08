---
title: DCF Valuation
tags: [finance, valuation, concept]
aliases: [Discounted Cash Flow, DCF, intrinsic value]
---

# 💰 DCF Valuation (Discounted Cash Flow)

> **Definition**: DCF is a valuation method that estimates the value of an investment by discounting future free cash flows back to the present using an appropriate discount rate (WACC).

*Heavily covered at: **Wharton · Booth · Columbia · HBS Finance II***

---

## 🔑 The Core Idea

A company is worth the **present value of all future free cash flows it will ever generate**.

$$\text{Enterprise Value} = \sum_{t=1}^{n} \frac{FCFF_t}{(1 + WACC)^t} + \frac{TV}{(1 + WACC)^n}$$

Where:
- `FCFF` = Free Cash Flow to the Firm
- `WACC` = Weighted Average Cost of Capital
- `TV` = Terminal Value
- `n` = explicit forecast period (typically 5–10 years)

---

## 📐 Step-by-Step DCF Process

### Step 1: Project Free Cash Flows

$$FCFF = EBIT(1-T) + D\&A - CapEx - \Delta NWC$$

| Component | Meaning |
|-----------|---------|
| EBIT(1-T) | NOPAT — operating profit after tax |
| + D&A | Add back non-cash charges |
| − CapEx | Capital expenditure (maintenance + growth) |
| − ΔNWC | Change in Net Working Capital |

**Forecast period**: Typically 5–10 years; beyond that, use a Terminal Value.

### Step 2: Calculate WACC
→ See [[WACC]] for full calculation

$$WACC = \frac{E}{V} \cdot r_e + \frac{D}{V} \cdot r_d (1-T)$$

### Step 3: Calculate Terminal Value

**Gordon Growth Model** (most common):
$$TV = \frac{FCFF_n \times (1+g)}{WACC - g}$$

**Exit Multiple Method**:
$$TV = EBITDA_n \times \text{Exit Multiple}$$

> 💡 A common mistake: TV often represents 60–80% of total value in growth companies. Your terminal value assumption matters *enormously*.

### Step 4: Discount Everything Back

$$EV = \sum \frac{FCFF_t}{(1+WACC)^t} + \frac{TV}{(1+WACC)^n}$$

### Step 5: Bridge to Equity Value

$$\text{Equity Value} = EV - \text{Net Debt}$$
$$\text{Share Price} = \frac{\text{Equity Value}}{\text{Shares Outstanding}}$$

---

## 🎯 DCF Sensitivity Analysis

Never present a single DCF number. Always run a **sensitivity table**:

|  | WACC 8% | WACC 10% | WACC 12% |
|--|---------|----------|----------|
| g = 2% | $120 | $95 | $78 |
| g = 3% | $145 | $110 | $88 |
| g = 4% | $185 | $132 | $102 |

---

## ⚠️ DCF Pitfalls & Limitations

| Pitfall | Why It Matters |
|---------|---------------|
| Garbage in, garbage out | Revenue assumptions drive everything |
| Terminal value dominance | 60-80% of value may sit in TV |
| WACC precision illusion | Small changes in WACC = huge EV swings |
| Ignores real options | Flexibility has value not captured |
| Circular reference risk | Debt affects WACC which affects value |

**Damodaran's wisdom**: "A DCF is only as good as the story behind it."

---

## 🔄 DCF vs. Other Valuation Methods

| Method | Pros | Cons |
|--------|------|------|
| DCF | Intrinsic value, not market-dependent | Highly sensitive to assumptions |
| Comparable Companies | Market-grounded | Requires truly comparable peers |
| Precedent Transactions | Includes control premium | Historical data may be stale |
| LBO | Sets a price floor | Only relevant if buyable |

> In practice, bankers use all three and triangulate.

---

## 📊 Real Example: Simple DCF

**Assume a company with:**
- Year 1-5 FCFF growing from $100M to $146M (8%/year)
- WACC = 10%
- Terminal growth = 3%

| Year | FCFF | Discount Factor | PV |
|------|------|----------------|----|
| 1 | 100 | 0.909 | 90.9 |
| 2 | 108 | 0.826 | 89.2 |
| 3 | 116.6 | 0.751 | 87.6 |
| 4 | 125.9 | 0.683 | 86.0 |
| 5 | 136.0 | 0.621 | 84.1 |
| TV | 1,997 | 0.621 | 1,240 |
| **EV** | | | **$1,677.8M** |

---

## 🔗 Connected Concepts

- [[Time Value of Money]] — the mathematical foundation
- [[WACC]] — the discount rate input
- [[CAPM]] — how to compute cost of equity for WACC
- [[Comparable Company Analysis]] — market-based alternative
- [[LBO Model]] — PE-specific valuation
- [[Terminal Value]] — the most sensitive assumption

---

## 🏫 School Context

- **Wharton** (FNCE 236): Extremely rigorous DCF with full sensitivity frameworks
- **Columbia**: Value Investing program uses DCF with heavy margin of safety cushions (Graham tradition)
- **HBS**: Taught via cases; emphasis on *judgment* in assumptions, not mechanics
- **Booth**: DCF linked to efficient market debate — when does intrinsic value diverge from price?

---

*← [[📊 Finance MOC]] | Related: [[WACC]] · [[Comparable Company Analysis]] · [[LBO Model]]*
