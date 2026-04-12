# Archipelago
**PSEi Portfolio Intelligence Tool** — *coming soon.*

A practical application of the research *Topological Stability and Systemic Fragility of the Philippine Equity Market* by **Graph Gang**, BSM CS3B, Bulacan State University.

---

## Overview

**Archipelago** translates academic graph theory into an interactive tool for understanding and managing structural risk in the Philippine Stock Exchange (PSEi). Where most portfolio tools stop at returns and volatility, Archipelago exposes the *hidden topology* of the market — the connections, communities, and fragility points that determine how shocks actually propagate.
---

## 🌐 Live Demo

[philippine-stocks-network-ja3c.vercel.app/archipelago-app](https://philippine-stocks-network-ja3c.vercel.app/archipelago-app/archipelago_app.html)

---

## Research Foundation

Archipelago is built directly on the empirical findings of our study:

| Metric | Finding |
|---|---|
| **Hub stocks** | ALI, SMPH, URC |
| **Algebraic connectivity (λ₂)** | ≈ 0 *(near-fragile state)* |
| **Connected components** | 14 → **17** after hub removal |
| **Louvain communities** | 16 distinct clusters |
| **Method** | MST + 3-KNN filtering on Pearson correlation distances |

> Removing just **3 hub stocks** increases market fragmentation by **21%**. Archipelago helps investors recognize and avoid this exposure in their own portfolios.

---

## Features

| Module | Function |
|---|---|
| **My Observatory** | Personal portfolio dashboard with topology map, diversification score, and systemic exposure metrics |
| **Portfolio Scanner** | Detects structural risk, community overlap, and hidden correlations in your holdings |
| **Contagion Simulator** | Simulates shock propagation when hub stocks (ALI, SMPH, URC) crash |
| **Diversify Recommender** | Topology-aware stock suggestions that reduce *structural*, not just statistical, risk |
| **Market Health** | Live monitoring of λ₂, MST structure, and sector correlation matrices |
| **Portfolio Topology** | Full PSEi network map — communities, bridge nodes, and isolated stocks |
| **About** | Research methodology and team background |

---

## 🤖 Harris.AI

Every screen is powered by **Harris.AI**, an in-app intelligence layer providing real-time structural analysis, risk synthesis, and mitigation strategies based on each portfolio's topological position within the PSEi network.

---

## Tech Stack

- **HTML / CSS / JavaScript** — Single-file compiled application
- **Tailwind CSS** — Styling
- **Graph Gang research dataset** — PSEi correlation network (2023–2025)

---

## Status

Archipelago is currently a **research prototype**. The current build demonstrates the full user experience using the static dataset from our study.

---

## Future Work

Planned extensions to evolve Archipelago from prototype to production tool:

1. **Live PSEi data integration** via PSE Edge or a third-party market data API for real-time λ₂ and topology updates.
2. **Rolling-window analysis** to track how the network's algebraic connectivity evolves over time and flag fragility transitions early.
3. **Backtesting engine** to validate topology-aware diversification strategies against historical PSEi data.
4. **Expanded Harris.AI** with explainable-AI summaries and personalized rebalancing playbooks.
5. **User authentication & portfolio persistence** so investors can track their topological exposure across sessions.
6. **Cross-market generalization** to apply the same MST + k-NN methodology to ASEAN exchanges (IDX, SET, KLSE) for comparative fragility studies.
7. **Mobile-first redesign** for accessibility to retail Filipino investors.

---

## Contributing & Feedback

Archipelago is a living research prototype, and the map is far from finished. If you've spotted something we missed, have ideas worth testing, or want to push the methodology further — open an issue or reach out to the authors. The best networks grow at their edges.

---

*Archipelago — "See the invisible risk."*
