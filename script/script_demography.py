#%%
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz
from covidviz import data 
from  covidviz.covidtime.utils_plot import df_plot_dec,df_plot_rea,df_plot_hosp,df_plot_gender
import pandas as pd
from covidviz.preprocess.format_data import clean_gender,clean_age,format_age,remove_nan,group
# %%

data_age = pd.read_csv('covidviz/data/AgeGroups.csv',sep=';')
data_gender = pd.read_csv('covidviz/data/age_gender.csv',sep=';')

# %%
dfc = clean_age(data_age)
dfc1 = remove_nan(dfc)
dfC = format_age(dfc1)

# %%
df_plot_rea(dfC)
df_plot_hosp(dfC)
df_plot_dec(dfC)

# %%
df = clean_gender(data_gender)
df1 = format_age(df)
group(df1)

# %%
df_plot_gender(df1)
