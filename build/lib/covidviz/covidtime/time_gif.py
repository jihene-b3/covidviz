#import packages :

import pandas as pd
import pandas_alive
import covidviz
from covidviz import *
from covidviz.preprocess.format_data import *
from covidviz.preprocess.clean_df import choose_columns, choose_granularity
import time



def adapt_time(data):
    """
    Removes the date given with a wrong foramt 
    Chnages dates into timestamp format 
    """
    start = time.time()
    data = data[data.date != '2020-11_11']
    data['date'] = pd.to_datetime(data['date'])
    end = time.time()
    print("Time spent on adapt_time function: {0:.5f} s.".format(end - start)) 
    return data

# data treatment 
def data_treatment_by_option(data_granu, option):
    """
    Adjusts dataframe to set pandas_alive package requirements as arguments 
    Resamples data so we take into acount rows with option =! 0
    """
    start = time.time()
    df = data_granu.groupby(['maille_nom', 'date'])[option].sum().reset_index()
    df = df.set_index(['maille_nom', 'date'])
    df = df.sort_values(['maille_nom', 'date'],ascending=True)
    df=df[df[option] > 0]
    df.reset_index(inplace=True)
    df_clean = df.pivot(index="date", columns="maille_nom", values=option).fillna(0)
    end = time.time()
    print("Time spent on data_treatment_by_option: {0:.5f} s.".format(end - start)) 
    return(df_clean)

def plot_animation(df_clean, granu, option):
    """
    Plot an animation....
    """
    start = time.time()
    if granu == "departement" and option == "deces":
        df_clean.plot_animated("temp/covid-19-h-bar-deaths_departement.gif", period_fmt="%Y-%m-%d", title="Covid-19 : French departments'number of deaths",n_visible=15)
    elif granu == "departement" and option == "cas_confirmes":
        df_clean.plot_animated("temp/covid-19-h-bar-cases_departement.gif", period_fmt="%Y-%m-%d", title="Covid-19 : French departments'number of deaths",n_visible=15)
    elif granu == "region" and option == "deces":
        df_clean.plot_animated("temp/covid-19-deaths-regions.gif", 
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
        df_clean.plot_animated("temp/covid-19-cases-region.gif", 
                            title="Covid-19 : Evoulution of French regions deaths counts", 
                            kind='line', 
                            period_fmt="%Y-%m-%d", 
                            period_label={ 
                                'x':0.25, 
                                'y':0.9, 
                                'family': 'sans-serif', 
                                'color': 'darkred' 
                            })
    end = time.time()
    print("Time spent on plot_animation: {0:.5f} s.".format(end - start)) 

