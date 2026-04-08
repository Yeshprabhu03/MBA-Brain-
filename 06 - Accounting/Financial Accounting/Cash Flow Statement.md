---
title: Cash Flow Statement
tags: [accounting, financial-accounting, concept]
aliases: [statement of cash flows, operating cash flow, FCF, free cash flow]
---

# 💸 Cash Flow Statement

> **Definition**: A financial statement that shows how cash moves into and out of a business over a period of time, classified into operating, investing, and financing activities. **Cash is king** — net income can be manipulated, but cash flows are harder to fake.

*The most important of the three financial statements for credit analysis and DCF valuation.*

---

## 🔑 Why Cash Flow ≠ Net Income

**Accrual accounting** lets companies record revenue when earned (not received) and expenses when incurred (not paid). This creates a gap:

| Scenario | Net Income impact | Cash impact |
|---------|-----------------|-------------|
| Sell on credit ($100K) | Revenue recognized now | Cash comes later |
| Buy inventory ($50K) | No P&L impact yet | Cash gone now |
| Depreciate equipment ($20K) | P&E expense recognized | No cash leaves |
| Receive advance payment ($30K) | No revenue yet | Cash in now |

**Result**: A company can be **profitable but cash-flow negative** (growing fast, bad collections) or **lack income but cash-flow positive** (asset sales, depreciation-heavy). Always read both.

---

## 📐 Three Sections of the Cash Flow Statement

```
─────────────────────────────────────────
A. OPERATING ACTIVITIES
   Net Income                       +
   + Depreciation & Amortization    +  (non-cash add-back)
   + Changes in Working Capital:
       Δ Accounts Receivable         − (increasing AR uses cash)
       Δ Inventory                   − (increasing inventory uses cash)
       Δ Accounts Payable            + (increasing AP = cash cushion)
─────────────────────────────────────────
= Cash from Operations (CFO)

B. INVESTING ACTIVITIES
   Capital Expenditures (CapEx)      − (buying PP&E)
   Acquisitions                      −
   Asset sales                       +
   Purchase of investments           −
─────────────────────────────────────────
= Cash from Investing (CFI)         [Usually negative for growing companies]

C. FINANCING ACTIVITIES
   Debt issuance                     +
   Debt repayment                    −
   Stock issuance                    +
   Share buybacks                    −
   Dividends paid                    −
─────────────────────────────────────────
= Cash from Financing (CFF)

NET CHANGE IN CASH = CFO + CFI + CFF
```

---

## 🔢 Key Cash Flow Metrics

### Free Cash Flow (FCF) — The Core Valuation Input

$$\text{FCF} = \text{Cash from Operations} - \text{Capital Expenditures (CapEx)}$$

FCF represents the actual cash the business generates — available for debt repayment, dividends, buybacks, or acquisitions.

**Alternative formula** (used in DCF):
$$\text{FCFF} = \text{EBIT} \times (1-t) + D\&A - \Delta \text{Working Capital} - \text{CapEx}$$

### CapEx Types
- **Maintenance CapEx**: Just keeping existing assets running
- **Growth CapEx**: Investing for future revenue growth

**Warren Buffett's "Owner Earnings"** = Net Income + D&A − Maintenance CapEx

---

## 📊 Signs of Quality Cash Flow

| Good Sign | Bad Sign |
|-----------|---------|
| CFO consistently > Net Income | CFO < Net Income (aggressive revenue recognition) |
| Growing FCF over time | Negative FCF + no path to profitability |
| Low CapEx intensity (high FCF conversion) | CapEx-heavy with thin margins |
| Working capital needs declining | AR growing faster than revenue |
| Financing from operations, not debt | Funding operations with constant debt issuance |

---

## 🏆 Cash Flow in Valuation

[[DCF Valuation]] is built entirely on projected unlevered **FCF**:

$$\text{Enterprise Value} = \sum_{t=1}^{n} \frac{FCF_t}{(1+WACC)^t} + \frac{\text{Terminal Value}}{(1+WACC)^n}$$

**The CFO → FCF → DCF chain**: Understanding cash flow statements is the prerequisite for DCF modeling.

---

## 🔗 Connected Concepts

- [[Income Statement]] — Net income is the starting point of the cash flow statement
- [[Balance Sheet]] — Cash is an asset; statement reconciles beginning and ending cash
- [[DCF Valuation]] — FCF is the key input
- [[WACC]] — FCF discounted at WACC to get enterprise value
- [[Working Capital Management]] — Working capital changes are major cash flow drivers

---

*← [[📒 Accounting MOC]] | Related: [[Income Statement]] · [[Balance Sheet]] · [[DCF Valuation]]*
