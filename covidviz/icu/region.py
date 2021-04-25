import os.path, sys, time
import pandas as pd
import numpy as np
import datetime
import plotly.express as px
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz

# ICU IN FRENCH REGIONS



def clean_df_reg(df_reg):
    """
    clean_df_reg

    We generate a DataFrame of ICU in french regions,
    with keeping one source : 'OpenCOVID19-fr'

    :param df_reg: data covid filtred by region
    :type df_reg: dataframe
    :return: df
    :rtype: dataframe
    """
    start = time.time()
    df = df_reg.copy()
    df.drop(['granularite', 'maille_code'], axis=1, inplace=True)
    df.loc[df['source_nom'] == "OpenCOVID19-fr", :]
    df.drop(['source_nom'], 1, inplace=True)
    df = df.set_index('date')
    df = df.sort_index()
    df.index = pd.to_datetime(df.index)
    df.fillna(0, inplace=True)
    df['reanimation'] = df['reanimation'].astype(int)
    end = time.time()
    print("Time spent on clean_df_reg: {0:.5f} s.".format(end - start))
    return df


def regroup_by_reg(df_reg):
    """
    regroup_by_reg

    We regroup the data on ICU by region using dictionary type

    :param df_reg: data covid filtred by region
    :type df_reg: dataframe
    :return: dict_reg
    :rtype: dict
    """
    start = time.time()
    df_reg = clean_df_reg(df_reg)
    dict_reg = {}
    for region in df_reg['maille_nom'].unique().tolist():
        dict_reg[region] = pd.DataFrame(
            df_reg.loc[df_reg['maille_nom'] == region,
                       'reanimation']).resample("1D").sum()
        dict_reg[region] = dict_reg[region].rename(
            columns={"reanimation": region})
    end = time.time()
    print("Time spent on regroup_by_reg: {0:.5f} s.".format(end - start))
    return dict_reg


def create_df_all_reg(df_reg):
    """
    create_df_all_reg

    We create a dataframe with ICU data including all regions

    :param df_reg: data covid filtred by region
    :type df_reg: dataframe
    :return: df_all_reg
    :rtype: dataframe
    """
    start = time.time()
    dict_reg = regroup_by_reg(df_reg)
    df_all_reg = pd.DataFrame()
    for region in df_reg['maille_nom'].unique().tolist():
        df_all_reg = pd.concat([df_all_reg, dict_reg[region]], axis=1)

    df_all_reg.fillna(0, inplace=True)
    df_all_reg = df_all_reg.astype(int)
    df_all_reg = df_all_reg.reset_index()
    end = time.time()
    print("Time spent on create_df_all_reg: {0:.5f} s.".format(end - start))
    return df_all_reg


