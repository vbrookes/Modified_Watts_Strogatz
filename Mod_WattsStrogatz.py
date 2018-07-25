# -*- coding: utf-8 -*-
import random
import networkx as nx
import numpy as np


''' Function to construct a graph with small world characteristics '''
''' with emprical degree and edge-weight distribution '''
def VB_watts_strogatz(nodes_list, degree, edge, t, seed=None):
    
    """Create a Watts–Strogatz small-world graph with empirical
    degree and edge-weight distributions. 
    
    Orginal base code
    https://github.com/sleepokay/watts-strogatz
    
    Parameters
    ----------
    nodes_list : list of graph sizes (integers) if function is included in a 
    loop to create many networks of sizes n, or list with one element for a 
    single graph of size n.
    n : int
        The number of nodes
    degree: int
        list of degrees from empirical distribution to give k
    k : int
        Each node is joined with its `k` nearest neighbors in a ring
        topology. k is selected from an empirical distribution for each node.
    t : float
        The probability of rewiring each edge
    edge: float
        list of edge-weights from empirical distribution
    seed : int, optional
        Seed for random number generator (default=None)
    
    Notes
    -----
    A regular lattice of 'n' nodes is created. Degree is pre-assigned to each node 
    from empirical distribution. Join each node in the ring to its k//2+1 nearest 
    neighbors in a forward direction then all nearest neighbours in a backward
    direction to achieve k.
    Edges are re-wired following a Bernoulli process in which edge `(u, v)` in 
    is replaced with a new edge `(u, w)` so that the degree of u and w are not
    > pre-assigned degree.
    In this way, the random rewiring does not increase the number of edges. 
    The rewired graph is not guaranteed to be connected.
    """
    if seed is not None:
        random.seed(seed)
    
    G = nx.Graph()
    n = random.choice(nodes_list)
    nodes = list(range(n)) # nodes are labeled 0 to n-1
    G.add_nodes_from(nodes)
    degrees = [] # Get a list of degrees for each node
    for i in range(0, max(nodes)+1):
        d = np.random.choice(degree)
        degrees.append(d)

        # connect each node to k/2 neighbors
    for j in range(0, max(nodes) + 1):
        l = degrees[j]
        k = (l - G.degree(j))//2+1
        # Forward nodes to connect from j
        if (j + k) <= max(nodes):
            for p1 in range(1, k):
                if G.degree(j) < degrees[j]:
                    if random.random() < t:
                        w = random.choice(nodes)
                        if w != j: 
                            if G.degree(w) < degrees[w]:
                                G.add_edge(j,w)
                            else:
                                pass
                        else:
                            pass
                    else:
                        G.add_edge(j, j + p1)
                else:
                    pass
    
        elif (j + k) > max(nodes):
            z = max(nodes) - j
            for p2 in range (1, z):
                if G.degree(j) < degrees[j]:
                    if random.random() < t:
                        w = random.choice(nodes)
                        if w != j: 
                            if G.degree(w) < degrees[w]:
                                G.add_edge(j,w)
                            else:
                                pass
                        else:
                            pass
                    else:
                        G.add_edge(j, j + p2)
                else:
                    pass
            y = k - z
            for p3 in range (1, y):
                if G.degree(j) < degrees[j]:
                    if random.random() < t:
                        w = random.choice(nodes)
                        if w != j: 
                            if G.degree(w) < degrees[w]:
                                G.add_edge(j,w)
                            else:
                                pass
                        else:
                            pass
                    else:
                        G.add_edge(j, 0 + p3)
                else:
                    pass
        # Backward nodes to connect from j
        if (j - k) >= 0:
            for s1 in range(1, k):
                if G.degree(j) < degrees[j]:
                    if random.random() < t:
                        w = random.choice(nodes)
                        if w != j: 
                            if G.degree(w) < degrees[w]:
                                G.add_edge(j,w)
                            else:
                                pass
                        else:
                            pass
                    else:
                        G.add_edge(j, j - s1)
                else:
                    pass
  
        elif (j + k) < 0:
            z = j - 0
            for s2 in range (1, z):
                if G.degree(j) < degrees[j]:
                    if random.random() < t:
                        w = random.choice(nodes)
                        if w != j: 
                            if G.degree(w) < degrees[w]:
                                G.add_edge(j,w)
                            else:
                                pass
                        else:
                            pass
                    else:
                        G.add_edge(j, j - s2)
                else:
                    pass
            y = k - z
            for s2 in range (1, y):
                if G.degree(j) < degrees[j]:
                    if random.random() < t:
                        w = random.choice(nodes)
                        if w != j: 
                            if G.degree(w) < degrees[w]:
                                G.add_edge(j,w)
                            else:
                                pass
                        else:
                            pass
                    else:
                        G.add_edge(j, max(nodes) - s2)
                else:
                    pass
        else:
            pass
    # This algorithm adds edges to k-nearest neighbours to complete required degree distribution                    
    for j in range(0, max(nodes) + 1):
        m = 1
        while G.degree(j) < degrees[j] and m <= max(nodes):
            if (j + m) <= max(nodes):
                if G.degree(m) < degrees[m]:
                    if j != m:
                        G.add_edge(j, m)
            else:
                r = (j - max(nodes)) + m -1
                if G.degree(r) < degrees[r]:
                    G.add_edge(j, r)
            m = m + 1

    for (u, v) in G.edges():
        G.edge[u][v]['weight'] = random.choice(edge)

    G.remove_edges_from(G.selfloop_edges()) # remove self-loops
    return G

    
