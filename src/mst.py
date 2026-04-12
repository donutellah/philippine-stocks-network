"""
mst.py
------
Builds the Minimum Spanning Tree (MST) from the full weighted graph.
The MST keeps only the N-1 edges of greatest influence (smallest weight),
forming the backbone of the market network.
"""

import networkx as nx


def build_mst(G: nx.Graph) -> nx.Graph:
    """
    Compute the Minimum Spanning Tree of the full weighted graph.

    Uses Kruskal's algorithm (default in NetworkX).
    The MST connects all nodes with the minimum total edge weight,
    removing cycles and keeping only the strongest relationships.

    Parameters
    ----------
    G : nx.Graph
        Full weighted graph (all edges included).

    Returns
    -------
    nx.Graph
        MST with exactly N-1 edges.
    """
    mst = nx.minimum_spanning_tree(G, weight="weight", algorithm="kruskal")
    print(f"  MST built: {mst.number_of_nodes()} nodes, {mst.number_of_edges()} edges")
    return mst
