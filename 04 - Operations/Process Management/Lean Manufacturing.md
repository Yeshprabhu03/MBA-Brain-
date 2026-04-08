---
title: Lean Manufacturing
tags: [operations, framework, concept]
aliases: [Toyota Production System, TPS, lean, waste elimination]
---

# 🏭 Lean Manufacturing

> **Definition**: A systematic method for waste elimination within a manufacturing system that also takes into account waste created through overburden and unevenness in workloads. Based on the Toyota Production System (TPS).

*Coined by: James Womack, Daniel Jones & Daniel Roos — "The Machine That Changed the World" (1990)*
*Origin: Toyota (Taiichi Ohno, Shigeo Shingo) — developed 1950s–80s*
*Key course: **HBS TOM, Wharton OIDD***

---

## 🔑 The Five Lean Principles (Womack & Jones)

1. **Specify Value**: Define value from the *customer's* perspective — only what the customer will pay for
2. **Map the Value Stream**: Identify all steps in the production process; separate value-adding from waste
3. **Create Flow**: Eliminate interruptions so the product flows continuously to the customer
4. **Establish Pull**: Only produce what the customer has demanded (vs. push/forecast-based production)
5. **Seek Perfection**: Continuously improve (Kaizen) — perfection is the north star, not the destination

---

## 🗑️ The 8 Wastes (DOWNTIME)

Toyota identified **Muda** (waste) as the enemy of efficiency:

| Waste | Description | Example |
|-------|-------------|---------|
| **D**efects | Products that require rework or scrapping | Wrong assembly requiring teardown |
| **O**verproduction | Making more than needed right now | Building to forecast, not demand |
| **W**aiting | Idle time when process stalls | Machine waiting for parts |
| **N**on-utilized talent | Untapped employee ideas and skills | Operators not in process improvement |
| **T**ransportation | Unnecessary movement of materials | Moving WIP across a large plant |
| **I**nventory | Excess material or WIP held | Weeks of raw material buffer |
| **M**otion | Unnecessary human movement | Walking to retrieve tools |
| **E**xtra processing | More work than customer values | 6-coat paint when 3 suffices |

---

## 🔧 Core Lean Tools

### 5S Workplace Organization
| S | Japanese | Meaning |
|---|---------|---------|
| Sort | Seiri | Remove what's not needed |
| Set in order | Seiton | Place for everything, everything in its place |
| Shine | Seiso | Clean and inspect |
| Standardize | Seiketsu | Document and make standard |
| Sustain | Shitsuke | Maintain discipline |

### Kanban (Visual Pull System)
- Cards or signals authorize production/replenishment
- Nothing is made without a Kanban signal (demand pull)
- WIP is physically limited by card count
- Used by: Toyota, Amazon warehouses, software teams (Jira boards)

### Poka-Yoke (Error Proofing)
- Design the process so mistakes are *impossible* to make
- Examples: USB-A only fits one way (but USB-C doesn't need to) · ATMs return card before cash to prevent card-forgetting

### Value Stream Mapping (VSM)
- Map every step from raw material → customer delivery
- Identify where time is spent (value-add vs. wait)
- Calculate: **Process time** vs. **Lead time** (the gap is waste)

### Kaizen (Continuous Improvement)
- Small, incremental improvements by frontline workers
- Toyota: Every worker has authority to stop the production line (Andon cord)
- "Kaizen events": Focused week-long improvement bursts

### Takt Time
$$\text{Takt Time} = \frac{\text{Available Production Time}}{\text{Customer Demand Rate}}$$

Takt = "pace" of production to meet demand exactly.
- If customers buy 100 units/shift (8 hrs), takt time = 8 hrs/100 = 4.8 min/unit
- All processes must be designed around takt time

---

## 📊 Lean vs. Traditional Manufacturing

| Dimension | Traditional (Push) | Lean (Pull) |
|-----------|-------------------|-------------|
| Production trigger | Forecast | Customer order |
| Batch size | Large (economies of scale) | Small (flexibility) |
| Inventory | High buffers | Minimal |
| Quality | Inspect at end | Built into process (jidoka) |
| Layout | Functional (departments) | Flow/cellular |
| Improvement | Top-down engineering | All employees (Kaizen) |

---

## 🌍 Beyond Manufacturing: Lean Thinking

Lean has spread far beyond factories:
- **Lean Healthcare**: Virginia Mason Medical Center reduced OR delays, costs
- **Lean Startup**: Apply lean principles to startup product development
- **Lean Accounting**: Match financial reporting to value streams
- **Lean Software**: Agile is heavily influenced by lean thinking

---

## 🔗 Connected Concepts

- [[Theory of Constraints]] — Goldratt's complementary bottleneck approach
- [[Six Sigma]] — Quality-focused complement to lean (Lean Six Sigma)
- [[Supply Chain Management]] — Lean revolutionized supply chains (JIT)
- [[Lean Startup]] — Eric Ries applied lean to startups

---

*← [[⚙️ Operations MOC]] | Related: [[Theory of Constraints]] · [[Six Sigma]] · [[Supply Chain Management]]*
