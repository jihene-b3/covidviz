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
from scipy.sparse import isspmatrix

#%%

# S_t : susceptible tracked 0
# S : susceptible 1
# E : Exposed 2
# E_t : Exposed tracked 3
# P : suspected 4
# C : confirmed 5
# I : infectious 6
# R : recovered 7

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

pos = nx.spring_layout(G, seed=12345678)
nx.draw_networkx(G, pos, with_labels=True, font_size=11,
                node_color='#528B8B')

labels_edge = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_edge)
nx.draw_networkx_edges(G, pos, edge_color='#528B8B')
plt.axis('off')
plt.show()


# %%
import numpy as np

df_transf_raw = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/70cf1fd0-60b3-4584-b261-63fb2281359e")

#%%

df_transf_raw['region_arrivee'] = df_transf_raw['region_arrivee'].replace(np.nan, "Other european country")


#%%
df_transf = cvz.choose_columns(df_transf_raw, ["region_depart", "region_arrivee", "nombre_patients_transferes"])


G = nx.from_pandas_edgelist(df_transf, 'region_depart', 'region_arrivee', edge_attr="nombre_patients_transferes", create_using=nx.DiGraph())


plt.figure(figsize=(15, 15))
pos = nx.spring_layout(G, seed=12042021)
nx.draw_networkx(G, pos, with_labels=True, font_size=18,
                node_color='#528B8B', edge_color='#528B8B')

# extract edge 'weights' (i.e. number of transfered patients)
labels_edge = nx.get_edge_attributes(G, "nombre_patients_transferes")
# add weights labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_edge)

new_lab_val = [ ]
for val in list(labels_edge.values()):
    val = val*0.04
    new_lab_val.append(val)

nx.draw_networkx_edges(G, pos, width=new_lab_val, edge_color='#528B8B')

plt.axis('off')
plt.title("French patient transfers' graph", fontsize=28)
plt.show()

# %%
