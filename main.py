"""
main.py
-------
Graph Gang — PSEi Topological Stability Analysis
BSM CS3B, Bulacan State University

Run this script to execute the full analysis pipeline from start to finish.
Make sure all dependencies are installed first:
    pip install -r requirements.txt
"""

import os
from src.data_loader import load_prices
from src.returns import compute_log_returns
from src.correlation import compute_correlation, compute_distance_matrix
from src.graph_builder import build_graph, apply_threshold
from src.mst import build_mst
from src.knn_graph import build_knn_graph
from src.centrality import compute_centrality
from src.community import detect_communities
from src.hub_removal import simulate_hub_removal
from src.visualizer import (
    plot_heatmap,
    plot_mst_knn,
    plot_topological_map,
    plot_hub_removal
)

# ── Output directories ──────────────────────────────────────────────────────
os.makedirs("outputs/figures", exist_ok=True)
os.makedirs("outputs/results", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

# ── Step 1: Load price data ──────────────────────────────────────────────────
print("Step 1: Loading PSEi closing prices...")
prices = load_prices("data/raw/psei_closing_prices.csv")

# ── Step 2: Compute log returns ──────────────────────────────────────────────
print("Step 2: Computing log returns...")
returns = compute_log_returns(prices)
returns.to_csv("data/processed/log_returns.csv")

# ── Step 3: Correlation and distance matrix ──────────────────────────────────
print("Step 3: Computing correlation and distance matrix...")
corr_matrix = compute_correlation(returns)
dist_matrix = compute_distance_matrix(corr_matrix)
corr_matrix.to_csv("data/processed/correlation_matrix.csv")
dist_matrix.to_csv("data/processed/distance_matrix.csv")

# ── Step 4: Plot distance heatmap ────────────────────────────────────────────
print("Step 4: Plotting distance matrix heatmap...")
plot_heatmap(dist_matrix, save_path="outputs/figures/heatmap_distance_matrix.png")

# ── Step 5: Build and filter graph ──────────────────────────────────────────
print("Step 5: Building graph with threshold τ = 1.2...")
THRESHOLD = 1.2
G_full = build_graph(dist_matrix)
G = apply_threshold(G_full, threshold=THRESHOLD)
print(f"  Edges surviving threshold: {G.number_of_edges()} / {G_full.number_of_edges()}")

# ── Step 6: MST and KNN graphs ───────────────────────────────────────────────
print("Step 6: Building MST and 3-KNN graphs...")
G_mst = build_mst(G_full)
G_knn = build_knn_graph(dist_matrix, k=3)
plot_mst_knn(G_mst, G_knn, save_path="outputs/figures/mst_knn_comparison.png")

# ── Step 7: Centrality and community detection ───────────────────────────────
print("Step 7: Computing centrality and detecting communities...")
centrality_df = compute_centrality(G)
centrality_df.to_csv("outputs/results/centrality_scores.csv")
print(centrality_df.sort_values("betweenness", ascending=False).head(5))

communities = detect_communities(G)
communities.to_csv("outputs/results/community_assignments.csv")
print(f"  Louvain communities detected: {communities['community'].nunique()}")

# ── Step 8: Topological map ──────────────────────────────────────────────────
print("Step 8: Plotting topological map...")
plot_topological_map(
    G,
    communities=communities,
    centrality=centrality_df,
    save_path="outputs/figures/topological_map.png"
)

# ── Step 9: Hub removal experiment ──────────────────────────────────────────
print("Step 9: Running hub removal experiment (ALI, SMPH, URC)...")
hubs = ["ALI", "SMPH", "URC"]
G_removed, components_before, components_after = simulate_hub_removal(G, hubs)
print(f"  Connected components before removal: {components_before}")
print(f"  Connected components after removal:  {components_after}")
plot_hub_removal(G_removed, save_path="outputs/figures/hub_removal_network.png")

# ── Step 10: Algebraic connectivity ─────────────────────────────────────────
import networkx as nx
import numpy as np
print("Step 10: Computing algebraic connectivity (λ₂)...")
laplacian = nx.laplacian_matrix(G).toarray()
eigenvalues = np.sort(np.linalg.eigvalsh(laplacian))
lambda_2 = eigenvalues[1]
print(f"  Algebraic connectivity λ₂ = {lambda_2:.4e}")

print("\nDone! All outputs saved to /outputs/")
