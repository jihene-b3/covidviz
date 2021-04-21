#%%
import pandas as pd
import plotly.express as px
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz

#%%
screening_daily = pd.read_csv('../covidviz/data/sp-pos-quot-dep-2021-04-16-19h05.csv', delimiter=';', low_memory=False)

#%%
screening_daily.rename(columns={'cl_age90' : 'cl_age', 'jour' : 'date', 'T' : 'Tests number', 'P' : 'Positive tests'}, inplace=True)

#%%
DEP = pd.DataFrame(screening_daily['dep'].unique())
DEP.set_axis(['code'], axis=1, inplace=True)

#%%
cvz.daily_test(90,'29')
