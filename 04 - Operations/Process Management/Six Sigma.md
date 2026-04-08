---
title: Six Sigma
tags: [operations, framework, quality, concept]
aliases: [DMAIC, six sigma, quality management, process improvement]
---

# 🎯 Six Sigma

> **Definition**: A data-driven methodology for eliminating defects in any process — from manufacturing to service. The name refers to the statistical goal of producing only 3.4 defects per million opportunities.

*Developed at: Motorola (1986); popularized by Jack Welch at GE (1995)*
*Sigma (σ) = standard deviation. At 6σ, process performance is 6 standard deviations from the mean — near-perfect quality.*

---

## 📊 What Does "Six Sigma" Mean Statistically?

| Sigma Level | Defects Per Million Opportunities | Yield |
|------------|----------------------------------|-------|
| 1σ | 690,000 | 30.9% |
| 2σ | 308,000 | 69.1% |
| 3σ | 66,800 | 93.3% |
| 4σ | 6,210 | 99.38% |
| 5σ | 230 | 99.977% |
| **6σ** | **3.4** | **99.9997%** |

**Context**: Most companies operate at ~3–4σ. Aviation targets 6σ+ for safety-critical systems.

---

## 🔄 The DMAIC Framework

The structured problem-solving methodology for improving existing processes:

### D — Define
*What is the problem and who does it affect?*
- Define the project scope and goals
- Identify customers (internal and external) and their **CTQs** (Critical to Quality requirements)
- Map the process at high level (SIPOC diagram)
- Create project charter

### M — Measure
*How bad is the current performance?*
- Identify key process metrics
- Collect baseline data
- Calculate current sigma level
- Measure system capability (Cp, Cpk)

### A — Analyze
*Why is the problem occurring?*
- Use data to identify **root causes** (not symptoms)
- Tools: Fishbone (Ishikawa) diagram, 5 Whys, Pareto chart
- Hypothesis testing to confirm causes

### I — Improve
*What solutions will fix the root causes?*
- Brainstorm and test solutions
- Pilot the improvement
- Design of experiments (DoE) to optimize
- Implement the solution

### C — Control
*How do we sustain the improvement?*
- Statistical Process Control (SPC) charts
- Control plan and monitoring system
- Standard work procedures
- Hand off to process owner

---

## 🔧 Key Six Sigma Tools

| Tool | Phase | Purpose |
|------|-------|---------|
| SIPOC Diagram | Define | Map Suppliers→Inputs→Process→Outputs→Customers |
| Voice of Customer (VOC) | Define | Capture what customers actually need |
| Pareto Chart (80/20) | Analyze | Identify top defect causes |
| Fishbone/Ishikawa Diagram | Analyze | Root cause brainstorming |
| 5 Whys | Analyze | Drill down to root cause |
| Control Chart | Control | Monitor process over time |
| Process Capability (Cpk) | Measure | How well process meets specifications |
| FMEA | Improve | Failure Modes and Effects Analysis |

---

## 🏅 Six Sigma Roles (Belt System)

| Belt | Training | Scope |
|------|---------|-------|
| **Yellow Belt** | Basic awareness | Project team member |
| **Green Belt** | 2–4 weeks | Part-time project leader |
| **Black Belt** | 4 weeks + project | Full-time improvement leader |
| **Master Black Belt** | Advanced + teaching | Strategy, coaching, program lead |
| **Champion** | Executive sponsor | Strategy alignment, resource authority |

---

## 🔄 Lean Six Sigma

Most organizations combine **Lean** (speed/waste) and **Six Sigma** (quality/variation) into **Lean Six Sigma**:

| Lean | Six Sigma | Combined |
|------|----------|---------|
| Eliminate waste | Reduce variation | Faster + better |
| Speed and flow | Statistical analysis | Comprehensive improvement |
| All 8 wastes | DMAIC framework | DMAIC + waste tools |

---

## 📊 Real Applications

| Industry | Six Sigma Application |
|---------|----------------------|
| **Manufacturing** | GE reduced defects for aircraft engine parts |
| **Healthcare** | Hospital reduces medication errors |
| **Banking** | Reduce loan processing errors/time |
| **Software** | Reduce bug rate in code releases |
| **Retail** | Reduce order fulfillment errors |

**GE under Jack Welch**: Invested $1B in Six Sigma training; estimated $12B in savings over 5 years.

---

## ⚠️ Criticisms

| Critique | Detail |
|---------|--------|
| Not all processes suit it | Innovation cannot be Six Sigma-ized |
| Can create bureaucracy | Heavy documentation burden |
| Optimizes existing; doesn't disrupt | Great for efficiency, not innovation |
| Belt system can become status game | Certifications ≠ results |

---

## 🔗 Connected Concepts

- [[Lean Manufacturing]] — Complementary waste-elimination approach
- [[Theory of Constraints]] — Focuses on bottlenecks vs. Six Sigma's focus on variation
- [[Supply Chain Management]] — Quality affects entire supply chain
- [[Balanced Scorecard]] — Internal process perspective

---

*← [[⚙️ Operations MOC]] | Related: [[Lean Manufacturing]] · [[Theory of Constraints]] · [[Supply Chain Management]]*
