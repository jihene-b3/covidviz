#!/usr/bin/env python
# coding: utf-8

# import libraries 

# In[1]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from demog_covid.preprocess.utils  import df_rea,df_dec,df_hosp
from demog_covid import preprocess
from demog_covid.preprocess.format_data import clean_age,format_age
from ipywidgets import interact  # widget manipulation
from download import download
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import ipywidgets as widgets
import kaleido

# Importation data

# In[2]:
url1 ='https://www.data.gouv.fr/fr/datasets/r/08c18e08-6780-452d-9b8c-ae244ad529b3'
path_target = "demog_covid/AgeGroups.csv"
download(url1, path_target, replace=True)
df_raw = pd.read_csv("AgeGroups.csv", sep=';')

# In[2]:

# Descriptif des variables : 

# - nb_hosp : nombre de patients hospitalisés, 
# - nb-rea :nombre de personnes actuellement en réanimation ou soins intensifs, 
# - nb_hospconv :nombre de personnes actuellement en hospitalisation conventionnelle, 
# - SSR_USLD : nombre de personnes actuellement en Soins de Suite et de Réadaptation (SSR) ou Unités de Soins de Longue Durée(USLD), 
# - nombre actuellement de personnes hospitalisées dans un autre type de service, 
# - nombre cumulé de personnes retournées à domicile, 
# - nombre cumulé de personnes décédées.

# In[4]:
def remove_nan(df):
    numeric = df.select_dtypes(include=np.number)
    numeric_columns = numeric.columns
    df[numeric_columns] = df[numeric_columns].interpolate(method ='linear', limit_direction ='forward')
    return(df)

# In[5]:reformat and clean data
dfc = clean_age(df_raw)
dfc1 = format_age(dfc)
dfc.to_csv(r'demog_covid/data/AgeGroups_cleaned.csv', index = False)

# In[6]: Display charts
df_rea(dfc)
df_dec(dfc)
df_hosp(dfc)

