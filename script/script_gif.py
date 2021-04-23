#%%

# import packages :
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz
import pandas as pd
import pandas_alive


#%%
# load data from covidviz 

_data = cvz.choose_columns(cvz.Load_db.save_as_df(), ['date', 'granularite', 'maille_code', 'maille_nom', 'reanimation','deces', 'cas_confirmes','gueris','source_nom'])

_data_department = cvz.choose_granularity(_data, 'departement')

_data_department = cvz.adapt_time(_data_department)

_data_region = cvz.choose_granularity(_data, 'region')
_data_region = cvz.adapt_time(_data_department)
#%%

df_clean_dep_death = cvz.data_treatment_by_option(_data_department, "deces")

cvz.plot_animation(df_clean_dep_death, "departement", "deces")


#%%
