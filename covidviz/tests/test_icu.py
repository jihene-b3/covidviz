import pandas as pd
import numpy as np
import datetime

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)

import covidmap as cm
from covidviz.preprocess.clean_df import choose_columns, choose_granularity
from coviviz.io.load_db import Load_db
import plotly.express as px
import icu

df = choose_columns(
    Load_db.save_as_df(),
    [
        'date',
        'granularite',
        'maille_code',
        'maille_nom',
        'reanimation',
        'source_nom'
    ]
)

icu.df_dep = choose_granularity(icu.df_dep, 'departement')


def test_icu_dep_all():
    fig1 = px.line(
        icu.df_all_dep,
        x='date', y=icu.df_all_dep.columns,
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title='Intensive care beds occupied since 1st confinement in french departments',
        height=500, width=800)
    fig1.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig1.show())


def test_icu_dep_conf1():
    fig2 = px.line(
        icu.df_all_dep,
        x='date', y=icu.df_all_dep.columns,
        range_x=['2020-03-17', '2020-05-10'],
        title='Intensive care beds occupied during the 1st confinement in french departments',
        height=500, width=800)
    fig2.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig2.show())


def test_icu_dep_dec():
    fig3 = px.line(
        icu.df_all_dep,
        x='date', y=icu.df_all_dep.columns,
        range_x=['2020-05-11', '2020-10-29'],
        title='Intensive care beds occupied during deconfinement in french departments', 
        height=500, width=800)
    fig3.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig3.show())


def test_icu_dep_conf2():
    fig4 = px.line(
        icu.df_all_dep,
        x='date', y=icu.df_all_dep.columns,
        range_x=['2020-10-30', '2021-12-14'],
        title='Intensive care beds occupied during the 2nd confinement in french departments',
        height=500, width=800)
    fig4.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig4.show())


def test_icu_dep_curfew():
    fig5 = px.line(
        icu.df_all_dep,
        x='date', y=icu.df_all_dep.columns,
        range_x=['2020-12-15', '2021-04-02'],
        title='Intensive care beds occupied during curfew in french departments',
        height=500, width=800)
    fig5.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig5.show())


def test_icu_dep_conf3():
    fig6 = px.line(
        icu.df_all_dep,
        x='date', y=icu.df_all_dep.columns,
        range_x=['2021-04-03', datetime.datetime.today().strftime('%Y-%m-%d')],
        title='Intensive care beds occupied during the 3rd confinement in french departments',
        height=500, width=800)
    assert (fig6.show())


icu.df_reg = choose_granularity(icu.df_reg, 'region')

def test_icu_reg_all():
    fig1 = px.line(
        icu.df_all_reg,
        x='date', y=icu.df_all_reg.columns,
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title='Intensive care beds occupied since 1st confinement in french regions',
        height=500, width=800)
    fig1.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig1.show())


def test_icu_reg_conf1():
    fig2 = px.line(
        icu.df_all_reg,
        x='date', y=icu.df_all_reg.columns,
        range_x=['2020-03-17', '2020-05-10'],
        title='Intensive care beds occupied during the 1st confinement in french regions',
        height=500, width=800)
    fig2.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig2.show)


def test_icu_reg_dec():
    fig3 = px.line(
        icu.df_all_reg,
        x='date', y=icu.df_all_reg.columns,
        range_x=['2020-05-11', '2020-10-29'],
        title='Intensive care beds occupied during deconfinement in french regions',
        height=500, width=800)
    fig3.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig3.show())


def test_icu_reg_conf2():
    fig4 = px.line(
        icu.df_all_reg,
        x='date', y=icu.df_all_reg.columns,
        range_x=['2020-10-30', '2021-12-14'],
        title='Intensive care beds occupied during the 2nd confinement in french regions',
        height=500, width=800)
    fig4.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig4.show())


