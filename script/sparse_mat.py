#%%
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz


#%%
G = cvz.create_transfer_graph()
cvz.plot_transfer_graph(G)

#%%
A = cvz.plot_adjacency_matrix(G)
# %%
