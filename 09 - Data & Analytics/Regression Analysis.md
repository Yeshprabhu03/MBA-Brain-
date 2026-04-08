---
title: Regression Analysis
tags: [data-analytics, statistics, concept]
aliases: [OLS, linear regression, multiple regression, statistical modeling]
---

# 📈 Regression Analysis

> **Definition**: A statistical method for estimating the relationships between a dependent variable (outcome) and one or more independent variables (predictors). It is the foundation of quantitative business analysis.

*Key courses: **Wharton STAT 613, Booth BUSN 41100, HBS Analytics***

---

## 🔑 The Core Intuition

**Question regression answers**: "How does Y change when X changes, *holding everything else constant*?"

This "holding everything else constant" (ceteris paribus) is what makes regression powerful — it controls for confounders.

---

## 📐 Simple Linear Regression

$$Y = \beta_0 + \beta_1 X + \varepsilon$$

| Term | Meaning |
|------|---------|
| `Y` | Dependent variable (what we're predicting) |
| `X` | Independent variable (the predictor) |
| `β₀` | Intercept (Y when X = 0) |
| `β₁` | Slope (change in Y for 1-unit change in X) |
| `ε` | Error term (unexplained variation) |

**Example**: Predicting Sales from Advertising Spend
$$\text{Sales} = 50 + 3.2 \times \text{AdSpend} + \varepsilon$$

Interpretation: Each additional $1K in ad spend → $3.2K more in sales.

---

## 📊 Multiple Regression

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_n X_n + \varepsilon$$

Controls for multiple variables simultaneously:
$$\text{Revenue} = 100 + 2.5 \cdot \text{AdSpend} + 1.8 \cdot \text{Price} - 0.3 \cdot \text{Competition} + \varepsilon$$

---

## 📏 Evaluating a Regression

### R² (R-squared) — Goodness of Fit
$$R^2 = 1 - \frac{SS_{residual}}{SS_{total}}$$

- R² = 0: Model explains nothing
- R² = 1: Model explains everything perfectly
- R² = 0.72: Model explains 72% of variation in Y

**Warning**: R² always increases when adding variables → use **Adjusted R²** for multiple regression.

### Statistical Significance (p-value)
- p < 0.05: The coefficient is statistically significant → X reliably predicts Y
- p > 0.05: Could be noise

### Confidence Intervals
- 95% CI: The true β₁ lies in this range with 95% confidence
- Narrow CI = more precise estimate

---

## ⚠️ Assumptions (OLS)

The Ordinary Least Squares (OLS) estimator requires:

| Assumption | If Violated |
|-----------|-------------|
| **Linearity** | Use polynomial or log transformation |
| **Independence of errors** | Autocorrelation in time series data → use time series models |
| **Homoscedasticity** (constant variance) | Heteroscedasticity → use robust standard errors |
| **No multicollinearity** | Correlated predictors → unstable coefficients |
| **Normality of errors** | Mostly needed for small samples |

---

## 🔢 Logistic Regression (Binary Outcomes)

When Y is binary (0 or 1), use **logistic regression**:
$$P(Y=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X)}}$$

- Outputs a **probability** between 0 and 1
- Common in: Credit default prediction, customer churn, fraud detection, disease diagnosis

---

## 💼 Business Applications

| Business Problem | Regression Type | Y Variable |
|----------------|----------------|-----------|
| Sales forecasting | Multiple regression | Revenue |
| Price elasticity | Log-log regression | Quantity sold |
| Customer churn | Logistic regression | Churned (0/1) |
| House pricing model | Multiple regression | Home price |
| Ad attribution | Multiple/ridge regression | Conversions |
| Credit scoring | Logistic regression | Default (0/1) |

---

## 🧠 Key Business Interpretation Rules

1. **Coefficients** show marginal effects — the impact of one variable *holding all others fixed*
2. **Signs matter**: Positive β = positive relationship, negative β = negative
3. **Scale matters**: Compare standardized coefficients for relative importance
4. **Causation ≠ correlation**: Regression shows association; need good design for causality ([[A/B Testing]])
5. **Out-of-sample validity**: Always test on held-out data

---

## 🔗 Connected Concepts

- [[A/B Testing]] — When you need causal inference, not just correlation
- [[Monte Carlo Simulation]] — Simulation-based complement to regression
- [[Hypothesis Testing]] — p-values and confidence intervals underlying regression
- [[Decision Trees]] — Non-linear alternative for prediction
- [[Behavioral Economics Overview]] — Regression can confirm behavioral biases

---

*← [[📉 Data & Analytics MOC]] | Related: [[A/B Testing]] · [[Hypothesis Testing]] · [[Decision Trees]]*
