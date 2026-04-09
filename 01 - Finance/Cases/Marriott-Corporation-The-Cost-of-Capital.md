---
title: Marriott Corporation - The Cost of Capital
tags: [case-study, finance, corporate-finance, wacc]
company: Marriott Corporation
industry: Hospitality
year: 1988
---

# 🏨 Case Study: Marriott Corporation - The Cost of Capital

## 📋 Case Overview

| Attribute | Detail |
|-----------|--------|
| **Company** | Marriott Corporation |
| **Founded** | 1927 |
| **Key People** | J.W. Marriott, Jr., Dan Cohrs (VP of Project Finance) |
| **Theme** | Hurdle rates, divisional cost of capital, capital structure optimization |
| **Outcome** | Established the standard academic and practitioner approach to calculating WACC for multi-divisional firms. |

---

## 📖 Background

In 1988, Marriott Corporation was a rapidly growing hospitality empire comprised of three distinct divisions:
1. **Lodging (Hotels)**: Capital intensive, heavy real estate.
2. **Contract Services**: Providing food/services to schools and hospitals; asset-light, stable cash flows.
3. **Restaurants**: Fast-food chains and family dining; highly competitive, economically sensitive.

Historically, corporations used a single, company-wide Weighted Average Cost of Capital (WACC) to evaluate all potential projects. However, Dan Cohrs, Marriott's VP of Project Finance, realized that using a single "hurdle rate" was fundamentally flawed. It punished low-risk projects (which were rejected because they couldn't beat the artificially high company WACC) and rewarded high-risk projects (which were accepted easily but didn't adequately compensate for their specific risk). Marriott needed a sophisticated methodology to calculate a distinct cost of capital for *each* division.

---

## 🎯 Central Problems

### 1. The Divisional Hurdle Rate Problem
How do you calculate a discrete WACC for a division that is not public? Because Contract Services doesn't trade on the stock market, you cannot simply look up its stock beta on Bloomberg. 

### 2. Unlevering and Relevering Beta
Different divisions can support different levels of debt. Lodging has hard real estate assets and can support 74% debt. Contract services has no hard collateral and can only support 40% debt. The financial challenge was stripping the effect of debt out of comparable companies, and reapplying Marriott's targeted debt capacity.

### 3. The Risk-Free Rate Selection
Should the company use a short-term Treasury bill or a long-term Treasury bond as the risk-free rate when calculating the Cost of Equity via the Capital Asset Pricing Model (CAPM)?

---

## 🔬 Strategic Analysis

### Framework Application 1: [[WACC]] Calculation Methodology
Marriott's methodology became the gold standard for project finance:

| Step | Action | Business Logic |
|------|--------|----------------|
| **1. Identify Comps** | Find pure-play public companies that operate *only* in the specific division's industry (e.g., Hilton for Lodging, McDonald's for Restaurants). | You must use market proxy data since the division has no standalone stock price. |
| **2. Unlever Beta** | Calculate the unlevered beta (asset beta) for all comps using the formula: $β_{unlevered} = β_{levered} / (1 + (1-t)(D/E))$. | This strips away the financial risk (leverage) of the peers, leaving only the pure business risk. |
| **3. Average & Relever** | Take the average unlevered beta of the comps, and relever it using *Marriott's target debt capacity for that specific division*. | Reattaches Marriott's unique financial structure to the industry's base business risk. |
| **4. Apply CAPM** | Plug the new divisional beta into CAPM. | Yields the precise Cost of Equity for that division. |

### Framework Application 2: [[Capital Structure]] Optimization
Marriott strategically mismatched its debt to its assets. They utilized massive amounts of cheap debt to build hotels, but then pursued an "originate-and-sell" model where they sold the real estate to investors and kept the lucrative, high-margin management contracts.

---

## 📈 Key Metrics (Marriott 1988)

| Metric | Lodging | Contract Services | Restaurants | Corporate |
|--------|---------|-------------------|-------------|-----------|
| **Target Debt Ratio (D/V)** | 74% | 40% | 42% | **60%** |
| **Estimated Division Beta** | ~1.15 | ~0.75 | ~1.05 | **~1.11** |
| **Final WACC** | ~8.5-9.0% | ~10-10.5% | ~10.5-11% | **~9.5%** |

*(Note: Data variations exist based on risk premium assumptions used by students).*

---

## 📝 Key Lessons

1. **Risk Dictates the Hurdle Rate**: Never use a corporate-wide WACC for a multi-business firm. Low-risk divisions will stagnate, and high-risk divisions will consume all capital and destroy value.
2. **Debt Capacity is Derived from Asset Quality**: The Lodging division could safely target 74% leverage because physical real estate provides collateral and stable cash flows. Restaurants cannot support that leverage.
3. **Pure-Play Comparables are Essential**: Finding the true cost of equity requires stripping the leverage out of fundamentally similar public peers to isolate the pure business risk.
4. **Match Debt Duration to Asset Life**: Marriott matched short-term corporate debt with short-term projects, and 10-30 year long-term Treasury rates against long-lived hotel assets.
5. **WACC is an Estimate, Not a Fact**: Small shifts in the assumed Equity Risk Premium (ERP) or the chosen risk-free rate drastically alter the WACC. Valuation requires judgment, not just algebraic precision.

---

## ❓ Discussion Questions

1. If Marriott's corporate overall WACC is 9.5%, and the Lodging division evaluates a project at 9.0%, why is it a massive strategic error to reject it for "failing to beat the corporate average"?
2. Should Marriott use a 1-year Treasury rate, a 10-year Treasury rate, or a 30-year Treasury rate as the risk-free rate ($r_f$) in the CAPM formula? Why?
3. Why is it necessary to use the targeted future capital structure (debt-to-equity ratio) rather than the company's historical or current capital structure when calculating WACC?
4. How do you measure the cost of debt ($r_d$) for a division when the division doesn't issue its own bonds to the public market?
5. The "originate-and-sell" hotel strategy is highly lucrative. How does this strategy impact Marriott's beta and overall risk profile over time?

---

## 🔗 Connected Concepts

- [[WACC]]: The absolute focal point of the case—learning how to synthesize debt and equity costs to find a minimum hurdle rate.
- [[CAPM]]: The Capital Asset Pricing Model used to calculate the Cost of Equity ($r_e$) for the various divisions.
- [[Beta and Systematic Risk]]: Explains why the restaurant division and the lodging division have inherently different sensitivities to macroeconomic shocks.
- [[Capital Structure]]: Driven by the realization that different assets dictate entirely different theoretical debt capacities.
- [[DCF Valuation]]: WACC is the denominator required to discount the future cash flows of Marriott's new hotel projects.
- [[Comparable Company Analysis]]: The technique used to identify pure-play competitors to extract proxy beta numbers.
- [[Risk-Free Rate]]: A core debate in the case regarding which duration of government bonds correctly anchors the CAPM equation.
- [[Agency Theory]]: The underlying reason a division manager might advocate using the "wrong" WACC if it helps their specific bonus structure.

---

*← [[📊 Finance MOC]] | ← [[📚 Case Studies MOC]]*
