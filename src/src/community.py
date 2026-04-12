"""
community.py
------------
Detects natural stock communities (clusters) using the Louvain algorithm.

Louvain community detection finds groups of nodes that are more
densely connected to each other than to the rest of the network.
It maximizes modularity — a measure of how well the network
separates into distinct communities.
"""

import networkx as nx
import pandas as pd
import community as community_louvain  # from python-louvain package


def detect_communities(G: nx.Graph, resolution: float = 1.0) -> pd.DataFrame:
    """
    Detect communities in the PSEi graph using the Louvain algorithm.

    Parameters
    ----------
    G : nx.Graph
        The filtered PSEi graph.
    resolution : float
        Resolution parameter for Louvain. Higher values = more, smaller communities.
        Default is 1.0 (standard modularity).

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: ticker, community.
        Each row assigns a stock to its detected community.
    """
    # Louvain works on undirected graphs — G is already undirected
    # Use edge weight as affinity (lower distance = higher affinity)
    # We invert weight so that closer stocks are more strongly pulled together
    G_affinity = nx.Graph()
    G_affinity.add_nodes_from(G.nodes())
    for u, v, data in G.edges(data=True):
        # Affinity = 1 / distance (closer = stronger community pull)
        affinity = 1.0 / data["weight"] if data["weight"] > 0 else 1.0
        G_affinity.add_edge(u, v, weight=affinity)

    partition = community_louvain.best_partition(
        G_affinity, weight="weight", resolution=resolution, random_state=42
    )

    df = pd.DataFrame({
        "ticker": list(partition.keys()),
        "community": list(partition.values()),
    })
    df.sort_values("community", inplace=True)
    df.reset_index(drop=True, inplace=True)

    num_communities = df["community"].nunique()
    print(f"  Louvain detected {num_communities} communities")
    return df
