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
"""
 SCREENING CENTERS IN PUBLIC ACCESS
"""
# %%
# We clean and complete the dataframe 'depis_grand_public' by adding missing informations.
depis_grand_public.drop(['ID', 'finess', 'date_modif'], 1, inplace=True)
depis_grand_public.drop([2388, 2742], inplace=True)

depis_grand_public.loc[1269, 'adresse'] = '6 Rue St Hermeland 50260 SOTTEVAST'
depis_grand_public.loc[1269, 'longitude'] = -1.5945067
depis_grand_public.loc[1269, 'latitude'] = 49.5224947

depis_grand_public.loc[1828, 'longitude'] = 3.409963
depis_grand_public.loc[1828, 'latitude'] = 46.1502923

depis_grand_public.loc[2595, 'longitude'] = 2.1660581
depis_grand_public.loc[2595, 'latitude'] = 48.6789083

depis_grand_public.loc[2595, 'adresse'] = depis_grand_public.loc[2595, 'cpl_loc']

depis_grand_public.loc[2595, 'cpl_loc'] = np.nan

depis_grand_public.loc[2844, 'longitude'] = 0.16686641335383762
depis_grand_public.loc[2844, 'latitude'] = 46.63853367849356

depis_grand_public.loc[3093, 'adresse'] = '286 Av. des Grésillons, 92600 Asnières-sur-Seine'

depis_grand_public.loc[3093, 'tel_rdv'] = '01 85 78 53 43'
depis_grand_public.loc[3093, 'longitude'] = 2.3141661
depis_grand_public.loc[3093, 'latitude'] = 48.9202844

depis_grand_public = depis_grand_public.reset_index()

# We add a column who indicates the department code.
for row in range(len(depis_grand_public)):
    depis_grand_public.loc[row, 'dep'] = depis_grand_public.loc[row, 'id_ej'][: 2]

# %%
# We (quickly) clean the dataframe
dep_fr.drop(
    ['Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7'],
    axis=1,
    inplace=True)

# %%
# We regroup all french departments maps
all_map_dep = {}
for dep_code in dep_fr['maille_code'].tolist():
    all_map_dep[f'{dep_code}'] = cvz.map_dep(f'{dep_code}', dep_fr)

# %%
# We regroup screening centers in public access by department
depis_department_grand_public = {}

for dep_code in dep_fr['maille_code'].tolist():
    depis_department_grand_public[f'{dep_code}'] = depis_grand_public[depis_grand_public['dep'] == f'{dep_code}']

    depis_department_grand_public[f'{dep_code}'] = depis_department_grand_public[f'{dep_code}'].reset_index()

    depis_department_grand_public[f'{dep_code}'].drop(['level_0', 'index'], axis=1, inplace=True) #clean
    depis_department_grand_public[f'{dep_code}'].fillna('-', inplace=True) #replace the NaN by '-' for visualization

# %%
"""
 SCREENING CENTERS IN RESTRICTED ACCESS
"""
# %%
# We clean the dataframe 'depis_acces_restreint'.
depis_acces_restreint.drop(['ID', 'finess', 'date_modif'], 1, inplace=True)

# We add a column who indicates the department code.
for row in range(len(depis_acces_restreint)):
    depis_acces_restreint.loc[row, 'dep'] = str(depis_acces_restreint.loc[row, 'id_ej'])[:2]

# %%
# We regroup screening centers in restricted access by department
depis_department_acces_restreint = {}
for dep_code in dep_fr['maille_code'].tolist():
    depis_department_acces_restreint[f'{dep_code}'] = depis_acces_restreint[depis_acces_restreint['dep'] == f'{dep_code}']

    depis_department_acces_restreint[f'{dep_code}'] = depis_department_acces_restreint[f'{dep_code}'].reset_index()

    depis_department_acces_restreint[f'{dep_code}'].drop(['index'], axis=1, inplace=True) # clean

"""
 not all departments have restricted access screening centers,
 so we clean the dictionary created
 by deleting the keys of departments without screening centers.
"""

dep_acces_restreint_list = []
for dep_code in dep_fr['maille_code'].tolist():
    if (len(depis_department_acces_restreint[f'{dep_code}']) != 0):
        a = f'{dep_code}'
        dep_acces_restreint_list.append(a)
    else:
        del depis_department_acces_restreint[f'{dep_code}']

for dep_code in dep_acces_restreint_list:
    depis_department_acces_restreint[f'{dep_code}'].fillna('-', inplace=True) #replace the NaN by '-' for visualization

