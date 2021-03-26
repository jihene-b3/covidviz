import  pandas as pd
import numpy as np

# TO IMPROVE
# doesn't show the right number of cases for the moment
# because of the groupby

# return a dataframe with the number of covid cases by departments

def get_cases_by_dep(df_covid, log_scale=True):
  """
  Get the number of covid cases in the dataframe by department.
  :param df_covid: dataframe with covid data
  :type df_covid: pandas.core.frame.DataFrame
  :param log_scale: log scale
  :type log_scale: bool
  """
  cases_dep = df_covid.groupby(['maille_code']).size()
  if log_scale:
    cases_dep = np.log(cases_dep)
  return cases_dep