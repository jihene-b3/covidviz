import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from demography_covid import io
from demography_covid import preprocess
from download import download
import plotly.express as px
import folium
import plotly.graph_objects as go
import kaleido

def df_rea(df) :
    fig = px.bar(df, x="AgeGroup",
        y="nb-rea",
        color="AgeGroup",
        animation_frame="date", 
        animation_group="AgeGroup",
        range_y=[0,30])
    fig.update_layout(
        height=600,
        title_text="Nombre de patients en réanimation par classe d'âge")
    fig.show()
    return(fig.show())
# In[34]:
def df_hosp(df) :
    fig = px.bar(df, x="AgeGroup", y="nb_hosp", color="AgeGroup",
         animation_frame="date", animation_group="AgeGroup", 
         range_y=[0,150])
    fig.update_layout(
    height=600,
    title_text="Nombre de patients hospitalisés par classe d'âge"
)
    fig.show()
    return(fig.show())

# In[38]:
def df_dec(df) : 
    datefrom='2020-04-01'
    fig = px.line(df, x="date", y="dec_Tot", color="AgeGroup",range_x=[datefrom,'2021-04-15'])
# fig.update_layout(hovermode='x unified')
    fig.update_layout(
    height=600,
    title_text="Nombre de patients décédès par classes d'âges"
)
    fig.show()
    return(fig.show())