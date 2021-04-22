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
G = cvz.create_propag_graph()
cvz.plot_propag_graph(G)

#%%
G = cvz.create_transfer_graph()
cvz.plot_transfer_graph(G)
