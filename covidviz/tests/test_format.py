import os.path, sys
import numpy as np
import geopandas as gpd
import pandas as pd

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)
import covidviz as cvz

# Global variables :
df_covid = pd.read_csv("covidviz/data/df_covid.csv")
data_age = pd.read_csv('covidviz/data/AgeGroups.csv', sep=';')
data_gender = pd.read_csv('covidviz/data/age_gender.csv', sep=';')


def test_format_granularity():
    df_covid_dep = cvz.choose_granularity(df_covid,"departement")
    df_covid_reg = cvz.choose_granularity(df_covid,"region")
    test_reg = cvz.format_granularity(df_covid_reg, "region")
    test_dep = cvz.format_granularity(df_covid_dep, "departement")
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


def test_clean_age():
    test = cvz.clean_age(data_age)
    assert (test.loc[11, "nb_hosp"] >= 0)
    assert (list(test.columns)[1] == "age")


def test_clean_gender():
    test = cvz.clean_gender(data_gender)
    assert not('fra' in list(test.columns))
    assert (list(test.columns)[0] == "week")


def test_format_age():
    test = cvz.format_age(cvz.clean_age(data_age))
    print(test["AgeGroup"])
    assert (test['AgeGroup'][11] == '[0,9]')

