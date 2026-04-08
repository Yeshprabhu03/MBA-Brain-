---
title: Terminal Value
tags: [finance, valuation, concept]
---

# ♾️ Terminal Value

> **Definition**: The estimated value of a business beyond the explicit forecast period in a Discounted Cash Flow (DCF) model. It represents the present value of all future cash flows stretching into perpetuity.

---

## 🤔 Why Terminal Value Matters

In a [[DCF Valuation]], you typically project discrete cash flows for 5 to 10 years. Because companies are assumed to operate indefinitely (a "going concern"), you must capture the value generated *after* that forecast period. 

Crucially, **Terminal Value typically represents 60–80% of the total DCF enterprise value**. Because it heavily weights the final valuation, even minor tweaks to terminal assumptions can drastically swing your conclusion.

---

## 📐 Two Methods of Calculation

There are two primary ways to calculate Terminal Value:

### 1. Gordon Growth Model (Perpetuity Growth)
This method assumes the company will grow its free cash flow at a constant rate forever.

**Formula**: 
$$TV = \frac{FCF_{n+1}}{WACC - g}$$

- **$FCF_{n+1}$** = Expected Free Cash Flow one year *after* the Explicit Forecast Period (Year n + 1)
- **WACC** = Weighted Average Cost of Capital (Discount Rate)
- **$g$** = Terminal Growth Rate

*Rule of thumb for $g$*: It should typically align with long-term macroeconomic growth (e.g., inflation or GDP growth, typically 2-3%). If $g >$ GDP growth, you are assuming the company will eventually become larger than the entire economy!

### 2. Exit Multiple Method
This method assumes the business will be sold at the end of the forecast period for a multiple of some financial metric (usually EBITDA).

**Formula**:
$$TV = Final Year EBITDA \times Exit Multiple$$

*Rule of thumb for the Exit Multiple*: Usually based on current comparable companies (**[[Comparable Company Analysis]]**) or recent precedent transactions. 

---

## ⚠️ Key Assumptions & Sensitivity

Because TV is such a massive driver of total value, bankers build **Sensitivity Tables** around it.
- **In Gordon Growth**: Varying WACC and Long-term Growth ($g$).
- **In Exit Multiple**: Varying the final year EBITDA and the chosen Multiple.

### Common Mistakes & Stress-Testing
1. **Aggressive Growth Rates**: Using a 5% perpetuity growth rate is mathematically dangerous and economically unrealistic.
2. **Ignoring the Implied Multiple**: If you use the Gordon Model, you should divide the resulting TV by Year $n$ EBITDA to find the *implied* exit multiple. If it's wildly different from industry averages, your assumptions are flawed.
3. **Mismatched Risk**: Ensure the WACC reflects the stabilized, mature risk profile of the company in the terminal state.

---

## 🔗 Connected Concepts
- [[DCF Valuation]]
- [[WACC]]
- [[EBITDA Multiples]]
- [[Comparable Company Analysis]]

---

## 🏫 School Context
- **Wharton & Booth**: Emphasize the mathematical rigor of the Gordon Growth Model; you will be tested on proving why $g$ must logically be lower than the discount rate.
- **HBS & Columbia**: Lean heavily toward the Exit Multiple method as it is more "market-grounded" and reflects how private equity actually values an exit.

---

*← [[📊 Finance MOC]]*
