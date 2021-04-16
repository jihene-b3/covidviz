import os.path
import sys
import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore", category=RuntimeWarning)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)

import covidmap as cm

def test_format_dep():
    df_covid = pd.read_csv("../data/data_covid_clean.csv")
    test = cm.format_dep(df_covid)
    assert test["maille_code"][0] == "33"
