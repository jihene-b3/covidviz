#%%
import pydeck as pdk
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz
import pandas as pd
from scipy import sparse
import networkx as nx
import matplotlib.pyplot as plt

#%%

G = nx.Graph() # creation du graphe
# les aretes : avec eventuellement des poids
# si pas de poids c'est 0 ou 1 (= si ya une arete)

G.add_edge('Patient', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('Patient', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
G.add_edge('D', 'Patient', weight=2)

# %%
pos = nx.spring_layout(G, seed=1234)
nx.draw_networkx(G, pos, with_labels=True)

labels_edge = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_edge)
nx.draw_networkx_edges(G, pos, width=list(labels_edge.values()))
plt.axis('off')
plt.show()
# %%
