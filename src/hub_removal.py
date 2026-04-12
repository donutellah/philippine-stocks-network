Hub_removal.py
--------------
Simulates the structural effect of removing hub stocks from the PSEi network.

This experiment tests systemic fragility: if the most central stocks
(ALI, SMPH, URC) are removed, how much more fragmented does the market become?
We measure this by counting connected components before and after removal.
"""

import networkx as nx
from typing import Tuple, List


def simulate_hub_removal(
    G: nx.Graph,
    hubs: List[str]
) -> Tuple[nx.Graph, int, int]:
    """
    Remove hub nodes from the graph and measure the change in fragmentation.

    Parameters
    ----------
    G : nx.Graph
        The filtered PSEi graph (before removal).
    hubs : list of str
        List of stock tickers to remove (e.g. ["ALI", "SMPH", "URC"]).

    Returns
    -------
    G_removed : nx.Graph
        The graph after hub removal.
    components_before : int
        Number of connected components before removal.
    components_after : int
        Number of connected components after removal.
    """
    # Count connected components before removal
    components_before = nx.number_connected_components(G)

    # Remove the hub nodes and all their edges
    G_removed = G.copy()
    for hub in hubs:
        if hub in G_removed.nodes():
            G_removed.remove_node(hub)
        else:
            print(f"  Warning: {hub} not found in graph — skipping.")

    # Count connected components after removal
    components_after = nx.number_connected_components(G_removed)

    print(f"  Hubs removed: {hubs}")
    print(f"  Connected components: {components_before} → {components_after}")
    print(f"  Fragmentation increased by {components_after - components_before} components")

    return G_removed, components_before, components_after
