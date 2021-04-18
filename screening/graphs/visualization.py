import pandas as pd
import plotly.express as px
import numpy as np

screening_daily = pd.read_csv(
    'screening/data/sp-pos-quot-dep-2021-04-16-19h05.csv',
    delimiter=';',
    low_memory=False)

screening_daily.rename(
    columns={'cl_age90': 'cl_age',
             'jour': 'date',
             'T': 'Tests number',
             'P': 'Positive tests'},
    inplace=True)

DEP = pd.DataFrame(screening_daily['dep'].unique())
DEP.set_axis(['code'], axis=1, inplace=True)

AGE = pd.DataFrame(screening_daily['cl_age'].unique())
AGE.set_axis(['classe'], axis=1, inplace=True)


screening_daily_age_dep = {}
for age in AGE['classe'].tolist():
    screening_daily_age_dep[age] =
    screening_daily[screening_daily['cl_age'] == age]

    screening_daily_age_dep[age].drop(['cl_age'], axis=1, inplace=True)
    screening_daily_age_dep[age] = screening_daily_age_dep[age].reset_index()
    screening_daily_age_dep[age].drop(['pop', 'index'], axis=1, inplace=True)

    screening_daily_age_dep[age]['Tests cumul'] =
    screening_daily_age_dep[age]['Tests number'].cumsum()

    screening_daily_age_dep[age]['% positive tests'] =
    (screening_daily_age_dep[age]['Positive tests']/screening_daily_age_dep[age]['Tests number'])*100

    screening_daily_age_dep[age].fillna(0, inplace=True)

screening_daily_age = {}
for age in AGE['classe'].tolist():
    screening_daily_age[age] =
    screening_daily[screening_daily['cl_age'] == age]

    screening_daily_age[age].drop(['cl_age'], axis=1, inplace=True)
    screening_daily_age[age] = screening_daily_age[age].reset_index()
    screening_daily_age[age] = screening_daily_age[age].set_index('date')

    screening_daily_age[age].index =
    pd.to_datetime(screening_daily_age[age].index, format="%Y-%m-%d")

    screening_daily_age[age] = screening_daily_age[age].resample("1D").sum()
    screening_daily_age[age].drop(['pop', 'index'], axis=1, inplace=True)

    screening_daily_age[age]['Tests cumul'] =
    screening_daily_age[age]['Tests number'].cumsum()

    screening_daily_age[age]['% positive tests'] =
    (screening_daily_age[age]['Positive tests']/screening_daily_age[age]['Tests number'])*100

    screening_daily_age[age] = screening_daily_age[age].reset_index()


screening_daily_dep = {}
for dep_code in DEP['code'].tolist():
    screening_daily_dep[dep_code] =
    screening_daily[screening_daily['dep'] == dep_code]

    screening_daily_dep[dep_code].drop(['dep'], axis=1, inplace=True)
    screening_daily_dep[dep_code] = screening_daily_dep[dep_code].reset_index()

    screening_daily_dep[dep_code] =
    screening_daily_dep[dep_code].set_index('date')

    screening_daily_dep[dep_code].index =
    pd.to_datetime(screening_daily_dep[dep_code].index, format="%Y-%m-%d")

    screening_daily_dep[dep_code] =
    screening_daily_dep[dep_code].resample("1D").sum()

    screening_daily_dep[dep_code].drop(['cl_age', 'pop', 'index'],
                                       axis=1, inplace=True)

    screening_daily_dep[dep_code]['Tests cumul'] =
    screening_daily_dep[dep_code]['Tests number'].cumsum()

    screening_daily_dep[dep_code]['% positive tests'] =
    (screening_daily_dep[dep_code]['Positive tests']/screening_daily_dep[dep_code]['Tests number'])*100

    screening_daily_dep[dep_code] = screening_daily_dep[dep_code].reset_index()


def daily_test(age, department):
    df = screening_daily_age_dep[age][screening_daily_age_dep[age]['dep'] == f'{department}']
    df.drop(['dep'], axis=1, inplace=True)
    df = df.reset_index()

    fig = px.bar(
        df,
        x='date', y='Tests number',
        color='% positive tests',
        title=f"Screening in department {department} for class age {age}",
        height=600, width=1000)
    fig.update_xaxes(rangeslider_visible=True)
    return(fig.show())


def daily_test_dep(department):
    fig = px.bar(
        screening_daily_dep[department],
        x='date', y='Tests number',
        color='% positive tests',
        title=f"Covid Screening in department {department}",
        height=600, width=1000)
    fig.update_xaxes(rangeslider_visible=True)
    return(fig.show())


def daily_test_age(age_class):
    fig = px.bar(
        screening_daily_age[age_class],
        x='date', y='Tests number',
        color='% positive tests',
        title=f"Covid Screening in France for the age class {age_class}",
        height=600, width=1000)
    fig.update_xaxes(rangeslider_visible=True)
    return(fig.show())
