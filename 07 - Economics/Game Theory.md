---
title: Game Theory
tags: [economics, decision-making, concept, strategy]
aliases: [Nash Equilibrium, Prisoner's Dilemma]
---

# 🎲 Game Theory

> **Definition**: The mathematical study of strategic decision-making, where the optimal outcome for you depends not only on your actions, but upon the choices made by others—who are also acting in their own self-interest.

*A highly mathematical discipline integrated into advanced Microeconomics.*

---

## 🛠️ When to Use It

- **Pricing Wars**: Deciding whether to slash prices to gain market share, knowing your competitor will likely match your cut.
- **Spectrum/Ad Auctions**: Determining how to bid for Google Ad placements or government 5G spectrum when you don't know the budgets of your competitors.
- **Oligopoly Strategy**: When there are only 2 or 3 players in a market (e.g., Airbus vs. Boeing), and every strategic move induces a direct counter-move.

---

## 🔑 The Core Models

### 1. The Prisoner's Dilemma
Two suspects are arrested. They are interrogated separately. 
- If both stay silent (Cooperate), they each get 1 year in jail.
- If both betray each other (Defect), they each get 3 years.
- If Player A defects and Player B stays silent, A goes free and B gets 5 years.

**The Result**: The rational choice for an individual is always to Defect (it's the *Dominant Strategy*). Therefore, both defect and get 3 years. **Conclusion**: Rational individual behavior often leads to a suboptimal collective outcome.

### 2. Nash Equilibrium
Named after John Nash. A situation where no player has an incentive to change their strategy, *given the strategy chosen by the other player*. In the Prisoner's Dilemma, both defecting is the Nash Equilibrium. 

---

## 📊 Worked Example: Airline Pricing

Imagine American Airlines (AA) and Delta are the only carriers on a route. Fares are $500. Both are making $10M in profit.

| | Delta Keeps at $500 | Delta Drops to $300 |
|---|---|---|
| **AA Keeps at $500** | Both make $10M | AA makes $2M, Delta makes $15M |
| **AA Drops to $300** | AA makes $15M, Delta makes $2M | Both make $5M |

- **AA's Logic**: "If Delta keeps prices high, I should drop mine to steal all the customers and make $15M. If Delta drops prices, I *must* drop mine or I will lose all my customers and make only $2M."
- **Delta's Logic**: Exactly the same.
- **The Outcome**: Both airlines drop prices to $300. Both make $5M. They destroyed collective value because they couldn't securely collude.

---

## ⚠️ Common Mistakes

- **Assuming Single-Turn Games**: The tragic outcome of the Prisoner's Dilemma changes drastically if the game is played repeatedly infinitely ("Iterated Prisoner's Dilemma"). In repeated games, players learn to cooperate because the threat of future retaliation enforces good behavior.
- **Assuming Rationality**: Humans are not perfectly rational perfectly calculating machines; behavioral economics proves we act on emotion, spite, and incomplete information.
- **Ignoring Asymmetric Payoffs**: In standard examples, the matrix is symmetric. In reality, a massive incumbent might survive a price war that bankrupts a smaller player, changing the dominant strategy.

---

## 🎯 When Would I Use This?

1. **Strategic Pricing Committee**: "If we introduce a massive holiday discount, Game Theory indicates that Target and Walmart will instantly match our price within 24 hours. Therefore, we will not gain market share, we will only destroy our collective profit pool. Do not discount."
2. **Supplier Negotiations**: "We are entering a bargaining situation with an exclusive supplier. We must model their payoffs and figure out their 'reservation price' to push the negotiation right to their indifference point without causing a walkout."
3. **M&A Bidding War**: "We are in a sealed-bid auction against a rival firm to buy a target company. We must apply game theory to ensure we don't fall victim to the 'Winner's Curse' (overpaying simply to win the auction)."

---

## 🔗 Connected Concepts

- [[Pricing Strategy]]: The core business area where game theory is most often applied.
- [[Behavioral Economics]]: The antithesis to strict game theory, explaining how irrational humans actually behave.
- [[Porter's Five Forces]]: "Industry Rivalry" is essentially an assessment of the game theory dynamics between existing competitors.
- [[Blue Ocean Strategy]]: The attempt to escape Game Theory entirely by creating a market space where there are no competitors to play against.
- [[First Principles Thinking]]: Breaking down a competitor's fundamental incentive structure to predict their next move.
- [[Agency Theory]]: A specialized "game" played between shareholders and management.

---

*← [[📊 Economics MOC]] | ← [[🔧 Frameworks MOC]]*
