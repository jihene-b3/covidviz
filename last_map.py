#%%
import pydeck as pdk
import covidmap as cm
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
df_covid_raw = cm.Load_db().save_as_df()

# columns we want to keep 
columns = ['date', 'granularite', 'maille_code', 'maille_nom','cas_confirmes', 'hospitalises','deces']
df_covid_cleaned = cm.choose_columns(df_covid_raw, columns)

# keep only departements
df_covid_cleaned_dep = cm.choose_granularity(df_covid_cleaned,"departement")

# format departements
df_covid = cm.format_dep(df_covid_cleaned_dep)

#%%
map = cm.Map_covid(df_covid, departments, "deces")
map.plot_all()
