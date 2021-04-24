#import packages :

import pandas as pd
import pandas_alive
import covidviz
from covidviz import *
from covidviz.preprocess.format_data import *
from covidviz.preprocess.clean_df import choose_columns, choose_granularity




# adapt_time(_data)
def adapt_time(_data):
    _data = _data[_data.date != '2020-11_11']
    _data['date'] = pd.to_datetime(_data['date'])
    return _data


# data treatment 
def data_treatment_by_option(_data_granu, option):
    df =_data_granu.groupby(['maille_nom', 'date'])[option].sum().reset_index()
    df = df.set_index(['maille_nom', 'date'])
    df = df.sort_values(['maille_nom', 'date'],ascending=True)
    df=df[df[option] > 0]
    df.reset_index(inplace=True)
    df_clean = df.pivot(index="date", columns="maille_nom", values=option).fillna(0)
    return(df_clean)

def plot_animation(df_clean, granu, option):
    if granu == "departement" and option == "deces":
        df_clean.plot_animated("image/covid-19-h-bar-deaths_departement.gif", period_fmt="%Y-%m-%d", title="Covid-19 : French departments'number of deaths",n_visible=15)
    elif granu == "departement" and option == "cas_confirmes":
        df_clean.plot_animated("../image/covid-19-h-bar-cases_departement.gif", period_fmt="%Y-%m-%d", title="Covid-19 : French departments'number of deaths",n_visible=15)
    elif granu == "region" and option == "deces":
        df_clean.plot_animated("examples/covid-19-deaths-regions.gif", 
                            title="Covid-19 : Evolution of French regions deaths counts", 
                            kind='line', 
                            period_fmt="%Y-%m-%d", 
                            period_label={ 
                                'x':0.25, 
                                'y':0.9, 
                                'family': 'sans-serif', 
                                'color': 'darkred' 
                            })
    elif granu == "region" and option == "cas_confirmes":
        df_clean.plot_animated("exampels/covid-19-cases-region.gif", 
                            title="Covid-19 : Evoulution of French regions deaths counts", 
                            kind='line', 
                            period_fmt="%Y-%m-%d", 
                            period_label={ 
                                'x':0.25, 
                                'y':0.9, 
                                'family': 'sans-serif', 
                                'color': 'darkred' 
                            })

