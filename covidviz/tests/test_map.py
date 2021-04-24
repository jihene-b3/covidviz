import os.path, sys
import numpy as np
import geopandas as gpd
import pandas as pd
import ipywidgets
from ipywidgets import interact, interactive_output, Play, jslink, HBox, IntSlider

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)
import covidviz as cvz

# Global variables :
df_covid = pd.read_csv("covidviz/data/df_covid.csv")

url_dep = 'https://france-geojson.gregoiredavid.fr/repo/departements.geojson'
url_reg = 'https://france-geojson.gregoiredavid.fr/repo/regions.geojson'
departments = gpd.read_file(url_dep)
regions = gpd.read_file(url_reg)

def test_Map_covid():
    test = cvz.Map_covid(df_covid, departments, "deces")
    assert type(test) == cvz.covidmap.plot_map.Map_covid
