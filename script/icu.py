#%%
import pandas as pd
import numpy as np
import plotly.express as px
import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz

# %%
    """
     ICU by department
    """
# %%
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
#we filtred data by department
df_dep = cvz.choose_granularity(df_raw, "departement")
#we filtred data by region
df_reg = cvz.choose_granularity(df_raw, "region")

# %%
# lineplot for all departments in different periods
cvz.icu_dep_display('since 1st confinement', df_dep)
cvz.icu_dep_display('during 1st confinement', df_dep)
cvz.icu_dep_display('during deconfinement', df_dep)
cvz.icu_dep_display('during 2nd confinement', df_dep)
cvz.icu_dep_display('during curfew', df_dep)
cvz.icu_dep_display('during 3rd confinement', df_dep)

# %%
"""
 ICU by region
"""

# %%
cvz.icu_reg_display('since 1st confinement', df_reg) # lineplot for all regions since 1st confinement 
cvz.icu_by_reg_display('since 1st confinement', 'Occitanie', df_dep) # lineplot for Occitanie since 1st confinement 
cvz.icu_all_reg_display(df_reg) #ICU flux in France (with all regions) since 1st confinement
cvz.icu_reg_repartition(df_reg) #Regional repartition of ICU during Covid19 crisis
cvz.heat_map_icu_reg(df_reg) #Regional saturation in % in ICU during Covid19 crisis
