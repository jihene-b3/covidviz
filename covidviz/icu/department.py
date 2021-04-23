import pandas as pd
import numpy as np
import datetime
import plotly.express as px


"""
 ICU IN FRENCH DEPARTMENTS

 We generate a first DataFrame of ICU in french departments,
 with keeping one source : 'Santé publique France Data'
"""


def format_df_dep(df_with_just_dep):
    df_dep = df_with_just_dep.copy()
    df_dep.drop('granularite', axis=1, inplace=True)
    df_dep.loc[df_dep['source_nom'] == "Santé publique France Data", :]
    df_dep.drop(['source_nom'], 1, inplace=True)
    df_dep = df_dep.set_index('date')
    df_dep = df_dep.sort_index()
    df_dep.index = pd.to_datetime(df_dep.index)
    df_dep.fillna(0, inplace=True)
    df_dep['reanimation'] = df_dep['reanimation'].astype(int)
    return df_dep

# %%


def regroup_by_dep(df_dep):
    """
    Regroup the data by department using dictionary type
    """
    dict_dep = {}
    for department in df_dep['maille_nom'].unique().tolist():
        dict_dep[department] = pd.DataFrame(
            df_dep.loc[df_dep['maille_nom'] == department,
                    'reanimation']).resample("1D").sum()
        dict_dep[department] = dict_dep[department].rename(
            columns={"reanimation": department})
    return dict_dep


# %%

def create_df_all_dep(df_dep, dict_dep):
    """
    We create a DataFrame including all departments
    """
    df_all_dep = pd.DataFrame()
    for department in df_dep['maille_nom'].unique().tolist():
        df_all_dep = pd.concat([df_all_dep, dict_dep[department]], axis=1)

    df_all_dep.fillna(0, inplace=True)
    df_all_dep = df_all_dep.astype(int)
    df_all_dep = df_all_dep.reset_index()
    return df_all_dep

# %%


def icu_dep_all(df_all_dep):
    """
    return the lineplot of intensive care beds occupied
    since 1st confinement in french departments
    """
    fig1 = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title='Intensive care beds occupied since 1st confinement in french departments',
        height=500, width=800)
    fig1.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig1.show())


def icu_dep_conf1(df_all_dep):
    """
    return the lineplot of intensive care beds occupied
    during the 1st confinement in french departments
    """
    fig2 = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-03-17', '2020-05-10'],
        title='Intensive care beds occupied during the 1st confinement in french departments',
        height=500, width=800)
    fig2.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig2.show())


def icu_dep_dec(df_all_dep):
    """
    return the lineplot of intensive care beds occupied
    during deconfinement in french departments
    """
    fig3 = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-05-11', '2020-10-29'],
        title='Intensive care beds occupied during deconfinement in french departments', 
        height=500, width=800)
    fig3.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig3.show())


def icu_dep_conf2(df_all_dep):
    """
    return the lineplot of intensive care beds occupied
    during the 2nd confinement in french departments
    """
    fig4 = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-10-30', '2021-12-14'],
        title='Intensive care beds occupied during the 2nd confinement in french departments',
        height=500, width=800)
    fig4.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig4.show())


def icu_dep_curfew(df_all_dep):
    """
    return the lineplot of intensive care beds occupied
    during curfew in french departments
    """
    fig5 = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-12-15', '2021-04-02'],
        title='Intensive care beds occupied during curfew in french departments',
        height=500, width=800)
    fig5.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig5.show())


def icu_dep_conf3(df_all_dep):
    """
    return the lineplot of intensive care beds occupied
    during the 3rd confinement in french departments
    """
    fig6 = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2021-04-03', datetime.datetime.today().strftime('%Y-%m-%d')],
        title='Intensive care beds occupied during the 3rd confinement in french departments',
        height=500, width=800)
    return(fig6.show())
