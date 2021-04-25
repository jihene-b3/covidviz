import pandas as pd
import numpy as np
import datetime, time
import plotly.express as px


def clean_df_dep(df_dep):
    """
    clean_df_dep : ICU IN FRENCH DEPARTMENTS

    We generate a first DataFrame of ICU in french departments,
    with keeping one source : 'Santé publique France Data',
    We also clean the data

    :param df_with_just_dep: data covid in french departments
    :type df_with_just_dep: dataframe
    :return: df
    :rtype: dataframe
    """
    start = time.time()
    df = df_dep.copy()
    df.drop('granularite', axis=1, inplace=True)
    df.loc[df['source_nom'] == "Santé publique France Data", :]
    df.drop(['source_nom'], 1, inplace=True)
    df = df.set_index('date')
    df = df.sort_index()
    df.index = pd.to_datetime(df.index)
    df.fillna(0, inplace=True)
    df['reanimation'] = df['reanimation'].astype(int)
    end = time.time()
    print("Time spent on clean_df_dep: {0:.5f} s.".format(end - start))
    return df


def regroup_by_dep(df_dep):
    """
    regroup_by_dep

    data regrouped by department in a dictionnary (one key is one department).

    :param df_dep: data on ICU in french departments
    :type df_dep: dataframe
    :return: dict_dep
    :rtype: dict
    """
    start = time.time()
    df_dep = clean_df_dep(df_dep)
    dict_dep = {}
    for department in df_dep['maille_nom'].unique().tolist():
        dict_dep[department] = pd.DataFrame(
            df_dep.loc[df_dep['maille_nom'] == department,
                       'reanimation']).resample("1D").sum()
        dict_dep[department] = dict_dep[department].rename(
            columns={"reanimation": department})
    end = time.time()
    print("Time spent on regroup_by_dep: {0:.5f} s.".format(end - start))
    return dict_dep


def create_df_all_dep(df_dep):
    """
    create_df_all_dep

    all data on ICU in all departments (by columns)

    :param df_dep: data on ICU in french departments
    :type df_dep: dataframe
    :param dict_dep: [description]
    :type dict_dep: dict
    :return: df_all_dep
    :rtype: dataframe
    """
    start = time.time()
    # df_dep = clean_df_dep(df_dep)
    dict_dep = regroup_by_dep(df_dep)
    df_all_dep = pd.DataFrame()
    for department in df_dep['maille_nom'].unique().tolist():
        df_all_dep = pd.concat([df_all_dep, dict_dep[department]], axis=1)

    df_all_dep.fillna(0, inplace=True)
    df_all_dep = df_all_dep.astype(int)
    df_all_dep = df_all_dep.reset_index()
    end = time.time()
    print("Time spent on create_df_all_dep: {0:.5f} s.".format(end - start))
    return df_all_dep


def icu_dep_all(df_dep):
    """
    icu_dep_all

    Regroup all the lineplot of intensive care beds occupied
    in french departments for different periods
    in a dictionnary

    :param df_dep: data on ICU in french departments
    :type df_dep: dataframe
    """
    start = time.time()

    df_all_dep = create_df_all_dep(df_dep)
    dict_plot_dep = {}

    dict_plot_dep['since 1st confinement'] = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title='Intensive care beds occupied since 1st confinement in french departments',
        height=500, width=800)
    dict_plot_dep['since 1st confinement'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_dep['during 1st confinement'] = px.line(
            df_all_dep,
            x='date', y=df_all_dep.columns,
            range_x=['2020-03-17', '2020-05-10'],
            title='Intensive care beds occupied during the 1st confinement in french departments',
            height=500, width=800)
    dict_plot_dep['during 1st confinement'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_dep['during deconfinement'] = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-05-11', '2020-10-29'],
        title='Intensive care beds occupied during deconfinement in french departments',
        height=500, width=800)
    dict_plot_dep['during deconfinement'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_dep['during 2nd confinement'] = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-10-30', '2020-12-14'],
        title='Intensive care beds occupied during the 2nd confinement in french departments',
        height=500, width=800)
    dict_plot_dep['during 2nd confinement'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_dep['during curfew'] = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-12-15', '2021-04-02'],
        title='Intensive care beds occupied during curfew in french departments',
        height=500, width=800)
    dict_plot_dep['during curfew'].update_xaxes(dtick='M1', tickformat="%d\n%b")

    dict_plot_dep['during 3rd confinement'] = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2021-04-03', datetime.datetime.today().strftime('%Y-%m-%d')],
        title='Intensive care beds occupied during the 3rd confinement in french departments',
        height=500, width=800)
    end = time.time()
    print("Time spent on icu_dep_all: {0:.5f} s.".format(end - start))
    return(dict_plot_dep)


def icu_dep_display(period, df_dep):
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
    dict_plot_dep = icu_dep_all(df_dep)
    end = time.time()
    print("Time spent on icu_dep_display: {0:.5f} s.".format(end - start))
    return(dict_plot_dep[period].show())
