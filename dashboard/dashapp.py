import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

#Load the data

df = pd.read_csv('df_vacc.csv', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['date'])


import plotly.graph_objects as go 
fig = px.line(df, x=df.index, 
              y= df["weekly"],
              color='codelocation',
              template='plotly_dark').update_layout(
                  {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                   'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

config = dict({'scrollZoom': True})
              

# Creates a list of dictionaries, which have the keys 'label' and 'value'.
def get_options(list_location):
  dict_list = []
  for i in list_location:
    dict_list.append({'label': i, 'value': i})
  return dict_list

# Initialization of the dash app

app = dash.Dash(__name__)

# Define the dash app

app.layout = html.Div(
    children=[
        html.Div(className='row', #Define the row element
                 children=[
                    html.Div(className='four columns div-user-controls', #Left element
                             children=[
                                 html.H2('COVID DASHBOARD'),
                                 html.P('Visualising time series with Plotly - Dash.'),
                                 html.P('Pick one or more location from the dropdown below.'),
                                 html.Div(className='div-for-dropdown',
                                          children=[
                                                    dcc.Dropdown(id='locselector',
                                                                 options=get_options(df['codelocation'].unique()),
                                                                 multi=True,
                                                                 value=[df['codelocation'].sort_values()[0]],
                                                                 style={'backgroundColor': '#1E1E1E'},
                                                                 className='locselector')
                                                    ],
                                          style={'color': '#1E1E1E'})
                                 ]
                             ),
                    html.Div(className='eight columns div-for-charts bg-grey', #Right element
                             children=[
    dcc.Graph(id='timeseries',
              config={'displayModeBar': False},
              animate=True,
              figure=fig)
])
                    
                    ])
                              ])
# Run the dash app

app.run_server(debug=True)
