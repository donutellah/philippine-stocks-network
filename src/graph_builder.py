graph_builder.py
----------------
Builds a weighted undirected graph from the distance matrix
and applies threshold filtering to remove weak connections.
"""

import networkx as nx
import pandas as pd


def build_graph(dist_matrix: pd.DataFrame) -> nx.Graph:
    """
    Build a fully connected weighted undirected graph from the distance matrix.

    Each node is a PSEi stock ticker. Each edge weight is the
    distance d_ij between stocks i and j.

    Parameters
    ----------
    dist_matrix : pd.DataFrame
        Symmetric distance matrix (tickers as index and columns).

    Returns
    -------
    nx.Graph
        Fully connected weighted graph (self-loops excluded).
    """
    G = nx.Graph()
    tickers = dist_matrix.columns.tolist()

    # Add all tickers as nodes
    G.add_nodes_from(tickers)

    # Add edges for all unique pairs (upper triangle only, skip diagonal)
    for i, ticker_i in enumerate(tickers):
        for j, ticker_j in enumerate(tickers):
            if j <= i:
                continue  # Skip diagonal and lower triangle (undirected)
            weight = dist_matrix.loc[ticker_i, ticker_j]
            G.add_edge(ticker_i, ticker_j, weight=float(weight))

    print(f"  Full graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    return G


def apply_threshold(G: nx.Graph, threshold: float = 1.2) -> nx.Graph:
    """
    Remove edges with distance greater than the threshold.

    Weak correlations (large distances) are treated as noise
    and excluded from the filtered network.

    Parameters
    ----------
    G : nx.Graph
        Full weighted graph.
    threshold : float
        Maximum distance allowed. Default is τ = 1.2.

    Returns
    -------
    nx.Graph
        Filtered graph containing only strong connections.
    """
    G_filtered = nx.Graph()
    G_filtered.add_nodes_from(G.nodes())  # Keep all nodes even if isolated

    for u, v, data in G.edges(data=True):
        if data["weight"] <= threshold:
            G_filtered.add_edge(u, v, weight=data["weight"])

    surviving = G_filtered.number_of_edges()
    total = G.number_of_edges()
    print(f"  After threshold τ={threshold}: {surviving} edges kept ({surviving/total*100:.1f}% of total)")
    return G_filtered
