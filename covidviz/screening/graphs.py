import pandas as pd
import plotly.express as px
import numpy as np


def screening_by_age_dep(screening_daily):
    """
    screening_by_age_dep

    We regroup data by age (we will filter by department after).
    We add the columns :
        - 'Tests cumul' :
            indicates the number of cumulative screenings
            since the first day (first line of data), per day.
        - '% positive tests' :
            indicates the percentage of positive screenings.

    :param screening_daily: data on the number of screenings carried out by age group and / or department
    :type screening_daily: dataframe
    :return: screening_daily_age_dep
    :rtype: dict
    """
    df = screening_daily.copy()
    df.rename(columns={
        'cl_age90': 'cl_age', 'jour': 'date', 'T': 'Tests number', 'P': 'Positive tests'
        },
        inplace=True)
    AGE = pd.DataFrame(df['cl_age'].unique())
    AGE.set_axis(['classe'], axis=1, inplace=True)
    screening_daily_age_dep = {}

    for age in AGE['classe'].tolist():
        screening_daily_age_dep[age] = df[df['cl_age'] == age]

        screening_daily_age_dep[age].drop(['cl_age'], axis=1, inplace=True)
        screening_daily_age_dep[age] = screening_daily_age_dep[age].reset_index()
        screening_daily_age_dep[age].drop(['pop', 'index'], axis=1, inplace=True)

        screening_daily_age_dep[age]['Tests cumul'] = screening_daily_age_dep[age]['Tests number'].cumsum()

        screening_daily_age_dep[age]['% positive tests'] = (screening_daily_age_dep[age]['Positive tests']/screening_daily_age_dep[age]['Tests number'])*100

        screening_daily_age_dep[age].fillna(0, inplace=True)
    return screening_daily_age_dep


def screening_by_age(screening_daily):
    """
    screening_by_age

    We regroup data by age.
    We add the columns :
        - 'Tests cumul' : 
            indicates the number of cumulative screenings
            since the first day (first line of data), per day.
        - '% positive tests' :
            indicates the percentage of positive screenings.

    :param screening_daily: data on the number of screenings carried out by age group and / or department
    :type screening_daily: dataframe
    :return: Daily screenings by age
    :rtype: dict
    """
    df = screening_daily.copy()
    df.rename(columns={
        'cl_age90': 'cl_age', 'jour': 'date', 'T': 'Tests number', 'P': 'Positive tests'
        },
        inplace=True)    
    # Grouping all age classes
    AGE = pd.DataFrame(df['cl_age'].unique())
    AGE.set_axis(['classe'], axis=1, inplace=True)
    screening_daily_age = {}
    for age in AGE['classe'].tolist():
        screening_daily_age[age] = df[df['cl_age'] == age]

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


def screening_by_dep(screening_daily):
    """
    screening_by_dep

    We regroup data by dep.
    We add the columns :
        - 'Tests cumul' : 
            indicates the number of cumulative screenings
            since the first day (first line of data), per day.
        - '% positive tests' :
            indicates the percentage of positive screenings.

    :param screening_daily: data on the number of screenings carried out by age group and / or department
    :type screening_daily: dataframe
    :return: Daily screenings by department
    :rtype: dict
    """
    df = screening_daily.copy()
    df.rename(columns={
        'cl_age90': 'cl_age', 'jour': 'date', 'T': 'Tests number', 'P': 'Positive tests'
        },
        inplace=True)    
    # Grouping all departments
    DEP = pd.DataFrame(df['dep'].unique())
    DEP.set_axis(['code'], axis=1, inplace=True)

    screening_daily_dep = {}
    for dep_code in DEP['code'].tolist():
        screening_daily_dep[dep_code] = df[df['dep'] == dep_code]

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


def daily_test(age, department, screening_daily):
    """
    daily_test

    displays the barplot of screenings performed per day by age group and department.
    The more intense the color of the bar (towards yellow),
    the higher the percentage of number of positive tests (the reference is placed to the right of the graph). 
    The 'plotly' package allows you to zoom the desired period.

    :param age: age class in [9, 19, 29, 39, 49, 59, 69, 79, 89, 90]
    :type age: int
    :param department: french department like '34' (for Hérault department)
    :type department: str
    :param screening_daily: data on the number of screenings carried out by age group and / or department
    :type screening_daily: dataframe
    :return: Daily screenings by age and department
    """
    screening_daily_age_dep = screening_by_age_dep(screening_daily)
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


def daily_test_dep(department, screening_daily):
    """
    daily_test_dep

    displays the barplot of screenings performed per day by department.
    The more intense the color of the bar (towards yellow),
    the higher the percentage of number of positive tests (the reference is placed to the right of the graph). 
    The 'plotly' package allows you to zoom the desired period.

    :param department: french department like '34' (for Hérault department)
    :type department: str
    :param screening_daily: data on the number of screenings carried out by age group and / or department
    :type screening_daily: dataframe
    :return: Daily screenings by department
    """
    screening_daily_dep = screening_by_dep(screening_daily)
    fig = px.bar(
        screening_daily_dep[department],
        x='date', y='Tests number',
        color='% positive tests',
        title=f"Covid Screening in department {department}",
        height=600, width=1000)
    fig.update_xaxes(rangeslider_visible=True)
    return(fig.show())


def daily_test_age(age_class, screening_daily):
    """
    daily_test_age

    displays the barplot of screenings performed per day by age.
    The more intense the color of the bar (towards yellow),
    the higher the percentage of number of positive tests (the reference is placed to the right of the graph). 
    The 'plotly' package allows you to zoom the desired period.

    :param age: age class in [9, 19, 29, 39, 49, 59, 69, 79, 89, 90]
    :type age: int
    :param screening_daily: data on the number of screenings carried out by age group and / or department
    :type screening_daily: dataframe
    :return: Daily screenings by age
    """
    screening_daily_age = screening_by_age(screening_daily)
    fig = px.bar(
        screening_daily_age[age_class],
        x='date', y='Tests number',
        color='% positive tests',
        title=f"Covid Screening in France for the age class {age_class}",
        height=600, width=1000)
    fig.update_xaxes(rangeslider_visible=True)
    return(fig.show())
