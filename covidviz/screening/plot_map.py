import pandas as pd
import numpy as np
import folium

"""
 SCREENING CENTERS IN PUBLIC ACCESS
"""


def clean_public_centers(depis_grand_public):
    """
    clean_public_centers

    We clean and complete the dataframe 'depis_grand_public' by adding missing informations.
    We add a column who indicates the department code.

    :param depis_grand_public: all informations about screening centers in public access in France
    :type depis_grand_public: dataframe
    :return: depis_grand_public cleaned
    :rtype: dataframe
    """
    df = depis_grand_public.copy()
    df.drop(['ID', 'finess', 'date_modif'], 1, inplace=True)
    df.drop([2388, 2742], inplace=True)

    df.loc[1269, 'adresse'] = '6 Rue St Hermeland 50260 SOTTEVAST'
    df.loc[1269, 'longitude'] = -1.5945067
    df.loc[1269, 'latitude'] = 49.5224947

    df.loc[1828, 'longitude'] = 3.409963
    df.loc[1828, 'latitude'] = 46.1502923

    df.loc[2595, 'longitude'] = 2.1660581
    df.loc[2595, 'latitude'] = 48.6789083

    df.loc[2595, 'adresse'] = df.loc[2595, 'cpl_loc']

    df.loc[2595, 'cpl_loc'] = np.nan

    df.loc[2844, 'longitude'] = 0.16686641335383762
    df.loc[2844, 'latitude'] = 46.63853367849356

    df.loc[3093, 'adresse'] = '286 Av. des Grésillons, 92600 Asnières-sur-Seine'

    df.loc[3093, 'tel_rdv'] = '01 85 78 53 43'
    df.loc[3093, 'longitude'] = 2.3141661
    df.loc[3093, 'latitude'] = 48.9202844

    df = df.reset_index()

    for row in range(len(df)):
        df.loc[row, 'dep'] = df.loc[row, 'id_ej'][: 2]
    return df


def clean_dep(dep_fr):
    """
    clean_dep

    We (quickly) clean the dataframe

    :param dep_fr: coordonates of french departments
    :type dep_fr: dataframe
    :return: coordonates of french departments (cleaned)
    :rtype: dataframe
    """
    df = dep_fr.copy()
    df.drop(
        ['Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7'],
        axis=1,
        inplace=True)
    return df


def map_dep(department, dep_fr):
    """
    map_dep

    :param department: french department or DOM code
    :type department: str
    :param dep_fr: all french departments and DOM coordinates
    :type dep_fr: dataframe
    :return: the french department (or DOM) map selected
    :rtype: Folium Map Object
    """
    df = dep_fr.copy()
    df = clean_dep(df)
    dep_map = folium.Map(
        location=[
            df[df['maille_code'] == department]['Latitude'],
            df[df['maille_code'] == department]['Longitude']
            ], zoom_start=8)
    return dep_map


def regroup_map(dep_fr):
    """
    regroup_map

    :param dep_fr: all french departments and DOM coordinates
    :type dep_fr: dataframe
    :return: all french departments maps regrouped
    :rtype: dict
    """
    df = dep_fr.copy()
    df = clean_dep(df)
    all_map_dep = {}
    for dep_code in df['maille_code'].tolist():
        all_map_dep[f'{dep_code}'] = map_dep(f'{dep_code}', df)
    return all_map_dep


def regroup_public_center_by_dep(depis_grand_public, dep_fr):
    """
    regroup_public_center_by_dep

    :param depis_grand_public: all informations about screening centers in public access in France
    :type depis_grand_public: dataframe
    :param dep_fr: all french departments and DOM coordinates
    :type dep_fr: dataframe
    :return: screening centers in public access by department regrouped
    :rtype: dict
    """
    df = depis_grand_public.copy()
    df = clean_public_centers(df)
    df1 = dep_fr.copy()
    df1 = clean_dep(df1)
    depis_department_grand_public = {}

    for dep_code in df1['maille_code'].tolist():
        depis_department_grand_public[f'{dep_code}'] = df[df['dep'] == f'{dep_code}']

        depis_department_grand_public[f'{dep_code}'] = depis_department_grand_public[f'{dep_code}'].reset_index()

        depis_department_grand_public[f'{dep_code}'].drop(['level_0', 'index'], axis=1, inplace=True) #clean
        depis_department_grand_public[f'{dep_code}'].fillna('-', inplace=True) #replace the NaN by '-' for visualization
    return depis_department_grand_public


