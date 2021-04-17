import os.path
import sys
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)

import covidmap as cm

def test_format_granularity():
    df_covid = pd.read_csv("../data/data_covid_clean.csv")
    test_reg = cm.format_granularity(df_covid, "region")
    test_dep = cm.format_granularity(df_covid, "departement")
    assert (test_reg["maille_code"][0] == "11" and test_dep["maille_code"][0] == "33")


