#%%
from covidviz import data 
from covidviz.preprocess.clean_df import choose_columns, choose_granularity
import matplotlib.pyplot as plt 
import pandas as pd
import matplotlib.ticker as mtick
from covidviz.covidtime.plot_covidtracker import ratio

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz

# %%
a = cvz.Load_db.save_as_df()
data = cvz.choose_columns(a, ['date', 'granularite', 'maille_code', 'maille_nom', 'reanimation','deces', 'cas_confirmes','gueris','hospitalises','source_nom'])

# %%
data = cvz.choose_granularity(data, 'departement')

# %%
data['date'] = pd.to_datetime(data['date'])

# %%
gb_data= data[data['date'] == data['date'].max()].reset_index()
current_date = data['date'].max().strftime('%d/%m/%Y')
current_date_file = gb_data['date'].max().strftime('%d/%m/%Y')
#hospitalisees total = hospitalises + gueris
data_ratio_hospitalises = (gb_data['deces'] / (gb_data['hospitalises'] + gb_data['gueris'])) * 100
data_hospitalises = gb_data['hospitalises'] + gb_data['gueris']
data_deces = gb_data['deces']
data_depcode = gb_data['maille_nom']

# %%
nbhospitalises_80p = data_hospitalises.sum() * 0.80
min_value_80p = data_hospitalises.loc[data_hospitalises[data_hospitalises.sort_values(ascending=False).cumsum() <= nbhospitalises_80p].index].min()

# %%

cvz.ratio(gb_data, data_depcode, data_ratio_hospitalises,current_date, data_hospitalises, current_date_file, min_value_80p , nbhospitalises_80p) 

# %%
