"""
knn_graph.py
------------
Builds a k-Nearest Neighbor (KNN) graph from the distance matrix.
Each stock is connected to its k closest neighbors by distance.
This preserves local clusters better than the MST.
"""

import networkx as nx
import pandas as pd


def build_knn_graph(dist_matrix: pd.DataFrame, k: int = 3) -> nx.Graph:
    """
    Build a k-Nearest Neighbor graph from the distance matrix.

    For each stock, connect it to its k closest stocks (smallest distance).
    The graph is made undirected — if A connects to B, B also connects to A.

    Parameters
    ----------
    dist_matrix : pd.DataFrame
        Symmetric distance matrix.
    k : int
        Number of nearest neighbors per node. Default is k=3.

    Returns
    -------
    nx.Graph
        Undirected KNN graph.
    """
    tickers = dist_matrix.columns.tolist()
    G_knn = nx.Graph()
    G_knn.add_nodes_from(tickers)

    for ticker in tickers:
        # Get distances to all other stocks, sort ascending
        distances = dist_matrix[ticker].drop(ticker).sort_values()

        # Connect to the k nearest neighbors
        for neighbor in distances.index[:k]:
            weight = distances[neighbor]
            G_knn.add_edge(ticker, neighbor, weight=float(weight))

    print(f"  {k}-KNN graph built: {G_knn.number_of_nodes()} nodes, {G_knn.number_of_edges()} edges")
    return G_knn