def test_icu_reg_curfew():
    fig5 = px.line(
        icu.df_all_reg,
        x='date', y=icu.df_all_reg.columns,
        range_x=['2020-12-15', '2021-04-02'],
        title='Intensive care beds occupied during curfew in french regions',
        height=500, width=800)
    fig5.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig5.show())


def test_icu_reg_conf3():
    fig6 = px.line(
        icu.df_all_reg,
        x='date', y=icu.df_all_reg.columns,
        range_x=['2021-04-03', datetime.datetime.today().strftime('%Y-%m-%d')],
        title='Intensive care beds occupied during the 3rd confinement in french regions',
        height=500, width=800)
    assert (fig6.show())


def test_icu_by_reg_all(region):
    fig1 = px.line(
        icu.icu_by_reg[f'{region}'],
        x='date', y=icu.icu_by_reg[f'{region}'].columns,
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title=f'Intensive care beds occupied since 1st confinement in {region}',
        height=500, width=800)
    fig1.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig1.show())


def test_icu_by_reg_conf1(region):
    fig2 = px.line(
        icu.icu_by_reg[f'{region}'],
        x='date', y=icu.icu_by_reg[f'{region}'].columns,
        range_x=['2020-03-17', '2020-05-10'],
        title=f'Intensive care beds occupied during the 1st confinement in {region}',
        height=500, width=800)
    fig2.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig2.show)


def test_icu_by_reg_dec(region):
    fig3 = px.line(
        icu.icu_by_reg[f'{region}'],
        x='date', y=icu.icu_by_reg[f'{region}'].columns,
        range_x=['2020-05-11', '2020-10-29'],
        title=f'Intensive care beds occupied during deconfinement in {region}',
        height=500, width=800)
    fig3.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig3.show())


def test_icu_by_reg_conf2(region):
    fig4 = px.line(
        icu.icu_by_reg[f'{region}'],
        x='date', y=icu.icu_by_reg[f'{region}'].columns,
        range_x=['2020-10-30', '2021-12-14'],
        title=f'Intensive care beds occupied during the 2nd confinement in {region}',
        height=500, width=800)
    fig4.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig4.show())


def test_icu_by_reg_curfew(region):
    fig5 = px.line(
        icu.icu_by_reg[f'{region}'],
        x='date', y=icu.icu_by_reg[f'{region}'].columns,
        range_x=['2020-12-15', '2021-04-02'],
        title=f'Intensive care beds occupied during curfew in {region}',
        height=500, width=800)
    fig5.update_xaxes(dtick='M1', tickformat="%d\n%b")
    assert (fig5.show())


def test_icu_by_reg_conf3(region):
    fig6 = px.line(
        icu.icu_by_reg[f'{region}'],
        x='date', y=icu.icu_by_reg[f'{region}'].columns,
        range_x=['2021-04-03', datetime.datetime.today().strftime('%Y-%m-%d')],
        title=f'Intensive care beds occupied during the 3rd confinement in {region}',
        height=500, width=800)
    assert (fig6.show())


def test_icu_all_reg():
    fig = px.bar(
        icu.df_all_reg,
        x='date', y='Total',
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title=f'ICU flux in France during Covid19 crisis',
        color='Total',
        labels={'Total': 'Number of patients'},
        height=500, width=800)
    assert (fig.show())


def test_icu_reg_repartition():
    fig = px.pie(
        icu.icu_reg_total,
        values='Total number',
        names=icu.icu_reg_total.index,
        title='Regional repartition of ICU during Covid19 crisis',
        color_discrete_sequence=px.colors.sequential.RdBu,
        height=500, width=800)
    assert (fig.show())

def test_heat_map_icu_reg():
    fig = px.imshow(
        icu.icu_beds_reg_prop.iloc[:, 1:],
        y=icu.icu_beds_reg_prop['date'],
        title='Regional saturation in % in ICU during Covid19 crisis',
        height=700, width=800)
    assert (fig.show())

