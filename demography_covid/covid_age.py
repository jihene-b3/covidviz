#!/usr/bin/env python
# coding: utf-8

# import libraries 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from demography_covid import io
from demography_covid import preprocess
from ipywidgets import interact  # widget manipulation
from download import download
import plotly.express as px
import folium
import plotly.graph_objects as go
import seaborn as sns
import ipywidgets as widgets
import kaleido


# Importation data

# In[25]:


url1 ='https://www.data.gouv.fr/fr/datasets/r/08c18e08-6780-452d-9b8c-ae244ad529b3'
path_target = "./classes_âges.csv"
download(url1, path_target, replace=True)
df_raw = pd.read_csv("classes_âges.csv", sep=';')
df_soc=df_raw.rename(columns={"cl_age90": "age", "jour": "date","hosp":"nb_hosp","rea":"nb-rea","HospConv":"nb_hospconv","rad":"rad_Tot","dc":"dec_Tot"})
df_soc.drop(['autres'], axis = 1, inplace = True) 
df=df_soc[df_soc['nb_hosp'] > 0]
df


# 

# - nb_hosp : nombre de patients hospitalisés, 
# - nb-rea :nombre de personnes actuellement en réanimation ou soins intensifs, 
# - nb_hospconv :nombre de personnes actuellement en hospitalisation conventionnelle, 
# - SSR_USLD : nombre de personnes actuellement en Soins de Suite et de Réadaptation (SSR) ou Unités de Soins de Longue Durée(USLD), 
# - nombre actuellement de personnes hospitalisées dans un autre type de service, 
# - nombre cumulé de personnes retournées à domicile, 
# - nombre cumulé de personnes décédées.

# In[28]:


df.loc[(df.age < 10),  'AgeGroup'] = '[0,9]'
df.loc[(df.age > 9) & (df.age < 20),  'AgeGroup'] = '[10,19]'
df.loc[(df.age > 19) & (df.age < 30),  'AgeGroup'] = '[20,39]'
df.loc[(df.age > 29) & (df.age < 40),  'AgeGroup'] = '[30,39]'
df.loc[(df.age > 39) & (df.age < 50),  'AgeGroup'] = '[40,49]'
df.loc[(df.age > 49) & (df.age < 60),  'AgeGroup'] = '[50,59]'
df.loc[(df.age > 59) & (df.age < 70),  'AgeGroup'] = '[60,69]'
df.loc[(df.age > 69) & (df.age < 80),  'AgeGroup'] = '[70,79]'
df.loc[(df.age > 79) & (df.age < 90),  'AgeGroup'] = '[80,89]'
df.loc[(df.age > 89),  'AgeGroup'] = '[90,+]'


# In[40]:


df.to_csv(r'./data/AgeGroups_cleaned.csv', index = False)


# In[27]:


#df_soc['jour'] = pd.to_datetime(df_soc['jour']).dt.to_period('M')


# In[32]:
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

# In[ ]:




