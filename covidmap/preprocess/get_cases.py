import  pandas as pd
import numpy as np

# TO IMPROVE
# doesn't show the right number of cases for the moment
# because of the groupby

# return a dataframe with the number of covid cases by departments
## ideas  
# create a function with a for loop that iterates over the list of elements in column "maille-code" : then df_covid["maille_code"=="DEP-"+ str(i)] 
# or use df_covid[df_covid.maille_code.str.contains('Dep-'+ str(i))]
# issue to think about : DEP-2A and DEP-2B 
# maybe it would be easier to list the elements of the column maille_nom, then do the iteration over the list of characters of all french departments.

def get_cases_by_dep(df_covid, log_scale=True):
  cases_dep = df_covid.groupby(['maille_code']).size()
  if log_scale:
    cases_dep = np.log(cases_dep)
  return cases_dep