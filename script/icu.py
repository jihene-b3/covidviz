#%%
import pandas as pd
import numpy as np
import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz
from covidviz.icu.department import *
from covidviz.icu.region import *
import plotly.express as px
#%%
# Loading data
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
# %%
df_dep = cvz.choose_granularity(df_raw, "departement")
df_reg = cvz.choose_granularity(df_raw, "region")

#%%
df_dep = format_df_dep(df_raw)
df_reg = format_df_reg(df_raw)

#%%
dict_dep = regroup_by_dep(df_dep)
dict_reg = regroup_by_reg(df_reg)

#%%
df_all_dep = create_df_all_dep(df_dep, dict_dep)
df_all_reg = create_df_all_reg(df_reg, dict_reg)
# %%
icu_dep_all(df_all_dep)

# %%
icu_reg_all(df_all_reg)

# %%
