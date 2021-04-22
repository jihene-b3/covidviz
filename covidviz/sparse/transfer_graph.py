from scipy import sparse
import networkx as nx
import matplotlib.pyplot as plt
from scipy.sparse import isspmatrix
import numpy as np
from covidviz.preprocess import clean_df
import pandas as pd


def create_transfer_graph():

    df_transf_raw = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/70cf1fd0-60b3-4584-b261-63fb2281359e")
    df_transf_raw['region_arrivee'] = df_transf_raw['region_arrivee'].replace(np.nan, "Other european country")
    df_transf = clean_df.choose_columns(df_transf_raw, ["region_depart", "region_arrivee", "nombre_patients_transferes"])
    G = nx.from_pandas_edgelist(df_transf, 'region_depart', 'region_arrivee', edge_attr="nombre_patients_transferes", create_using=nx.DiGraph())
    return G


def plot_transfer_graph(G):
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
