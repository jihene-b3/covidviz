#%%

# import packages :
import pandas as pd
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz
from IPython.display import display, Markdown
from covidviz.preprocess.clean_df import choose_columns,choose_granularity
#from covidviz.io.load_db import Load_db

#%%
data = cvz.choose_columns(cvz.Load_db.save_as_df(), ['date', 'granularite', 'maille_code', 'maille_nom', 'reanimation','deces', 'cas_confirmes','gueris','source_nom'])
#%%
data = cvz.enable_time_series_plot(data, timein_field="date", timeseries_field_out="t")

#%%
maille_active = 'FRA'
fra = cvz.data_preproc(data, maille_active)
fra.tail(10)

#%%
_ = cvz.plots_maille_code(maille_active='FRA', start_date='2020-04-01')

#%% Zomm in the period after the last lockdown
_ = cvz.plots_maille_code(maille_active='FRA', start_date='2021-01-01')

#%%
_ = cvz.plots_maille_code(maille_active='REG-76')

#%%list_reg = [r for r in data["maille_code"].unique() if "REG" in r]
list_reg = [r for r in data["maille_code"].unique() if "REG" in r]
for reg in list_reg:
    cvz.data_preproc(data, reg)