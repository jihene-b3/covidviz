# %%
import pandas as pd
import plotly.express as px
import numpy as np
import os
import sys
import folium

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz


# %%



"""
 Loading data on the screening map
"""


# all informations about screening centers in public access in France

grand_public_path = '../covidviz/data/scr_public_centers.csv'
depis_grand_public = pd.read_csv(grand_public_path)

# all informtations about screening centers in restricted access in France

acces_restreint_path = '../covidviz/data/scr_private_centers.csv'
depis_acces_restreint = pd.read_csv(acces_restreint_path)

# coordonates of french departments

dep_fr = pd.read_csv('../covidviz/data/depart_fr_coord.csv', delimiter=';')

# %%
cvz.map_screening('34', dep_fr, depis_grand_public, depis_acces_restreint)
# %%



"""
 SCREENING VISUALIZATION BY GRAPHS
"""


# Loading of data on the number of screenings carried out by age group and / or department

screening_daily = pd.read_csv(
    '../covidviz/data/sp-pos-quot-dep-2021-04-16-19h05.csv',
    delimiter=';',
    low_memory=False)
# %%
cvz.daily_test(9, '34', screening_daily)
cvz.daily_test_dep('34', screening_daily)
cvz.daily_test_age(9, screening_daily)
