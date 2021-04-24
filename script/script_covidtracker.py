#%%
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz
from covidviz import data 
from covidviz.preprocess.clean_df import choose_columns, choose_granularity
import pandas as pd

# %%
data = cvz.choose_columns(cvz.Load_db.save_as_df(), ['date', 'granularite', 'maille_code', 'maille_nom', 'reanimation','deces', 'cas_confirmes','gueris','source_nom'])

# %%