def icu_reg_all(df_reg):
    """
    icu_reg_all

    regroup all the lineplot of intensive care beds occupied
    for different periods in Covid crisis in french departments

    :param df_reg: data covid filtred by region
    :type df_reg: dataframe
    """
    start = time.time()

    df_all_reg = create_df_all_reg(df_reg)
    dict_plot_reg = {}

    dict_plot_reg['since 1st confinement'] = px.line(
            df_all_reg,
            x='date', y=df_all_reg.columns,
            range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
            title='Intensive care beds occupied since 1st confinement in french regions',
            height=500, width=800)
    dict_plot_reg['since 1st confinement'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_reg['during 1st confinement'] = px.line(
            df_all_reg,
            x='date', y=df_all_reg.columns,
            range_x=['2020-03-17', '2020-05-10'],
            title='Intensive care beds occupied during the 1st confinement in french regions',
            height=500, width=800)
    dict_plot_reg['during 1st confinement'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_reg['during deconfinement'] = px.line(
        df_all_reg,
        x='date', y=df_all_reg.columns,
        range_x=['2020-05-11', '2020-10-29'],
        title='Intensive care beds occupied during deconfinement in french regions',
        height=500, width=800)
    dict_plot_reg['during deconfinement'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_reg['during 2nd confinement'] = px.line(
        df_all_reg,
        x='date', y=df_all_reg.columns,
        range_x=['2020-10-30', '2020-12-14'],
        title='Intensive care beds occupied during the 2nd confinement in french regions',
        height=500, width=800)
    dict_plot_reg['during 2nd confinement'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_reg['during curfew'] = px.line(
        df_all_reg,
        x='date', y=df_all_reg.columns,
        range_x=['2020-12-15', '2021-04-02'],
        title='Intensive care beds occupied during curfew in french regions',
        height=500, width=800)
    dict_plot_reg['during curfew'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_reg['during 3rd confinement'] = px.line(
        df_all_reg,
        x='date', y=df_all_reg.columns,
        range_x=['2021-04-03', datetime.datetime.today().strftime('%Y-%m-%d')],
        title='Intensive care beds occupied during the 3rd confinement in french regions',
        height=500, width=800)
    
    end = time.time()
    print("Time spent on icu_reg_all: {0:.5f} s.".format(end - start))

    return(dict_plot_reg)


def icu_reg_display(period, df_reg):
    """
    icu_dep_display

    Return the lineplot of intensive care beds occupied
    in french departments for period selected.

    :param period: period in ['since 1st confinement', 'during 1st confinement', 'during deconfinement', 'during 2nd confinement', 'during curfew', 'during 3rd confinement']
    :type period: str
    :param df_dep: data on ICU in french departments
    :type df_dep: dataframe
    """
    start = time.time()
    dict_plot_reg = icu_reg_all(df_reg)
    end = time.time()
    print("Time spent on icu_reg_display: {0:.5f} s.".format(end - start))
    return(dict_plot_reg[period].show())


def icu_by_reg_all(region, df_dep):
    """
    icu_by_reg_all

    regroup by region all the lineplot of intensive care beds occupied
    for different periods in Covid crisis in french departments

    :param df_reg: data covid filtred by region
    :type df_reg: dataframe
    """
    start = time.time()

    icu_by_reg = cvz.link_dep_reg(df_dep)
    dict_plot_by_reg = {}

    dict_plot_by_reg['since 1st confinement'] = px.line(
        icu_by_reg[region],
        x='date', y=icu_by_reg[region].columns,
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title=f'Intensive care beds occupied since 1st confinement in {region}',
        height=500, width=800)
    dict_plot_by_reg['since 1st confinement'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_by_reg['during 1st confinement'] = px.line(
        icu_by_reg[region],
        x='date', y=icu_by_reg[region].columns,
        range_x=['2020-03-17', '2020-05-10'],
        title=f'Intensive care beds occupied during the 1st confinement in {region}',
        height=500, width=800)
    dict_plot_by_reg['during 1st confinement'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_by_reg['during deconfinement'] = px.line(
        icu_by_reg[region],
        x='date', y=icu_by_reg[region].columns,
        range_x=['2020-05-11', '2020-10-29'],
        title=f'Intensive care beds occupied during deconfinement in {region}',
        height=500, width=800)
    dict_plot_by_reg['during deconfinement'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_by_reg['during 2nd confinement'] = px.line(
        icu_by_reg[region],
        x='date', y=icu_by_reg[region].columns,
        range_x=['2020-10-30', '2021-12-14'],
        title=f'Intensive care beds occupied during the 2nd confinement in {region}',
        height=500, width=800)
    dict_plot_by_reg['during 2nd confinement'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_by_reg['during curfew'] = px.line(
        icu_by_reg[region],
        x='date', y=icu_by_reg[region].columns,
        range_x=['2020-12-15', '2021-04-02'],
        title=f'Intensive care beds occupied during curfew in {region}',
        height=500, width=800)
    dict_plot_by_reg['during curfew'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_by_reg['during 3rd confinement'] = px.line(
        icu_by_reg[region],
        x='date', y=icu_by_reg[region].columns,
        range_x=['2021-04-03', datetime.datetime.today().strftime('%Y-%m-%d')],
        title=f'Intensive care beds occupied during the 3rd confinement in {region}',
        height=500, width=800)
    
    end = time.time()
    print("Time spent on icu_by_reg_all: {0:.5f} s.".format(end - start))

    return(dict_plot_by_reg)


def icu_by_reg_display(period, region, df_dep):
    """
    icu_dep_display

    Return the lineplot of intensive care beds occupied
    in french departments for period selected.

    :param period: period in ['since 1st confinement', 'during 1st confinement', 'during deconfinement', 'during 2nd confinement', 'during curfew', 'during 3rd confinement']
    :type period: str
    :param df_dep: data on ICU in french departments
    :type df_dep: dataframe
    """
    start = time.time()
    dict_plot_by_reg = icu_by_reg_all(region, df_dep)
    end = time.time()
    print("Time spent on cicu_by_reg_display: {0:.5f} s.".format(end - start))
    return(dict_plot_by_reg[period].show())


def icu_all_reg_display(df_reg):
    """
    icu_all_reg_display

    Return the lineplot of ICU flux data by region since 1st confinement

    :param df_reg: data covid filtred by region
    :type df_reg: dataframe
    """
    start = time.time()
    df_all_reg = create_df_all_reg(df_reg)
    df_all_reg['Total'] = np.sum(df_all_reg.iloc[:, 1:], axis=1)
    fig = px.bar(
        df_all_reg,
        x='date', y='Total',
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title=f'ICU flux in France during Covid19 crisis',
        color='Total',
        labels={'Total': 'Number of patients'},
        height=500, width=800)
    end = time.time()
    print("Time spent on icu_all_reg_display: {0:.5f} s.".format(end - start))
    return(fig.show())


def change_format_reg(df_reg):
    """
    change_format_reg

    df_reg cleaned in ICU data and we changed the DOM columns (regrouped in 'Région d'Outre Mer'),
    and renamed some name region to be adaptable for later.

    :param df_reg: covid data filtred by region
    :type df_reg: dataframe
    :return: df_all_reg
    :rtype: dataframe
    """
    start = time.time()

    df_all_reg = create_df_all_reg(df_reg)
    df_all_reg["Régions d'Outre Mer"] = df_all_reg["Guadeloupe"] + df_all_reg['Martinique'] + df_all_reg['Guyane'] + df_all_reg['La Réunion'] + df_all_reg['Mayotte']
    df_all_reg.drop(['Guadeloupe', 'Martinique', 'Guyane', 'La Réunion', 'Mayotte'], axis=1, inplace=True)

    df_all_reg.rename(columns={
                            "Provence-Alpes-Côte d'Azur": "Provence-Alpes-Côte-d'Azur",
                            "Centre-Val de Loire": 'Centre-Val-de-Loire',
                            "Grand Est": "Grand-Est"}, inplace=True)
    end = time.time()
    print("Time spent on change_format_reg: {0:.5f} s.".format(end - start))
    return df_all_reg


def create_reg_total(df_reg):
    """
    create_reg_total

    sum of rows, total number of patients in ICU since 1st confinement, by reg

    :param df_reg: covid data filtred by region
    :type df_reg: dataframe
    :return: icu_reg_total
    :rtype: dataframe
    """
    start = time.time()
    df_all_reg = change_format_reg(df_reg)
    icu_reg_total = pd.DataFrame(np.sum(df_all_reg.iloc[:, 1:15], axis=0))
    icu_reg_total.columns = ['Total number']
    end = time.time()
    print("Time spent on create_reg_total: {0:.5f} s.".format(end - start))
    return icu_reg_total


def icu_reg_repartition(df_reg):
    """
    icu_reg_repartition

    A pie chart whos shows the repartition of patients in ICU by regions

    :param df_reg: covid data filtred by region
    :type df_reg: dataframe
    """
    start = time.time()
    icu_reg_total = create_reg_total(df_reg)
    fig = px.pie(
        icu_reg_total,
        values='Total number',
        names=icu_reg_total.index,
        title='Regional repartition of ICU during Covid19 crisis',
        color_discrete_sequence=px.colors.sequential.RdBu,
        height=500, width=800)
    end = time.time()
    print("Time spent on icu_reg_repartition: {0:.5f} s.".format(end - start))
    return(fig.show())


def create_icu_beds_reg(df_reg):
    """
    create_icu_beds_reg 

    Imports the data concerning the beds available in the intensive care unit by region.
    The data is cleaned.
    Then, we copy the data frame with all the data from the intensive care unit by region (column),
    to divide each column by the number of beds available with the corresponding region.
    This is then multiplied by 100 to return the percentage of occupied beds in intensive care unit.

    :param df_reg: covid data filtred by region
    :type df_reg: dataframe
    """
    start = time.time()
    icu_beds_reg = pd.read_csv('../covidviz/data/bed_rea_reg.csv', delimiter=';')

    icu_beds_reg = icu_beds_reg.rename(columns={'Unnamed: 0': 'Région'})
    icu_beds_reg = icu_beds_reg.drop(['CHR', 'Autres'], 1)

    icu_beds_reg = icu_beds_reg.loc[:13]
    icu_beds_reg = icu_beds_reg.rename(columns={'Confondu': 'Nombre de lits'})
    icu_beds_reg = icu_beds_reg.reindex(index=[7, 8, 9, 4, 6, 5, 3, 1, 2, 0, 10, 11, 12, 13])
    icu_beds_reg = icu_beds_reg.reset_index()
    icu_beds_reg = icu_beds_reg.drop(['index'], 1)
    icu_beds_reg = icu_beds_reg.rename(index={"Provence-Alpes-Côte-d'Azur": "Provence-Alpes-Côte d'Azur"})

    icu_beds_reg = icu_beds_reg.set_index('Région')

    df_all_reg = change_format_reg(df_reg)
    icu_beds_reg_prop = df_all_reg.copy()
    for col in icu_beds_reg.index.tolist():
        for row in range(len(icu_beds_reg_prop)):
            icu_beds_reg_prop.loc[row, col] = (icu_beds_reg_prop.loc[row, col]/int(icu_beds_reg.loc[col, 'Nombre de lits']))*100
    
    end = time.time()
    print("Time spent on create_icu_beds_reg: {0:.5f} s.".format(end - start))

    return(icu_beds_reg_prop)


def heat_map_icu_reg(df_reg):
    """
    heat_map_icu_reg

    return a heatmap of the percentage of occupied beds in ICU.

    :param df_reg: covid data filtred by region
    :type df_reg: dataframe
    """
    start = time.time()

    icu_beds_reg_prop = create_icu_beds_reg(df_reg) 
    fig = px.imshow(
        icu_beds_reg_prop.iloc[:, 1:],
        y=icu_beds_reg_prop['date'],
        title='Regional saturation in % in ICU during Covid19 crisis',
        height=700, width=800)

    end = time.time()
    print("Time spent on heat_map_icu_reg: {0:.5f} s.".format(end - start))

    return(fig.show())
