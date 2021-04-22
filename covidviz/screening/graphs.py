import pandas as pd
import plotly.express as px
import numpy as np


def daily_test(age, department, screening_daily_age_dep):
    """
    daily_test 

    displays the barplot of screenings performed per day by age group and department.
    The more intense the color of the bar (towards yellow),
    the higher the percentage of number of positive tests (the reference is placed to the right of the graph). 
    The 'plotly' package allows you to zoom the desired period.

    Args:
        age (int): age class in [9, 19, 29, 39, 49, 59, 69, 79, 89, 90]
        department (str): french department like '34' (for Hérault department)
        screening_daily_age_dep (dict): data by age filtred then by department
    """
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
    """
    daily_test_dep

    displays the barplot of screenings performed per day by department.
    The more intense the color of the bar (towards yellow),
    the higher the percentage of number of positive tests (the reference is placed to the right of the graph). 
    The 'plotly' package allows you to zoom the desired period.

    Args:
        department (str): french department like '34' (for Hérault department)
        screening_daily_dep (dict): data by dep
    """
    fig = px.bar(
        screening_daily_dep[department],
        x='date', y='Tests number',
        color='% positive tests',
        title=f"Covid Screening in department {department}",
        height=600, width=1000)
    fig.update_xaxes(rangeslider_visible=True)
    return(fig.show())


def daily_test_age(age_class, screening_daily_age):
    """
    daily_test_age

    displays the barplot of screenings performed per day by age group.
    The more intense the color of the bar (towards yellow),
    the higher the percentage of number of positive tests (the reference is placed to the right of the graph). 
    The 'plotly' package allows you to zoom the desired period.

    Args:
        age (int): age class in [9, 19, 29, 39, 49, 59, 69, 79, 89, 90]
        screening_daily_age (dict): data by age
    """
    fig = px.bar(
        screening_daily_age[age_class],
        x='date', y='Tests number',
        color='% positive tests',
        title=f"Covid Screening in France for the age class {age_class}",
        height=600, width=1000)
    fig.update_xaxes(rangeslider_visible=True)
    return(fig.show())
