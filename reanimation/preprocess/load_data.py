import pandas as pd
rea_data_path = 'reanimation/data/data_covid_clean.csv'

confinement_1 = pd.read_csv(rea_data_path)
deconfinement_1 = pd.read_csv(rea_data_path)
confinement_2 = pd.read_csv(rea_data_path)
curfew = pd.read_csv(rea_data_path)
rea_all = pd.read_csv(rea_data_path)
beds_in_rea_dep = pd.read_csv('reanimation/data/bed_rea_dep.csv',
                              delimiter=';')
beds_in_rea_reg = pd.read_csv('reanimation/data/bed_rea_reg.csv',
                              delimiter=';')
