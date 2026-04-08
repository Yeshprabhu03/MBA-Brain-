---
title: Supply Chain Management
tags: [operations, concept, supply-chain]
aliases: [SCM, supply chain, logistics]
---

# 🚚 Supply Chain Management

> **Definition**: The management of the flow of goods and services, including all processes that transform raw materials into final products, from supplier to end customer.

*Key courses: **HBS TOM, Wharton OIDD, MIT SCM (bonus)***

---

## 🗺️ The Supply Chain Structure

```
[Raw Material Suppliers]
        ↓
[Component Manufacturers]
        ↓
[Manufacturers / Assemblers]
        ↓
[Distributors / Wholesalers]
        ↓
[Retailers / Direct-to-Consumer]
        ↓
[End Customers]
```

Each arrow represents **flows of**: Materials + Information + Finances

---

## 🔑 Core Trade-Off: Efficiency vs. Responsiveness

| Strategy | Efficiency Focus | Responsiveness Focus |
|----------|-----------------|---------------------|
| **Goal** | Lowest cost | React fast to demand |
| **Supply** | Reliable, high-volume suppliers | Flexible, redundant suppliers |
| **Inventory** | Minimal (JIT) | Buffer stock |
| **Lead time** | Acceptable longer leads | Short, fast leads |
| **Best for** | Stable, predictable demand | Volatile, fashion, seasonal |
| **Example** | Toyota (stable products) | Zara (fast fashion) |

---

## 📦 Inventory Management

### Economic Order Quantity (EOQ)
$$EOQ = \sqrt{\frac{2DS}{H}}$$

| Variable | Meaning |
|---------|---------|
| D | Annual demand |
| S | Ordering cost per order |
| H | Holding cost per unit per year |

**EOQ finds the order size that minimizes total inventory cost** (ordering cost + holding cost).

### Safety Stock
$$SS = z \times \sigma_{demand} \times \sqrt{LT}$$

- `z` = service level z-score (e.g., z=1.65 for 95%)
- `σ_demand` = standard deviation of demand
- `LT` = lead time

**Reorder Point** = Lead Time Demand + Safety Stock

### Just-In-Time (JIT)
- Zero inventory philosophy from Toyota
- Receive materials only when needed in production
- Requires tight supplier relationships and predictable demand
- **Risk**: Supply disruptions (COVID-19 exposed JIT vulnerabilities)

---

## 🌊 The Bullwhip Effect

**Definition**: Small fluctuations in consumer demand cause amplified swings in orders further up the supply chain.

```
Consumer buys 100 units → Retailer orders 120 → Wholesaler orders 150 → Manufacturer orders 200
```

**Causes**:
- Demand forecast errors
- Order batching (ordering weekly instead of daily)
- Price fluctuations (forward buying)
- Rationing game (shortage hoarding)

**Solutions**:
- Vendor-Managed Inventory (VMI)
- Sharing POS data with suppliers (CPFR)
- Everyday low pricing (eliminate promotions that cause hoarding)
- EDI / real-time information sharing

---

## 🌍 Global Supply Chain Strategy

### Offshoring vs. Reshoring vs. Nearshoring

| Strategy | Definition | Trend |
|---------|-----------|-------|
| **Offshoring** | Production in low-cost distant country | Declining post-COVID |
| **Reshoring** | Bringing production home | Growing (chips, pharma) |
| **Nearshoring** | Moving to nearby countries | Growing (Mexico for US) |

**Drivers of reshoring** (post-2020):
- COVID supply chain disruptions
- Geopolitical risk (China tension)
- Rising labor costs in Asia
- "Made in USA" brand value
- Inflation Reduction Act incentives

---

## 🔄 Case: Zara's Supply Chain Advantage

Zara (Inditex) reinvented fashion supply chains:

| Traditional Retailer | Zara |
|---------------------|------|
| Plan 6–12 months ahead | Design to shelf in 2–4 weeks |
| Large batch orders | Small batch orders |
| Low cost manufacturing | Spain/Portugal manufacturing (near) |
| Rarely stockouts managed | Intentional scarcity |
| Price markdowns | Almost no markdowns |

**Result**: Zara carries 1/10th the inventory of peers, at higher margins, with 30% less waste.

---

## 🔗 Connected Concepts

- [[Lean Manufacturing]] — Toyota's supply chain philosophy
- [[Theory of Constraints]] — Bottleneck management in supply
- [[Bullwhip Effect]] — Demand amplification problem
- [[Make vs. Buy Decision]] — Vertical integration choice
- [[Global Supply Chain Risk]] — Resilience planning

---

*← [[⚙️ Operations MOC]] | Related: [[Lean Manufacturing]] · [[Theory of Constraints]] · [[Bullwhip Effect]]*
