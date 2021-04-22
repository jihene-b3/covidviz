from scipy import sparse
import networkx as nx
import matplotlib.pyplot as plt
from scipy.sparse import isspmatrix
import numpy as np

def create_propag_graph():
    G = nx.DiGraph(directed=True)
    G.add_edge(r"$S_t$", 'S')
    G.add_edge('S', 'E')
    G.add_edge('E', 'I')
    G.add_edge('I', 'C')
    G.add_edge('E', 'P')
    G.add_edge(r"$E_t$", 'P')
    G.add_edge('P', 'C')
    G.add_edge('P', 'S')
    G.add_edge('S', 'P')
    G.add_edge('S', r"$E_t$")
    G.add_edge('S', r"$S_t$")
    G.add_edge('C', 'R')
    return G

def plot_propag_graph(G):
    pos = nx.spring_layout(G, seed=12345678)
    nx.draw_networkx(G, pos, with_labels=True, font_size=11,
                    node_color='#528B8B')

    labels_edge = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_edge)
    nx.draw_networkx_edges(G, pos, edge_color='#528B8B')
    plt.axis('off')
    plt.show()
