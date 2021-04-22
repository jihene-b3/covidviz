
import pandas as pd
import pandas_alive
import covidviz
from covidviz import *
from covidviz.preprocess.format_data import *
from covidviz.preprocess.clean_df import choose_columns, choose_granularity

# load data from covidviz (because already set)
_data = choose_columns(Load_db.save_as_df(), ['date', 'granularite', 'maille_code', 'maille_nom', 'reanimation','deces', 'cas_confirmes','gueris','source_nom'])


# prepare data for gif requirements 

#enable_time_series_plot(_data)
def adapt_time(df):
   df = df[df.date != '2020-11_11']
   df['date'] = pd.to_datetime(df['date'])
   return df 

#adapt_time(_data)

_data = _data[_data.date != '2020-11_11']
_data['date'] = pd.to_datetime(_data['date'])

#compare les décès cas_confirmés : 

#_data = _data.loc[_data['granularite'] == "departement",:]

_data_department = choose_granularity(_data, 'departement')


df=_data_department.groupby(['maille_nom','date'])['deces'].sum().reset_index()
df=df.set_index(['maille_nom','date'])
#df_dep.index=df_dep.index.set_levels([df_dep.index.levels[0], pd.to_datetime(df_dep.index.levels[1])])
df=df.sort_values(['maille_nom','date'],ascending=True)
df=df[df['deces'] > 0]

df.reset_index(inplace=True)
df_clean = df.pivot(index="date", columns="maille_nom",values="deces").fillna(0)
df_clean.plot_animated("covidviz/covidtime/output/covid-19-h-bar-deaths.gif", period_fmt="%Y-%m-%d", title="Covid-19 Departments number of deaths",n_visible=15)

##compare les cas_confirmés entre départements : 

df_c=_data_department.groupby(['maille_nom','date'])['cas_confirmes'].sum().reset_index()
df_c=df_c.set_index(['maille_nom','date'])
#df_dep.index=df_dep.index.set_levels([df_dep.index.levels[0], pd.to_datetime(df_dep.index.levels[1])])
df_c=df_c.sort_values(['maille_nom','date'],ascending=True)
df_c=df_c[df_c['cas_confirmes'] > 0]

df_c.reset_index(inplace=True)
df_clean2 = df_c.pivot(index="date", columns="maille_nom",values="cas_confirmes").fillna(0)
df_clean2.plot_animated("covidviz/covidtime/output/covid-19-h-bar-cases.gif", period_fmt="%Y-%m-%d", title="Covid-19 France Departments number of cases",n_visible=15)

##comparaison des dèces entre les régions : 
_data_region = choose_granularity(_data, 'region')
df_r=_data_region.groupby(['maille_nom','date'])['deces'].sum().reset_index()
df_r=df_r.set_index(['maille_nom','date'])
#df_dep.index=df_dep.index.set_levels([df_dep.index.levels[0], pd.to_datetime(df_dep.index.levels[1])])
df_r=df_r.sort_values(['maille_nom','date'],ascending=True)
df_r=df_r[df_r['deces'] > 0]

df_r.reset_index(inplace=True)
df_clean_r = df_r.pivot(index="date", columns="maille_nom",values="deces").fillna(0)

df_clean_r.plot_animated("covidviz/covidtime/output/covid-19-deaths-regions.gif", 
                      title="Covid-19 Departments number of deaths", 
                      kind='line', 
                      period_fmt="%Y-%m-%d", 
                      period_label={ 
                         'x':0.25, 
                         'y':0.9, 
                         'family': 'sans-serif', 
                         'color': 'darkred' 
                      })

#comparaison des cas confirmés entre régions : 

df_r_c=_data_region.groupby(['maille_nom','date'])['cas_confirmes'].sum().reset_index()
df_r_c=df_r_c.set_index(['maille_nom','date'])
#df_dep.index=df_dep.index.set_levels([df_dep.index.levels[0], pd.to_datetime(df_dep.index.levels[1])])
df_r_c=df_r_c.sort_values(['maille_nom','date'],ascending=True)
df_r_c=df_r_c[df_r_c['cas_confirmes'] > 0]

df_r_c.reset_index(inplace=True)
df_clean_r = df_r_c.pivot(index="date", columns="maille_nom",values="deces").fillna(0)

df_clean_r.plot_animated("covidviz/covidtime/output/covid-19-cases.gif-regions", 
                      title="Covid-19 regions number of cases", 
                      kind='line', 
                      period_fmt="%Y-%m-%d", 
                      period_label={ 
                         'x':0.25, 
                         'y':0.9, 
                         'family': 'sans-serif', 
                         'color': 'darkred' 
                      })
