# %%
import pandas as pd
import numpy as np
import datetime

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

import os.path, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)

import covidviz as cvz

# %%
df_raw = cvz.choose_columns(
    cvz.Load_db.save_as_df(),
    [
        'date',
        'granularite',
        'maille_code',
        'maille_nom',
        'reanimation',
        'source_nom'
    ]
)

# we filtred data by department
df_dep = cvz.choose_granularity(df_raw, "departement")
# we filtred data by region
df_reg = cvz.choose_granularity(df_raw, "region")


# %%
def test_clean_df_dep():
    df = cvz.clean_df_dep(df_dep)
    assert (df.loc['2020-01-24', 'maille_code'][1] == 'DEP-17')


# %%
def test_regroup_by_dep():
    dict_dep = cvz.regroup_by_dep(df_dep)
    assert (dict_dep['Hérault'].columns == 'Hérault')


# %%
def test_clean_df_reg():
    df = cvz.clean_df_reg(df_reg)
    assert (df.loc['2020-03-17', 'maille_nom'][1] == 'Guadeloupe')


# %%
def test_create_df_all_reg():
    df = cvz.create_df_all_reg(df_reg)
    assert (df.columns[:1] == 'date')
