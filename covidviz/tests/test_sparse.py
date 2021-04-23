import os.path, sys
import numpy as np
import pandas as pd
from scipy import sparse
import networkx as nx
import matplotlib.pyplot as plt
from scipy.sparse import isspmatrix

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)
import covidviz as cvz

# global variables
url_transf = "https://www.data.gouv.fr/fr/datasets/r/70cf1fd0-60b3-4584-b261-63fb2281359e"
df_transf_raw = pd.read_csv(url_transf)


def test_create_graph():
    test = cvz.create_transfer_graph()
    assert (type(test) == nx.classes.digraph.DiGraph)


def test_plot_adjacency_matrix():
    G = cvz.create_transfer_graph()
    test = cvz.plot_adjacency_matrix(G)
    assert (isspmatrix(test))