import  pandas as pd
import numpy as np

# TO IMPROVE
# doesn't show the right number of cases for the moment
# because of the groupby

# return a dataframe with the number of covid cases by departments

def get_cases_by_dep(df_covid, log_scale=True):
  cases_dep = df_covid.groupby(['maille_code']).size()
  if log_scale:
    cases_dep = np.log(cases_dep)
  return cases_dep