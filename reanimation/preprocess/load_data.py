import pandas as pd

confinement_1 = pd.read_csv('reanimation/data/data_covid_clean.csv')
deconfinement_1 = pd.read_csv('reanimation/data/data_covid_clean.csv')
confinement_2 = pd.read_csv('reanimation/data/data_covid_clean.csv')
curfew = pd.read_csv('reanimation/data/data_covid_clean.csv')
rea_all = pd.read_csv('reanimation/data/data_covid_clean.csv')
beds_in_rea_dep = pd.read_csv('reanimation/data/bed_rea_dep.csv', delimiter=';')
beds_in_rea_reg = pd.read_csv('reanimation/data/bed_rea_reg.csv', delimiter=';') 