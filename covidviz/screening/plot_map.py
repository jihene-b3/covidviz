import pandas as pd
import numpy as np
import folium

"""
 Clean the dataframe of public screening centers in France
"""

def get_public_centers(depis_grand_public):

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

    for row in range(len(depis_grand_public)):
        depis_grand_public.loc[row, 'dep'] = depis_grand_public.loc[row, 'id_ej'][:2]

    return depis_grand_public


def get_departments_location(dep_fr):
    dep_fr.drop([
        'Unnamed: 4',
        'Unnamed: 5',
        'Unnamed: 6',
        'Unnamed: 7'
        ],
        axis=1,
        inplace=True)
    return dep_fr


def map_dep(department):
    dep_map = folium.Map(
        location=[
            dep_fr[dep_fr['maille_code'] == f'{department}']['Latitude'],
            dep_fr[dep_fr['maille_code'] == f'{department}']['Longitude']
            ], zoom_start=8)
    return dep_map


def regroup_by_department(dep_fr):

    all_map_dep = {}

    for dep_code in dep_fr['maille_code'].tolist():
        all_map_dep[f'{dep_code}'] = map_dep(f'{dep_code}')

    return all_map_dep


def public_centers_by_dep(depis_grand_public):

    depis_department_grand_public = {}

    for dep_code in dep_fr['maille_code'].tolist():
        depis_department_grand_public[f'{dep_code}'] = depis_grand_public[depis_grand_public['dep'] == f'{dep_code}']

        depis_department_grand_public[f'{dep_code}'] = depis_department_grand_public[f'{dep_code}'].reset_index()

        depis_department_grand_public[f'{dep_code}'].drop(['level_0', 'index'], axis=1, inplace=True)
        depis_department_grand_public[f'{dep_code}'].fillna('-', inplace=True)

    return depis_department_grand_public


"""
 Clean the dataframe of private screening centers in France
"""


def get_private_centers(depis_acces_restreint):

    depis_acces_restreint.drop(['ID', 'finess', 'date_modif'], 1, inplace=True)

    for row in range(len(depis_acces_restreint)):
        depis_acces_restreint.loc[row, 'dep'] = str(depis_acces_restreint.loc[row, 'id_ej'])[:2]

    return depis_acces_restreint


def private_centers_by_dep(depis_acces_restreint):

    depis_department_acces_restreint = {}
    for dep_code in dep_fr['maille_code'].tolist():
        depis_department_acces_restreint[f'{dep_code}'] = depis_acces_restreint[depis_acces_restreint['dep'] == f'{dep_code}']

        depis_department_acces_restreint[f'{dep_code}'] = depis_department_acces_restreint[f'{dep_code}'].reset_index()

        depis_department_acces_restreint[f'{dep_code}'].drop(['index'], axis=1, inplace=True)

        dep_acces_restreint_list = []
        for dep_code in dep_fr['maille_code'].tolist():
            if (len(depis_department_acces_restreint[f'{dep_code}']) != 0):
                a = f'{dep_code}'
                dep_acces_restreint_list.append(a)
            else:
                del depis_department_acces_restreint[f'{dep_code}']

        for dep_code in dep_acces_restreint_list:
            depis_department_acces_restreint[f'{dep_code}'].fillna('-', inplace=True)

    return depis_department_acces_restreint


"""
 Create the hole map
 """


def map_screening(dep_code):
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

            icon1 = folium.Icon(color='green')

            folium.Marker(
                location=[
                    depis_department_grand_public[f'{dep_code}'].loc[i, 'latitude'],
                    depis_department_grand_public[f'{dep_code}'].loc[i, 'longitude']
                    ],
                icon=icon1,
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

            icon2 = folium.Icon(color='red')

            folium.Marker(
                location=[
                    depis_department_acces_restreint[f'{dep_code}'].loc[i, 'latitude'],
                    depis_department_acces_restreint[f'{dep_code}'].loc[i, 'longitude']
                    ],
                icon=icon2,
                popup=popup2,
                tooltip=tooltip2).add_to(all_map_dep[f'{dep_code}'])

    return(all_map_dep[f'{dep_code}'])
























