#%%
import pandas as pd
import numpy as np
import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz
import plotly.express as px
#%%
# Loading 'data_covid.csv' from covidmap
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

# %%
cvz.icu_dep_display('since 1st confinement', df_dep)

# %%
