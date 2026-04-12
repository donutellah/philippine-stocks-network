# Archipelago
PSEi Portfolio Intelligence Tool — coming soon.

> A practical application of the *Topological Stability and Systemic Fragility of the Philippine Equity Market* research by **Graph Gang**, BSM CS3B, Bulacan State University.

---

## What is Archipelago?

**Archipelago** is an interactive web application that turns academic graph theory research into a tool anyone can use to understand and manage risk in the Philippine Stock Exchange (PSEi).

Instead of just reading about which stocks are fragile — you can **see it, simulate it, and act on it.**

---

## Live Demo

> 🌐 [https://philippine-stocks-network-ja3c.vercel.app/archipelago-app/archipelago_app.html](#) ← *(add your Vercel link here)*

---

## Features

| Screen | Description |
|---|---|
| **My Observatory** | Your personal portfolio dashboard — see your topology map, diversification score, systemic exposure, and Harris.AI insights |
| **Portfolio Scanner** | Scan your stock holdings for structural risk, community overlap, and hidden correlations |
| **Contagion Simulator** | Simulate what happens when hub stocks like ALI, SMPH, or URC crash — watch the shock spread through the network |
| **Diversify Recommender** | Get topology-aware stock recommendations that actually reduce structural risk |
| **Market Health** | Monitor the PSEi's algebraic connectivity (λ₂), MST structure, and sector correlation matrix in real time |
| **Portfolio Topology** | Explore the full PSEi network map — see communities, bridge nodes, and isolated stocks |
| **About** | Learn about the research behind Archipelago |

---

## 🤖 Harris.AI

Every screen is powered by **Harris.AI** an in-app intelligence layer that provides real-time structural analysis, risk synthesis, and mitigation strategies based on your portfolio's topological position in the PSEi network.

---

## Research Foundation

Archipelago is built directly on the findings of our study:

- **Hub stocks identified:** ALI, SMPH, URC
- **Algebraic connectivity (λ₂):** ≈ 0 — near-fragile market state
- **Connected components:** 14 (17 after hub removal)
- **Louvain communities:** 16 distinct stock clusters
- **Method:** MST + 3-KNN graph filtering on Pearson correlation distances

> Removing just 3 hub stocks increases market fragmentation by 21% — this is what Archipelago helps you avoid in your own portfolio.

---

## Built With

- **HTML / CSS / JavaScript** — Single-file compiled app
- **Tailwind CSS** — Styling
- **Graph Gang research data** — PSEi correlation network (2023–2025)

---

## Status

This is a **prototype**. Full development with live PSEi data integration is planned as a future extension of the research.

