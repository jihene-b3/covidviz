#%%
import covidmap as cm
import pandas as pd

#%%
# import csv with departments only
df_covid = pd.read_csv(".\covidmap\data\data_covid_clean.csv")
#%%
# change the format of "maille_code" 
# "DEP-33" in "33" for example
df_covid = cm.format_dep(df_covid)

#%%
# get cases (it's not the good number for the moment)
# to improve !
cases_by_dep = cm.get_cases_by_dep(df_covid)

#%%
# plot France map with number of cases by dep
cm.plot_map(cases_by_dep)
# %%
