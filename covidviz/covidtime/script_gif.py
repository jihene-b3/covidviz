
import pandas as pd
import pandas_alive
from download import download 
import covidviz
from covidviz import *
from preprocess.format_data import enable_time_series_plot

#import data
url = 'https://github.com/opencovid19-fr/data/raw/master/dist/chiffres-cles.csv'
path_target = "covidviz/covidtime/data/chiffre-cles.csv"
download(url, path_target, replace=True)
_data = pd.read_csv("covidviz/covidtime/data/chiffre-cles.csv")

## comparaison entre départements 
#1.compare deces
#format data 
enable_time_series_plot(_data)
_data = _data[_data.date != '2020-11_11']
_data['date'] = pd.to_datetime(_data['date'])
_data = _data.loc[_data['granularite'] == "departement",:]

#current_date = _data['date'].max().strftime('%d/%m/%Y')

df_dep=_data.groupby(['maille_nom','date'])['deces'].sum().reset_index()
df_dep=df_dep.set_index(['maille_nom','date'])
#df_dep.index=df_dep.index.set_levels([df_dep.index.levels[0], pd.to_datetime(df_dep.index.levels[1])])
df_dep=df_dep.sort_values(['maille_nom','date'],ascending=True)
df=df_dep[df_dep['deces'] > 0]

df.reset_index(inplace=True)
df_clean = df.pivot(index="date", columns="maille_nom",values="deces").fillna(0)
df_clean.plot_animated("covidviz/covidtime/output/covid-19-h-bar-deaths.gif", period_fmt="%Y-%m-%d", title="Covid-19 Departments number of deaths",n_visible=15)

df_clean.plot_animated("covidviz/covidtime/output/covid-19-v-deaths-bar.gif", 
                     period_fmt="%Y-%m-%d", 
                     title="Covid-19 Departments number of deaths", 
                     orientation='v',n_visible=15)

##compare les cas_confirmés : 

df_dep_confirmes=_data.groupby(['maille_nom','date'])['cas_confirmes'].sum().reset_index()
df_dep_confirmes=df_dep_confirmes.set_index(['maille_nom','date'])

df_dep_confirmes=df_dep_confirmes.sort_values(['maille_nom','date'],ascending=True)
df11=df_dep_confirmes[df_dep_confirmes['cas_confirmes'] > 0]
df_dep_confirmes.reset_index(inplace=True)

df_confirmes = df_dep_confirmes.pivot(index="date", columns="maille_nom",values="cas_confirmes").fillna(0) 
df_confirmes.plot_animated("covidviz/covidtime/output/covid-19-h-bar-cases.gif", period_fmt="%Y-%m-%d", title="Covid-19 France Departments : number of cases over time",n_visible=15)
df_confirmes.plot_animated("covidviz/covidtime/output/covid-19-v-deaths-bar.gif", 
                     period_fmt="%Y-%m-%d", 
                     title="Covid-19 France Departments : number of cases over time", 
                     orientation='v',n_visible=15)