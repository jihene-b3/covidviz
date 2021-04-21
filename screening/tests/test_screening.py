import pandas as pd
import plotly.express as px
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

import screening as sc
import screening.graphs as scg
import screening.maps_departments as scmd


def daily_test(age, department):
    df = scg.screening_daily_age_dep[age][scg.screening_daily_age_dep[age]['dep'] == f'{department}']
    df.drop(['dep'], axis=1, inplace=True)
    df = df.reset_index()

    fig = px.bar(
        df,
        x='date', y='Tests number',
        color='% positive tests',
        title=f"Screening in department {department} for class age {age}",
        height=600, width=1000)
    fig.update_xaxes(rangeslider_visible=True)
    assert (fig.show())


def daily_test_dep(department):
    fig = px.bar(
        scg.screening_daily_dep[department],
        x='date', y='Tests number',
        color='% positive tests',
        title=f"Covid Screening in department {department}",
        height=600, width=1000)
    fig.update_xaxes(rangeslider_visible=True)
    assert (fig.show())


def daily_test_age(age_class):
    fig = px.bar(
        scg.screening_daily_age[age_class],
        x='date', y='Tests number',
        color='% positive tests',
        title=f"Covid Screening in France for the age class {age_class}",
        height=600, width=1000)
    fig.update_xaxes(rangeslider_visible=True)
    assert (fig.show())


def map_dep(department):
    assert (folium.Map(
        location=[
            scmd.dep_fr[scmd.dep_fr['maille_code'] == f'{department}']['Latitude'],
            scmd.dep_fr[scmd.dep_fr['maille_code'] == f'{department}']['Longitude']
            ], zoom_start=8))


def map_screening(dep_code):
    assert (scmd.all_map_dep[f'{dep_code}'])