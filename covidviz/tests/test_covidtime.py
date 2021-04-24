import pandas as pd
import datetime
import os.path, sys
import pandas as pd

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)
import covidviz as cvz

df_covid = pd.read_csv("covidviz/data/df_covid.csv")
df_dep = cvz.choose_granularity(df_covid,"departement")
df_covid_clean = cvz.choose_columns(df_covid, ['date', 'granularite', 'maille_code', 'maille_nom', 'reanimation','deces', 'cas_confirmes','gueris','source_nom'])
df_covid_clean = cvz.enable_time_series_plot(df_covid_clean, timein_field="date", timeseries_field_out="t")


def test_data_treatment():
    test = cvz.data_treatment_by_option(df_dep, "deces")
    assert (test.loc["2020-02-26", "Ain"] >= 0)
    

def test_adapt_time():
    test = cvz.adapt_time(df_covid)
    assert (type(test.date[1]) == pd._libs.tslibs.timestamps.Timestamp)
    

def test_enable_time_series():
    test = cvz.enable_time_series_plot(df_covid_clean, timein_field="date", timeseries_field_out="t")
    assert ('t' in list(test.columns))



