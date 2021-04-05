#%%
import pydeck as pdk
import covidmap as cm
import pandas as pd
import geopandas as gpd
from ipywidgets import interact, interactive_output, Play, jslink, HBox, IntSlider

#%%
url_dep = 'https://france-geojson.gregoiredavid.fr/repo/departements.geojson'
url_reg = 'https://france-geojson.gregoiredavid.fr/repo/regions.geojson'

#%%
departments = gpd.read_file(url_dep)
regions = gpd.read_file(url_reg)
df_covid_raw = pd.read_csv("covidmap/data/data_covid_clean.csv")
df_covid = cm.format_dep(df_covid_raw)

#%%
cases_dep = pd.DataFrame(df_covid.sort_values(['date']))
date_list= df_covid.groupby(['date']).size()

df_jour = cases_dep.loc[cases_dep['date']=='2021-03-11']
#%%
DATA_URL = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/geojson/vancouver-blocks.json"
#%%
init_view = pdk.ViewState(latitude=50.01200, longitude=3.17270, zoom=6, max_zoom=16, pitch=45, bearing=0)

#%%
departments = departments.assign(deces=0)
for i in df_jour.index :
    departments.loc[departments["code"]==df_jour.loc[i,"maille_code"],"deces"] = df_jour.loc[i,"deces"]
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


#%%

time_slider  = IntSlider(value=2010, min=2010, max=2021, step=1)
play = Play(value=2010, min=2010, max=2021, step=1, description="Press play", interval=1_000)
jslink((play,'value'), (time_slider, 'value'))
layout = HBox([time_slider, play])

#%%
map_covid = pdk.Deck(layers=[map_covid_layer], initial_view_state=init_view)


#%%

def update_plot(code):
    map_covid_layer.data = departments[departments['code'] == code]
    return map_covid.update()


#%%
#interaction = interactive_output(update_plot, {'code': time_slider})
#display(layout, interaction)

#%%

#%%
map_covid.to_html("geojson_layer.html")
#map_covid.show()