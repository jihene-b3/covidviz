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
death_dep = pd.DataFrame(df_covid.sort_values(['date']))
date_list = df_covid.groupby(['date']).size()

df_jour = death_dep.loc[death_dep['date'] == '2021-03-11']

#%%
init_view = pdk.ViewState(latitude=50.01200, longitude=3.17270, zoom=6, max_zoom=16, pitch=45, bearing=0)

#%%
departments = departments.assign(deces=0)
for i in df_jour.index :
    departments.loc[departments["code"] == df_jour.loc[i, "maille_code"], "deces"] = df_jour.loc[i, "deces"]
#%%
map_covid_layer = pdk.Layer(
    "GeoJsonLayer",
    departments,
    opacity=0.8,
    stroked=False,
    filled=True,
    extruded=True,
    wireframe=True,
    get_elevation="deces*100",
    get_fill_color="[255, deces/20, deces/20]",
    get_line_color=[255, 255, 255],
)


#%%

# Slider widget 
#time_slider  = IntSlider(value=2010, min=2010, max=2021, step=1)
#play = Play(value=2010, min=2010, max=2021, step=1, description="Press play", interval=1_000)
#jslink((play,'value'), (time_slider, 'value'))
#layout = HBox([time_slider, play])

#%%
map_covid = pdk.Deck(layers=[map_covid_layer], initial_view_state=init_view)


#%%

def update_plot(date_index):
    date = date_list.index[date_index]
    df_jour = death_dep.loc[death_dep['date'] == date]
    
    for i in departments.index :
        departments.loc[i,"deces"] = 0
    for i in df_jour.index :
        departments.loc[departments["code"] == df_jour.loc[i,"maille_code"],"deces"] = df_jour.loc[i,"deces"]
    print(date)
    map_covid_layer.data = departments
    return map_covid.update()

#%%
# widgets
time_slider = ipywidgets.IntSlider(value=0, min=0, max=date_list.size-1, step=1)
play = ipywidgets.Play(value=0, min=0, max=date_list.size-1, step=1, description='Press play', interval=50)
ipywidgets.jslink((play, 'value'), (time_slider, 'value'))
layout = ipywidgets.HBox([time_slider, play])


#%%
interaction = interactive_output(update_plot, {'date_index': time_slider})

#%%
#map_covid.to_html("geojson_layer.html")
display(layout, interaction)
map_covid.update()
map_covid.show()
# %%
