import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

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


app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='four columns div-user-controls',
                             children=[
                                 html.H2('COVID VACCINES TRACKER FRANCE'),
                                 html.P('Tracking vaccination rates by French department'),
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
                    html.Div(className='eight columns div-for-charts bg-grey',
                             children=[
    dcc.Graph(id='timeseries',
              config={'displayModeBar': False},
              animate=True)
])
                    
                    ])
                              ])

# Callback for timeseries number of vaccinations
@app.callback(Output('timeseries', 'figure'),
              [Input('locselector', 'value')])
def update_graph(selected_dropdown_value):
    trace1 = []
    df_sub = df
    for codelocation in selected_dropdown_value:
        trace1.append(go.Scatter(x=df_sub[df_sub['codelocation'] == codelocation].index,
                                 y=df_sub[df_sub['codelocation'] == codelocation]['weekly'],
                                 mode='lines',
                                 opacity=0.7,
                                 name= codelocation,
                                 textposition='bottom center'))
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Vaccinations', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
              ),

              }

    return figure

app.run_server(debug=True)