# %%
"""
 MAP VISUALIZATION (by department)

We add on the map screening centers (public + private) markers with all info in popups
"""
for dep_code in dep_fr['maille_code'].tolist():
    for i in range(len(depis_department_grand_public[f'{dep_code}'])):

        tooltip1 = f"<strong>{depis_department_grand_public[dep_code].loc[i, 'adresse']}</strong>"

        popup1 = folium.Popup(
            '<h4><b><p style="text-align:center;">{}</p></b></h4><br>'.format(
                depis_department_grand_public[dep_code].loc[i, 'rs']) +
            '<h5><b>Adresse : </b></h5>{}'.format(
                depis_department_grand_public[dep_code].loc[i, 'adresse']) +
            '<br>' +
            '<i>{}</i>'.format(
                depis_department_grand_public[dep_code].loc[i, 'cpl_loc']) +
            '<br>' +
            '<strong><b>Test RT-PCR : </b></strong>{}'.format(
                depis_department_grand_public[dep_code].loc[i, 'do_prel']) +
            '<br>' +
            '<strong><b>Test antigénique : </b></strong>{}'.format(
                depis_department_grand_public[dep_code].loc[i, 'do_antigenic']) +
            '<br>' +
            '<strong><b>Modalités de prélèvement : </b></strong>{}'.format(
                depis_department_grand_public[dep_code].loc[i, 'mod_prel']) +
            '<br>' +
            '<strong><b>Public : </b></strong>{}'.format(
                depis_department_grand_public[dep_code].loc[i, 'public']) +
            '<br>' +
            '<strong><b>Accès : </b></strong>{}'.format(
                depis_department_grand_public[dep_code].loc[i, 'check_rdv']) +
            '<br>' +
            '<h5><b>Horaire : </b></h5>{}'.format(
                depis_department_grand_public[dep_code].loc[i, 'horaire']) +
            '<br>' +
            '<strong><b>Personnes prioritaires : </b></strong>{}'.format(
                depis_department_grand_public[dep_code].loc[i, 'horaire_prio']) +
            '<br>' +
            '<strong><b>Téléphone : </b></strong>{}'.format(str(
                depis_department_grand_public[dep_code].loc[i, 'tel_rdv'])) +
            '<br>' +
            '<strong><b>Site internet : </b></strong>{}'.format(
                depis_department_grand_public[dep_code].loc[i, 'web_rdv']),
            max_width=500)
        folium.Marker(
                location=[
                    depis_department_grand_public[f'{dep_code}'].loc[i, 'latitude'],
                    depis_department_grand_public[f'{dep_code}'].loc[i, 'longitude']
                    ],
                icon=folium.Icon(color='green'),
                popup=popup1,
                tooltip=tooltip1).add_to(all_map_dep[f'{dep_code}'])

for dep_code in dep_acces_restreint_list:
    for i in range(len(depis_department_acces_restreint[f'{dep_code}'])):

        tooltip2 = f"<strong>{depis_department_acces_restreint[dep_code].loc[i,'adresse']}</strong>"

        popup2 = folium.Popup(
            '<h4><b><p style="text-align:center;">{}</p></b></h4><br>'.format(
                depis_department_acces_restreint[dep_code].loc[i, 'rs']) +
            '<h5><b>Adresse : </b></h5>{}'.format(
                depis_department_acces_restreint[dep_code].loc[i, 'adresse']) +
            '<br>' +
            '<i>{}</i>'.format(
                depis_department_acces_restreint[dep_code].loc[i, 'cpl_loc']) +
            '<br>' +
            '<strong><b>Test RT-PCR : </b></strong>{}'.format(
                depis_department_acces_restreint[dep_code].loc[i, 'do_prel']) +
            '<br>' +
            '<strong><b>Test antigénique : </b></strong>{}'.format(
                depis_department_acces_restreint[dep_code].loc[i, 'do_antigenic']) +
            '<br>' +
            '<strong><b>Modalités de prélèvement : </b></strong>{}'.format(
                depis_department_acces_restreint[dep_code].loc[i, 'mod_prel']) +
            '<br>' +
            '<strong><b>Public : </b></strong>{}'.format(
                depis_department_acces_restreint[dep_code].loc[i, 'public']) +
            '<br>' +
            '<strong><b>Accès : </b></strong>{}'.format(
                depis_department_acces_restreint[dep_code].loc[i, 'check_rdv']) +
            '<br>' +
            '<h5><b>Horaire : </b></h5>{}'.format(
                depis_department_acces_restreint[dep_code].loc[i, 'horaire']) +
            '<br>' +
            '<strong><b>Personnes prioritaires : </b></strong>{}'.format(
                depis_department_acces_restreint[dep_code].loc[i, 'horaire_prio']) +
            '<br>' +
            '<strong><b>Téléphone : </b></strong>{}'.format(str(
                depis_department_acces_restreint[dep_code].loc[i, 'tel_rdv'])) +
            '<br>' +
            '<strong><b>Site internet : </b></strong>{}'.format(
                depis_department_acces_restreint[dep_code].loc[i, 'web_rdv']),
            max_width=500)

        folium.Marker(
                location=[
                    depis_department_acces_restreint[f'{dep_code}'].loc[i, 'latitude'],
                    depis_department_acces_restreint[f'{dep_code}'].loc[i, 'longitude']
                    ],
                icon=folium.Icon(color='red'),
                popup=popup2,
                tooltip=tooltip2).add_to(all_map_dep[f'{dep_code}'])

