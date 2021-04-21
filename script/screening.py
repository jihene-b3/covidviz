#%%
import pandas as pd
import plotly.express as px
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz


#%%
grand_public_path = '../covidviz/data/scr_public_centers.csv'
acces_restreint_path = '../covidviz/data/scr_private_centers.csv'
depis_grand_public = pd.read_csv(grand_public_path)
depis_acces_restreint = pd.read_csv(acces_restreint_path)
dep_fr = pd.read_csv('../covidviz/data/depart_fr_coord.csv', delimiter=';')


#%%
screening_daily = pd.read_csv(
    '../covidviz/data/sp-pos-quot-dep-2021-04-16-19h05.csv',
    delimiter=';',
    low_memory=False)

screening_daily.rename(
    columns={'cl_age90': 'cl_age',
             'jour': 'date',
             'T': 'Tests number',
             'P': 'Positive tests'},
    inplace=True)

#%%

cvz.daily_test(90,'29')
