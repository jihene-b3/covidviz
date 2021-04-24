import pandas as pd
import datetime
import os, sys
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)

import covidviz as cvz

df_covid = pd.read_csv("covidviz/data/df_covid.csv")


def test_data_treatment():
    df_dep = cvz.choose_granularity(df_covid,"departement")
    test = cvz.data_treatment_by_option(df_dep, "deces")
    assert (test.loc["2020-02-26", "Ain"] >= 0)
    
