# Topological Stability and Systemic Fragility of the Philippine Equity Market

> **Graph Gang** — BSM CS3B | College of Science, Bulacan State University
>
> Ellah Benerado · Niña Mycaella Fedalquin · Ryan Jerick Peñafiel · Carl Nuqui · Angel Viray

---

## Overview

This project applies **graph theory and network analysis** to the 30 component stocks of the Philippine Stock Exchange Index (PSEi) using daily closing prices from **2023 to 2025**.

We model the stock market as a weighted undirected graph where:
- Each **node** is a PSEi stock
- Each **edge** represents a strong correlation between two stocks
- **Edge weights** are derived from a Pearson correlation-based distance metric

We then analyze the network's structure to identify **hub stocks**, **fragile connections**, and **systemic risk** — answering the question: *if a key stock collapses, how much of the market collapses with it?*

---

## 🗂️ Repository Structure

psei-graph-analysis/
│
├── data/
│   ├── raw/
│   │   └── psei_closing_prices.csv       # Raw daily closing prices (2023–2025)
│   └── processed/
│       ├── log_returns.csv               # Computed log returns
│       ├── correlation_matrix.csv        # Pearson correlation matrix
│       └── distance_matrix.csv           # Transformed distance matrix
│
├── notebooks/
│   ├── 01_data_collection.ipynb          # Data download and cleaning
│   ├── 02_correlation_distance.ipynb     # Log returns, correlation, distance
│   ├── 03_graph_construction.ipynb       # Graph building + threshold filtering
│   ├── 04_mst_knn.ipynb                  # MST and KNN graph construction
│   ├── 05_centrality_community.ipynb     # Centrality metrics + Louvain detection
│   └── 06_hub_removal_analysis.ipynb     # Hub removal experiment (ALI, SMPH, URC)
│
├── src/
│   ├── data_loader.py                    # Functions to load and clean price data
│   ├── returns.py                        # Log return computation
│   ├── correlation.py                    # Pearson correlation and distance matrix
│   ├── graph_builder.py                  # Graph construction and threshold filtering
│   ├── mst.py                            # Minimum Spanning Tree construction
│   ├── knn_graph.py                      # k-Nearest Neighbor graph construction
│   ├── centrality.py                     # Degree, betweenness, eigenvector centrality
│   ├── community.py                      # Louvain community detection
│   ├── hub_removal.py                    # Hub removal simulation
│   └── visualizer.py                     # All plotting and visualization functions
│
├── outputs/
│   ├── figures/
│   │   ├── heatmap_distance_matrix.png   # Figure 1: Distance matrix heatmap
│   │   ├── mst_knn_comparison.png        # Figure 2: MST vs KNN graph
│   │   ├── topological_map.png           # Figure 3: Full PSEi network map
│   │   └── hub_removal_network.png       # Figure 4: Network after hub removal
│   └── results/
│       ├── centrality_scores.csv         # Centrality metrics per stock
│       └── community_assignments.csv     # Louvain community labels per stock
│
├── requirements.txt                      # Python dependencies
├── .gitignore                            # Files to exclude from version control
└── README.md                             # This file
```

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/graph-gang-bsu/psei-graph-analysis.git
cd psei-graph-analysis
```

### 2. Set up a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the notebooks in order

Open Jupyter and run the notebooks inside `/notebooks/` **in numbered order** (01 → 06). Each notebook builds on the outputs of the previous one.

```bash
jupyter notebook
```

Or run the full pipeline as a script:

```bash
python src/main.py
```

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`. Key libraries:

| Library | Purpose |
|---|---|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical computation |
| `yfinance` | Downloading PSEi stock price data |
| `scipy` | Pearson correlation computation |
| `networkx` | Graph construction and analysis |
| `matplotlib` | Plotting and visualization |
| `seaborn` | Heatmap visualization |
| `python-louvain` | Louvain community detection |
| `scikit-learn` | KNN graph construction |
| `jupyter` | Running notebooks |

Install all at once:

```bash
pip install -r requirements.txt
```

---

## Methodology Summary

### Step 1 — Log Returns
Daily log returns are computed as:

```
r_i(t) = ln(P_i(t)) - ln(P_i(t-1))
```

### Step 2 — Pearson Correlation Matrix
A 30×30 correlation matrix is computed from the log return series of all PSEi stocks.

### Step 3 — Distance Metric
Correlations are transformed into distances:

```
d_ij = sqrt(2 * (1 - |rho_ij|))
```

Smaller distance = stronger connection between stocks.

### Step 4 — Threshold Filtering
Edges with distance > **τ = 1.2** are removed. Only strong connections survive.

### Step 5 — Graph Construction
Two filtered graph representations are built:
- **Minimum Spanning Tree (MST)** — keeps the N−1 strongest backbone connections
- **3-Nearest Neighbor Graph (KNN)** — each stock connects to its 3 closest neighbors

### Step 6 — Network Analysis
- **Algebraic connectivity (λ₂)** — global stability score of the network
- **Degree, betweenness, eigenvector centrality** — identifies hub stocks
- **Louvain community detection** — finds natural stock clusters

### Step 7 — Hub Removal Experiment
ALI, SMPH, and URC (the top betweenness hubs) are removed from the network.
Connected components increase from **14 → 17**, confirming structural fragility.

---

## Key Results

| Metric | Value |
|---|---|
| Total possible edges | 435 |
| Edges after thresholding (τ = 1.2) | 35 |
| Louvain communities detected | 16 |
| Connected components | 14 |
| Algebraic connectivity (λ₂) | ≈ 0 (−1.97 × 10⁻¹⁶) |
| Connected components after hub removal | 17 |
| Key hub stocks identified | ALI, SMPH, URC |

---

## 📁 Data Source

Stock price data was scraped from **PSE Edge** (https://edge.pse.com.ph)
using **Python** and **BeautifulSoup4**.

Daily closing prices for all 30 PSEi component stocks were collected
from **January 2023 to December 2025**.

The scraper script is located at `src/scraper.py`.
Raw data is saved to `data/raw/psei_closing_prices.csv`.

PSEi component tickers used:
```
AC, AEV, AGI, ALI, BDO, BPI, CBC, DMC, GLO, ICT,
JFC, JGS, LOTO, MBT, MER, SCC, SMC, SM, SMPH, ACEN,
LTG, TEL, URC, PGOLD, EMI, GTCAP, CNPF, AREIT, CNVRG, MONDE
```
---

### Authors
| Name | Role |
| :--- | :--- |
| Ellah D. Benerado | Member |
| Niña Mycaella Fedalquin | Member |
| Ryan Jerick Peñafiel | Member |
| Carl Gaudenz Nuqui | Member |
| Angel Lorraine Viray | Member |

---

## 📄 License

This project was created for academic purposes as part of a course requirement at Bulacan State University. All code is original work by Graph Gang — BSM CS3B.