# %%
"""
 SCREENING VISUALIZATION BY GRAPHS
"""
# Loading of data on the number of screenings carried out by age group and / or department
screening_daily = pd.read_csv(
    '../covidviz/data/sp-pos-quot-dep-2021-04-16-19h05.csv',
    delimiter=';',
    low_memory=False)

screening_daily.rename(
    columns={'cl_age90': 'cl_age', 'jour': 'date', 'T': 'Tests number', 'P': 'Positive tests'},
    inplace=True)
# %%
# Grouping all age classes
AGE = pd.DataFrame(screening_daily['cl_age'].unique())
AGE.set_axis(['classe'], axis=1, inplace=True)

# Grouping all departments
DEP = pd.DataFrame(screening_daily['dep'].unique())
DEP.set_axis(['code'], axis=1, inplace=True)

# %%
"""
 Daily screenings by age and dep

We regroup data by age (we will filter by dep in the function).
We add the columns :
    - 'Tests cumul' : 
        indicates the number of cumulative screenings
        since the first day (first line of data), per day.
    - '% positive tests' :
        indicates the percentage of positive screenings.
"""
screening_daily_age_dep = {}

for age in AGE['classe'].tolist():
    screening_daily_age_dep[age] = screening_daily[screening_daily['cl_age'] == age]

    screening_daily_age_dep[age].drop(['cl_age'], axis=1, inplace=True)
    screening_daily_age_dep[age] = screening_daily_age_dep[age].reset_index()
    screening_daily_age_dep[age].drop(['pop', 'index'], axis=1, inplace=True)

    screening_daily_age_dep[age]['Tests cumul'] = screening_daily_age_dep[age]['Tests number'].cumsum()

    screening_daily_age_dep[age]['% positive tests'] = (screening_daily_age_dep[age]['Positive tests']/screening_daily_age_dep[age]['Tests number'])*100

    screening_daily_age_dep[age].fillna(0, inplace=True)

# %%
"""
 Daily screenings by age

We add the columns :
    - 'Tests cumul' : 
        indicates the number of cumulative screenings
        since the first day (first line of data), per day.
    - '% positive tests' :
        indicates the percentage of positive screenings.
"""
screening_daily_age = {}
for age in AGE['classe'].tolist():
    screening_daily_age[age] = screening_daily[screening_daily['cl_age'] == age]

    screening_daily_age[age].drop(['cl_age'], axis=1, inplace=True)
    screening_daily_age[age] = screening_daily_age[age].reset_index()
    screening_daily_age[age] = screening_daily_age[age].set_index('date')

    screening_daily_age[age].index = pd.to_datetime(screening_daily_age[age].index, format="%Y-%m-%d")

    screening_daily_age[age] = screening_daily_age[age].resample("1D").sum()
    screening_daily_age[age].drop(['pop', 'index'], axis=1, inplace=True)

    screening_daily_age[age]['Tests cumul'] = screening_daily_age[age]['Tests number'].cumsum()

    screening_daily_age[age]['% positive tests'] = (screening_daily_age[age]['Positive tests']/screening_daily_age[age]['Tests number'])*100

    screening_daily_age[age] = screening_daily_age[age].reset_index()

# %%
"""
 Daily screenings by dep

We regroup data by dep.
We add the columns :
    - 'Tests cumul' : 
        indicates the number of cumulative screenings
        since the first day (first line of data), per day.
    - '% positive tests' :
        indicates the percentage of positive screenings.
"""
screening_daily_dep = {}
for dep_code in DEP['code'].tolist():
    screening_daily_dep[dep_code] = screening_daily[screening_daily['dep'] == dep_code]

    screening_daily_dep[dep_code].drop(['dep'], axis=1, inplace=True)
    screening_daily_dep[dep_code] = screening_daily_dep[dep_code].reset_index()

    screening_daily_dep[dep_code] = screening_daily_dep[dep_code].set_index('date')

    screening_daily_dep[dep_code].index = pd.to_datetime(screening_daily_dep[dep_code].index, format="%Y-%m-%d")

    screening_daily_dep[dep_code] = screening_daily_dep[dep_code].resample("1D").sum()

    screening_daily_dep[dep_code].drop(['cl_age', 'pop', 'index'],
                                        axis=1, inplace=True)

    screening_daily_dep[dep_code]['Tests cumul'] = screening_daily_dep[dep_code]['Tests number'].cumsum()

    screening_daily_dep[dep_code]['% positive tests'] = (screening_daily_dep[dep_code]['Positive tests']/screening_daily_dep[dep_code]['Tests number'])*100

    screening_daily_dep[dep_code] = screening_daily_dep[dep_code].reset_index()

# %%

# %%
# cvz.daily_test(90, '29', screening_daily_age_dep)
# cvz.daily_test_dep('34', screening_daily_dep)
# cvz.daily_test_age(90, screening_daily_age)

# %%
# cvz.map_dep('29', dep_fr)
# cvz.map_screening('34', all_map_dep)
