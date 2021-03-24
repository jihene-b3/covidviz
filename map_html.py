import covidmap as cm
import pandas as pd

# import csv with departments only
df_covid = pd.read_csv(".\covidmap\data\data_covid_clean.csv")

# change the format of "maille_code" 
# "DEP-33" in "33" for example
for i in range(df_covid.shape[0]) :
    df_covid["maille_code"][i] = df_covid["maille_code"][i][4:]

# get cases (it's not the good number for the moment)
# to improve !
cases_by_dep = cm.get_cases_by_dep(df_covid)

# plot France map with number of cases by dep
cm.plot_map(cases_by_dep)