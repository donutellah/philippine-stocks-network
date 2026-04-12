"""
centrality.py
-------------
Computes node centrality metrics to identify hub stocks in the PSEi network.

Three centrality measures are used:
- Degree centrality     : how many connections a stock has
- Betweenness centrality: how often a stock lies on the shortest path between others
- Eigenvector centrality: how connected a stock is to other well-connected stocks
"""

import networkx as nx
import pandas as pd


def compute_centrality(G: nx.Graph) -> pd.DataFrame:
    """
    Compute degree, betweenness, and eigenvector centrality for all nodes.

    Parameters
    ----------
    G : nx.Graph
        The filtered PSEi graph.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: ticker, degree, betweenness, eigenvector.
        Sorted by betweenness centrality descending.
    """
    # Degree centrality — fraction of nodes this node is connected to
    degree = nx.degree_centrality(G)

    # Betweenness centrality — fraction of shortest paths passing through this node
    # Use weight as distance (shorter distance = stronger connection)
    betweenness = nx.betweenness_centrality(G, weight="weight", normalized=True)

    # Eigenvector centrality — importance based on neighbors' importance
    try:
        eigenvector = nx.eigenvector_centrality(G, weight="weight", max_iter=1000)
    except nx.PowerIterationFailedConvergence:
        # Falls back to unweighted if convergence fails (e.g. disconnected graph)
        eigenvector = nx.eigenvector_centrality_numpy(G)

    # Combine into a single DataFrame
    df = pd.DataFrame({
        "ticker": list(degree.keys()),
        "degree": list(degree.values()),
        "betweenness": [betweenness[n] for n in degree.keys()],
        "eigenvector": [eigenvector[n] for n in degree.keys()],
    })

    df.sort_values("betweenness", ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)

    return df
