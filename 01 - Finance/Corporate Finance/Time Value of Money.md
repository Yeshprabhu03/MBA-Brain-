---
title: Time Value of Money
tags: [finance, concept, corporate-finance, #concept]
aliases: [TVM, PV, NPV basics]
---

# ⏳ Time Value of Money (TVM)

> **Core Principle**: A dollar today is worth more than a dollar in the future because money today can be invested to earn a return.

*Covered at: All MBA programs — typically Week 1 of Finance*

---

## 🔑 The Intuition

Money has a **time cost**. If someone owes you $1,000, getting it today is strictly better than getting it in a year — because you can invest $1,000 today and have more than $1,000 by next year.

This is why we **discount** future cash flows to their **present value** when making decisions.

---

## 📐 Core Formulas

### Future Value (FV)
$$FV = PV \times (1 + r)^n$$

- `PV` = Present Value
- `r` = interest rate per period
- `n` = number of periods

**Example**: $1,000 invested at 8% for 5 years → `1,000 × (1.08)^5 = $1,469`

### Present Value (PV)
$$PV = \frac{FV}{(1 + r)^n}$$

**Example**: What's $1,469 in 5 years worth today at 8%? → `1,469 / (1.08)^5 = $1,000`

### Net Present Value (NPV)
$$NPV = \sum_{t=0}^{n} \frac{CF_t}{(1 + r)^t}$$

- Accept a project if **NPV > 0**
- Reject if **NPV < 0**
- NPV = value created for shareholders

### Perpetuity
$$PV = \frac{C}{r}$$

**Example**: $100/year forever at 5% discount rate = `100/0.05 = $2,000`

### Growing Perpetuity (Gordon Growth Model)
$$PV = \frac{C}{r - g}$$

---

## 💡 Key Concepts

### Why the Discount Rate Matters
The choice of discount rate is *everything* in valuation:
- Low rate → high PV (future cash flows are valuable)
- High rate → low PV (future is heavily discounted)
- Companies use [[WACC]] as their discount rate for projects

### Rule 72
A quick mental math shortcut:
$$\text{Years to double} \approx \frac{72}{r}$$

At 8%: money doubles in ~9 years. At 6%: ~12 years.

### Annuity
A stream of equal cash flows for `n` periods:
$$PV_{annuity} = C \times \frac{1 - (1+r)^{-n}}{r}$$

---

## 📊 Decision Rules

| Investment Rule | Criterion | Notes |
|----------------|-----------|-------|
| NPV | NPV > 0 | Theoretically best rule |
| IRR | IRR > hurdle rate | Can mislead with non-normal CFs |
| Payback Period | PB < threshold | Ignores time value (bad!) |
| Discounted Payback | DPB < threshold | Better than simple payback |
| Profitability Index | PI > 1 | Useful for capital rationing |

---

## 🚫 Common Mistakes

1. **Using nominal CFs with real rates** (or vice versa) — be consistent
2. **Forgetting the terminal value** in DCF models
3. **Using wrong n** — make sure periods match the discount rate frequency
4. **Adding incremental cash flows incorrectly** — only incremental matters

---

## 🔗 Connected Concepts

- [[DCF Valuation]] — applies TVM to entire companies
- [[WACC]] — the discount rate for most corporate decisions
- [[CAPM]] — how to derive the cost of equity
- [[Capital Structure]] — how financing choices affect value
- [[Options and Derivatives]] — derivatives pricing uses risk-neutral discounting

---

## 🏫 School Context

- **HBS Finance I**: Taught via case studies; emphasis on *which* discount rate to choose, not the mechanics
- **Wharton FNCE 611**: Heavily mathematical; derives PV rigorously from first principles
- **Booth**: Context of Chicago School — markets are efficient, so TVM is purely mathematical
- **Columbia**: Emphasis on Benjamin Graham's margin of safety — conservative discounting

---

*← [[📊 Finance MOC]] | Related: [[DCF Valuation]] · [[WACC]] · [[NPV vs IRR]]*
