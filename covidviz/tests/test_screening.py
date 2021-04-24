import pandas as pd
import plotly.express as px
import numpy as np

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)

import covidviz as cvz

screening_daily = pd.read_csv(
    '../covidviz/data/sp-pos-quot-dep-2021-04-16-19h05.csv',
    delimiter=';',
    low_memory=False
)

grand_public_path = '../data/scr_public_centers.csv'
depis_grand_public = pd.read_csv(grand_public_path)

acces_restreint_path = '../data/scr_private_centers.csv'
depis_acces_restreint = pd.read_csv(acces_restreint_path)

dep_fr = pd.read_csv('../data/depart_fr_coord.csv', delimiter=';')


def test_screening_by_age_dep():
    df = cvz.screening_by_age_dep(screening_daily)
    assert (df[90].loc[0, '% positive tests'] <= 100)


def test_screening_by_dep():
    df = cvz.screening_by_dep(screening_daily)
    assert (df[90].loc[0, '% positive tests'] <= 100)


def test_screening_by_age():
    df = cvz.screening_by_age(screening_daily)
    assert (df[90].loc[0, '% positive tests'] <= 100)


def test_clean_public_centers():
    df = cvz.clean_public_centers(depis_grand_public)
    assert (df.loc[3093, 'tel_rdv'] == '01 85 90 79 13')


def test_regroup_public_center_by_dep():
    df = cvz.regroup_public_center_by_dep(depis_grand_public, dep_fr)
    assert (type(df['34']) == pd.core.frame.DataFrame)


def test_clean_private_centers():
    df = cvz.clean_private_centers(depis_acces_restreint)
    assert (type(df) == pd.core.frame.DataFrame)


def test_regroup_private_center_by_dep():
    df = cvz.regroup_private_center_by_dep(depis_acces_restreint, dep_fr)
    assert (type(df['34']) == pd.core.frame.DataFrame)
 