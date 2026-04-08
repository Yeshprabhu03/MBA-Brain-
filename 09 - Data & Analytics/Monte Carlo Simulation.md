---
title: Monte Carlo Simulation
tags: [data-analytics, finance, concept, statistics]
aliases: [Monte Carlo, simulation, scenario analysis, stochastic modeling]
---

# 🎲 Monte Carlo Simulation

> **Definition**: A computational technique that uses repeated random sampling to obtain numerical results — modeling the probability distribution of outcomes when inputs are uncertain. Instead of a single "base case" estimate, it shows a range of possible outcomes and their likelihoods.

*Named after the Monte Carlo casino in Monaco — reflecting the role of randomness*
*Used in: Finance, operations, supply chain, project management, risk assessment*

---

## 🔑 The Core Idea

**Traditional analysis problem**: Inputs (growth rate, margins, market size) are uncertain, but we plug in a single "best estimate" and get one output.

**Monte Carlo's solution**: Define inputs as *probability distributions*, then simulate thousands of random draws to build a distribution of outcomes.

```
TRADITIONAL:
Single point estimate → Single output (DCF value = $52/share)

MONTE CARLO:
Revenue growth = N(12%, σ=4%)  ┐
EBITDA margin  = N(22%, σ=3%)  ├─→ Run 10,000 simulations
WACC           = N(9%, σ=1%)   ┘
                                
Result: Distribution of outcomes
→ Mean = $52/share
→ 10th percentile = $38/share (downside)
→ 90th percentile = $67/share (upside)
→ P(value > $60) = 28%
```

---

## 🛠️ How to Run a Monte Carlo

### Step 1: Build the Base Model
Create your spreadsheet model (DCF, project plan, etc.) with clear input cells.

### Step 2: Define Input Distributions
For each uncertain input, choose a distribution type:

| Distribution | When to Use | Example |
|-------------|------------|---------|
| **Normal** | Symmetric uncertainty | Revenue growth rate |
| **Triangular** | Min/most likely/max known | Project duration |
| **Uniform** | Equal probability in range | Commodity price |
| **Log-normal** | Strictly positive, right-skewed | Stock prices |
| **Discrete** | Specific scenarios | Regulatory outcomes (0/1) |

### Step 3: Define Correlations
Inputs often move together (e.g., if growth is high, margins are probably better too). Need to specify correlations between inputs.

### Step 4: Run Simulations
- Typically 1,000–100,000 iterations
- Tools: **@Risk** (Excel plugin), **Crystal Ball**, **Python NumPy/SciPy**, **R**

### Step 5: Interpret Output Distribution
- Mean / Median outcome
- Standard deviation (spread)
- Percentiles (P10, P50, P90)
- Probability of specific outcomes (P(NPV > 0))

---

## 📊 Business Applications

### 1. DCF Valuation Under Uncertainty

Input uncertainty:
- Revenue growth rate: N(8%, 3%)
- EBIT margin: N(15%, 2%)
- Terminal growth rate: N(2.5%, 0.5%)
- WACC: N(9%, 1%)

Output: Distribution of equity value per share → more honest "bull/base/bear" case than point estimate.

### 2. Project Risk Assessment (PMO)
- Project duration inputs are uncertain (construction, software dev)
- Monte Carlo gives probability that project finishes by a date, within budget
- Outputs: P80 (budget that has 80% probability of not being exceeded)

### 3. Supply Chain Risk
- Demand uncertainty, supplier lead time variability, yield uncertainty
- Monte Carlo shows inventory stockout probability at different safety stock levels

### 4. Option Pricing (Black-Scholes)
- Underlying asset prices follow geometric Brownian motion
- Monte Carlo simulates price paths → values path-dependent options (Asian, barrier)

---

## 🧮 Simple Python Example

```python
import numpy as np

# Model: Simple DCF with uncertain growth and WACC
np.random.seed(42)
n = 10_000

# Input distributions
revenue_growth = np.random.normal(0.10, 0.03, n)  # 10% mean, 3% st dev
ebitda_margin  = np.random.normal(0.20, 0.02, n)  # 20% mean, 2% st dev
wacc           = np.random.normal(0.09, 0.01, n)  # 9% mean, 1% st dev
terminal_growth = 0.025  # fixed

# Year 1 EBITDA
base_revenue = 100  # $100M
ebitda = base_revenue * (1 + revenue_growth) * ebitda_margin

# Simplified terminal value
terminal_value = ebitda / (wacc - terminal_growth)
ev = ebitda / (1 + wacc) + terminal_value / (1 + wacc)

# Results
print(f"Mean EV: ${ev.mean():.1f}M")
print(f"P10 EV:  ${np.percentile(ev, 10):.1f}M")
print(f"P90 EV:  ${np.percentile(ev, 90):.1f}M")
print(f"P(EV > $300M): {(ev > 300).mean():.1%}")
```

---

## ⚠️ Limitations

| Limitation | Caution |
|-----------|---------|
| GIGO | Garbage in, garbage out — quality of distributions matters |
| Correlation structure hard to model | Ignoring correlations understates tail risk |
| Black swans not captured | Historical distributions miss unprecedented events |
| False precision | 10,000 simulations look rigorous but depend on assumptions |

---

## 🔗 Connected Concepts

- [[DCF Valuation]] — Monte Carlo makes DCF probabilistic
- [[A-B Testing]] — Both statistical; A/B tests reality, Monte Carlo models uncertainty
- [[Regression Analysis]] — Can use regression outputs as Monte Carlo inputs
- [[Break-Even Analysis]] — Monte Carlo shows probability of hitting break-even
- [[WACC]] — Key uncertain input in financial Monte Carlo

---

*← [[📉 Data & Analytics MOC]] | Related: [[DCF Valuation]] · [[Regression Analysis]] · [[WACC]]*
