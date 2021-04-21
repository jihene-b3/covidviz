import os.path
import sys
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
df_covid = pd.read_csv("covidmap/data/df_covid.csv")
url_dep = 'https://france-geojson.gregoiredavid.fr/repo/departements.geojson'
url_reg = 'https://france-geojson.gregoiredavid.fr/repo/regions.geojson'
departments = gpd.read_file(url_dep)
regions = gpd.read_file(url_reg)

def test_format_granularity():
    df_covid_dep = cvz.choose_granularity(df_covid,"departement")
    df_covid_reg = cvz.choose_granularity(df_covid,"region")
    test_reg = cvz.format_granularity(df_covid_reg, "region")
    test_dep = cvz.format_granularity(df_covid_dep, "departement")
    print(test_dep["maille_code"])
    assert (test_reg["maille_code"][20] == "11")
    assert (test_dep["maille_code"][5] == "16")

def test_choose_columns():
    test = cvz.choose_columns(df_covid, ["date", "maille_code"])
    assert list(test.columns) == ["date", "maille_code"]


def test_choose_granularity():
    test1 = cvz.choose_granularity(df_covid, "departement")
    test2 = cvz.choose_granularity(df_covid, "region")
    assert list(test1.granularite.unique())[0] == "departement"
    assert list(test2.granularite.unique())[0] == "region"

def test_Map_covid():
    test = cvz.Map_covid(df_covid, departments, "deces")
    assert type(test) == cm.vis.plot_map.Map_covid