"""
 SCREENING CENTERS IN RESTRICTED ACCESS
"""


def clean_private_centers(depis_acces_restreint):
    """
    clean_private_centers
    We clean the dataframe 'depis_acces_restreint'
    We add a column who indicates the department code.

    :param depis_acces_restreint: all informtations about screening centers in restricted access in France
    :type depis_acces_restreint: dataframe
    :return: the dataframe 'depis_acces_restreint' cleaned
    :rtype: dataframe
    """
    df = depis_acces_restreint.copy()
    df.drop(['ID', 'finess', 'date_modif'], 1, inplace=True)
    for row in range(len(df)):
        df.loc[row, 'dep'] = str(df.loc[row, 'id_ej'])[:2]
    return df


def regroup_private_center_by_dep(depis_acces_restreint, dep_fr):
    """
    regroup_private_center_by_dep

    :param depis_acces_restreint: all informtations about screening centers in restricted access in France
    :type depis_acces_restreint: dataframe
    :param dep_fr: all french departments and DOM coordinates
    :type dep_fr: dataframe
    :return: screening centers in restricted access by department regrouped
    :rtype: dict
    """
    df = depis_acces_restreint.copy()
    df = clean_private_centers(df)
    df1 = dep_fr.copy()
    df1 = clean_dep(df1)
    depis_department_acces_restreint = {}
    for dep_code in df1['maille_code'].tolist():
        depis_department_acces_restreint[f'{dep_code}'] = df[df['dep'] == f'{dep_code}']

        depis_department_acces_restreint[f'{dep_code}'] = depis_department_acces_restreint[f'{dep_code}'].reset_index()

        depis_department_acces_restreint[f'{dep_code}'].drop(['index'], axis=1, inplace=True) # clean
    return (depis_department_acces_restreint)


"""
 MAP VISUALIZATION (by department)
"""


def markers_set(dep_fr, depis_grand_public, depis_acces_restreint):
    """
    markers_set

    Remark :
    not all departments have restricted access screening centers,
    so we clean the dictionary 'depis_department_acces_restreint' created
    by deleting the keys of departments without screening centers.

    :param dep_fr: all french departments coordinates
    :type dep_fr: dataframe
    :param depis_grand_public: data on screening centers in public access in France
    :type depis_grand_public: dataframe
    :param depis_acces_restreint: data on screening centers in restricted access in France
    :type depis_acces_restreint: dataframe
    :return: [description]
    :rtype: [type]
    """
    df = dep_fr.copy()
    df = clean_dep(df)
    depis_department_grand_public = regroup_public_center_by_dep(depis_grand_public, dep_fr)
    all_map_dep = regroup_map(dep_fr)
    depis_department_acces_restreint = regroup_private_center_by_dep(depis_acces_restreint, dep_fr)

    for dep_code in df['maille_code'].tolist():
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

    dep_acces_restreint_list = []
    for dep_code in df['maille_code'].tolist():
        if (len(depis_department_acces_restreint[f'{dep_code}']) != 0):
            a = f'{dep_code}'
            dep_acces_restreint_list.append(a)
        else:
            del depis_department_acces_restreint[f'{dep_code}']

    for dep_code in dep_acces_restreint_list:
        depis_department_acces_restreint[f'{dep_code}'].fillna('-', inplace=True) #replace the NaN by '-' for visualization

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
    return all_map_dep


def map_screening(dep_code, dep_fr, depis_grand_public, depis_acces_restreint):
    """
    map_screening

    :param dep_code: french department code like '34' for Hérault
    :type dep_code: str
    :param dep_fr: all french departments coordinates
    :type dep_fr: dataframe
    :param depis_grand_public: data on screening centers in public access in France
    :type depis_grand_public: dataframe
    :param depis_acces_restreint: data on screening centers in restricted access in France
    :type depis_acces_restreint: dataframe
    :return: the department selected map with all markers, with all screening centers informations
    :rtype: Folium Map Object
    """
    all_map_dep = markers_set(dep_fr, depis_grand_public, depis_acces_restreint) 
    return(all_map_dep[f'{dep_code}'])
