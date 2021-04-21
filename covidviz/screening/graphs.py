import pandas as pd
import plotly.express as px
import numpy as np

AGE = pd.DataFrame(screening_daily['cl_age'].unique())
AGE.set_axis(['classe'], axis=1, inplace=True)
DEP = pd.DataFrame(screening_daily['dep'].unique())
DEP.set_axis(['code'], axis=1, inplace=True)

def screen_age_dep(screening_daily):
    screening_daily_age_dep = {}
    for age in AGE['classe'].tolist():
        screening_daily_age_dep[age] = screening_daily[screening_daily['cl_age'] == age]

        screening_daily_age_dep[age].drop(['cl_age'], axis=1, inplace=True)
        screening_daily_age_dep[age] = screening_daily_age_dep[age].reset_index()
        screening_daily_age_dep[age].drop(['pop', 'index'], axis=1, inplace=True)

        screening_daily_age_dep[age]['Tests cumul'] = screening_daily_age_dep[age]['Tests number'].cumsum()

        screening_daily_age_dep[age]['% positive tests'] = (screening_daily_age_dep[age]['Positive tests']/screening_daily_age_dep[age]['Tests number'])*100

        screening_daily_age_dep[age].fillna(0, inplace=True)
    return screening_daily_age_dep 

def screen_age(screening_daily):
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
    return screening_daily_age

def screen_dep(screening_daily):
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
    return screening_daily_dep


def daily_test(age, department, screening_daily_age_dep):
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


def daily_test_dep(department, screening_daily_dep):
    fig = px.bar(
        screening_daily_dep[department],
        x='date', y='Tests number',
        color='% positive tests',
        title=f"Covid Screening in department {department}",
        height=600, width=1000)
    fig.update_xaxes(rangeslider_visible=True)
    return(fig.show())


def daily_test_age(age_class, screening_daily_age):
    fig = px.bar(
        screening_daily_age[age_class],
        x='date', y='Tests number',
        color='% positive tests',
        title=f"Covid Screening in France for the age class {age_class}",
        height=600, width=1000)
    fig.update_xaxes(rangeslider_visible=True)
    return(fig.show())
