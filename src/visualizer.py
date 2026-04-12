"""
visualizer.py
-------------
All plotting and visualization functions for the PSEi graph analysis.
Generates the four main figures used in the study.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import pandas as pd
import seaborn as sns
from typing import Optional


# ── Shared style settings ────────────────────────────────────────────────────
DARK_BG = "#0F1B3D"
NODE_COLOR = "#2563EB"
HUB_COLOR = "#93C5FD"
EDGE_COLOR = "#3B82F6"
TEXT_COLOR = "#FFFFFF"
FIG_SIZE = (12, 8)


def plot_heatmap(dist_matrix: pd.DataFrame, save_path: str) -> None:
    """
    Plot and save the PSEi distance matrix as a heatmap (Figure 1).

    Parameters
    ----------
    dist_matrix : pd.DataFrame
        Symmetric distance matrix.
    save_path : str
        File path to save the figure.
    """
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    fig.patch.set_facecolor(DARK_BG)
    ax.set_facecolor(DARK_BG)

    sns.heatmap(
        dist_matrix,
        cmap="YlGnBu_r",
        ax=ax,
        square=True,
        linewidths=0.3,
        linecolor="#1E3A8A",
        cbar_kws={"label": "Metric Distance (d_ij)", "shrink": 0.8},
    )

    ax.set_title(
        "Figure 1: PSEi Distance Matrix Heatmap (2023–2025)",
        color=TEXT_COLOR, fontsize=13, pad=12
    )
    ax.tick_params(colors=TEXT_COLOR, labelsize=7)
    ax.set_xlabel("Stock Ticker", color=TEXT_COLOR, fontsize=9)
    ax.set_ylabel("Stock Ticker", color=TEXT_COLOR, fontsize=9)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight", facecolor=DARK_BG)
    plt.close()
    print(f"  Saved: {save_path}")


def plot_mst_knn(G_mst: nx.Graph, G_knn: nx.Graph, save_path: str) -> None:
    """
    Plot MST and KNN graphs side by side (Figure 2).

    Parameters
    ----------
    G_mst : nx.Graph
        Minimum Spanning Tree graph.
    G_knn : nx.Graph
        k-Nearest Neighbor graph.
    save_path : str
        File path to save the figure.
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    fig.patch.set_facecolor(DARK_BG)

    pos_mst = nx.spring_layout(G_mst, seed=42, k=2.5)
    pos_knn = nx.spring_layout(G_knn, seed=42, k=2.5)

    for ax, G, pos, title in zip(
        axes,
        [G_mst, G_knn],
        [pos_mst, pos_knn],
        ["Minimum Spanning Tree (MST)", "3-Nearest Neighbor (KNN) Graph"]
    ):
        ax.set_facecolor(DARK_BG)
        degrees = dict(G.degree())
        node_sizes = [300 + degrees[n] * 150 for n in G.nodes()]

        nx.draw_networkx_edges(G, pos, ax=ax, edge_color=EDGE_COLOR,
                               width=1.2, alpha=0.6)
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color=NODE_COLOR,
                               node_size=node_sizes, alpha=0.9)
        nx.draw_networkx_labels(G, pos, ax=ax, font_color=TEXT_COLOR,
                                font_size=6, font_weight="bold")

        ax.set_title(title, color=TEXT_COLOR, fontsize=11, pad=8)
        ax.axis("off")

    fig.suptitle("Figure 2: Topological Filtering Methods Comparison",
                 color=TEXT_COLOR, fontsize=13, y=1.01)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight", facecolor=DARK_BG)
    plt.close()
    print(f"  Saved: {save_path}")


def plot_topological_map(
    G: nx.Graph,
    communities: pd.DataFrame,
    centrality: pd.DataFrame,
    save_path: str
) -> None:
    """
    Plot the full PSEi topological community map (Figure 3).

    Node size scales with betweenness centrality.
    Node color represents Louvain community membership.

    Parameters
    ----------
    G : nx.Graph
        Filtered PSEi graph.
    communities : pd.DataFrame
        Community assignments (columns: ticker, community).
    centrality : pd.DataFrame
        Centrality scores (columns: ticker, betweenness, ...).
    save_path : str
        File path to save the figure.
    """
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    fig.patch.set_facecolor(DARK_BG)
    ax.set_facecolor(DARK_BG)

    pos = nx.spring_layout(G, seed=42, k=3.0)

    # Map community to color
    comm_map = dict(zip(communities["ticker"], communities["community"]))
    palette = plt.cm.get_cmap("tab20", communities["community"].nunique())
    node_colors = [palette(comm_map.get(n, 0)) for n in G.nodes()]

    # Map betweenness to node size
    bet_map = dict(zip(centrality["ticker"], centrality["betweenness"]))
    node_sizes = [500 + bet_map.get(n, 0) * 5000 for n in G.nodes()]

    nx.draw_networkx_edges(G, pos, ax=ax, edge_color=EDGE_COLOR,
                           width=1.0, alpha=0.5)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors,
                           node_size=node_sizes, alpha=0.92)
    nx.draw_networkx_labels(G, pos, ax=ax, font_color=TEXT_COLOR,
                            font_size=6.5, font_weight="bold")

    ax.set_title(
        "Figure 3: PSEi Topological Community Map (2023–2025)\n"
        "Node size ∝ betweenness centrality  |  Color = Louvain community",
        color=TEXT_COLOR, fontsize=11, pad=10
    )
    ax.axis("off")

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight", facecolor=DARK_BG)
    plt.close()
    print(f"  Saved: {save_path}")


def plot_hub_removal(G_removed: nx.Graph, save_path: str) -> None:
    """
    Plot the PSEi network after hub removal (Figure 4).

    Parameters
    ----------
    G_removed : nx.Graph
        Graph after ALI, SMPH, URC have been removed.
    save_path : str
        File path to save the figure.
    """
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    fig.patch.set_facecolor(DARK_BG)
    ax.set_facecolor(DARK_BG)

    pos = nx.spring_layout(G_removed, seed=42, k=3.0)
    degrees = dict(G_removed.degree())
    node_sizes = [250 + degrees[n] * 150 for n in G_removed.nodes()]

    nx.draw_networkx_edges(G_removed, pos, ax=ax, edge_color=EDGE_COLOR,
                           width=1.0, alpha=0.5)
    nx.draw_networkx_nodes(G_removed, pos, ax=ax, node_color=NODE_COLOR,
                           node_size=node_sizes, alpha=0.9)
    nx.draw_networkx_labels(G_removed, pos, ax=ax, font_color=TEXT_COLOR,
                            font_size=7, font_weight="bold")

    ax.set_title(
        "Figure 4: Fragmented PSEi Network After Removing ALI, SMPH, URC\n"
        "Connected components increased: 14 → 17",
        color=TEXT_COLOR, fontsize=11, pad=10
    )
    ax.axis("off")

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight", facecolor=DARK_BG)
    plt.close()
    print(f"  Saved: {save_path}")
