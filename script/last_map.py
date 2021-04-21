#%%
import pydeck as pdk
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz
import pandas as pd
import geopandas as gpd
import ipywidgets
from ipywidgets import interact, interactive_output, Play, jslink, HBox, IntSlider

#%%
url_dep = 'https://france-geojson.gregoiredavid.fr/repo/departements.geojson'
url_reg = 'https://france-geojson.gregoiredavid.fr/repo/regions.geojson'

#%%
departments = gpd.read_file(url_dep)
regions = gpd.read_file(url_reg)

#%%
# import covid data 
df_covid_raw = cvz.Load_db().save_as_df()

# columns we want to keep 
columns = ['date', 'granularite', 'maille_code', 'maille_nom','cas_confirmes', 'hospitalises','deces']
df_covid_cleaned = cvz.choose_columns(df_covid_raw, columns)

# keep only departements
df_covid_cleaned_dep = cvz.choose_granularity(df_covid_cleaned,"departement")

# format departements
df_covid = cvz.format_granularity(df_covid_cleaned_dep, "departement")

#%%
map = cvz.Map_covid(df_covid, departments, "deces")
map.plot_all()

#%%
map = cvz.Map_covid(df_covid, departments, "hospitalises")
map.plot_all()


# %%

df_covid_cleaned_reg = cvz.choose_granularity(df_covid_cleaned,"region")

# format regions
df_covid_reg = cvz.format_granularity(df_covid_cleaned_reg, "region")

# %%
map = cvz.Map_covid(df_covid_reg, regions, "deces")
map.plot_all()
# %%
map = cvz.Map_covid(df_covid_reg, regions, "hospitalises")
map.plot_all()
# %%
