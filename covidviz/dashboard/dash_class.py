class Dashapp:

    """
    Dash application
    """

    def __init__(self):
        """ Initialise the attributes """

        self.app = dash.Dash(__name__)
        self.app.layout = self.build_layout


    def run_app(self):
        """ Run the dash app """
        if __name__ == '__main__':
            dash_app = Dashapp()
            dash_app.app.run_server(debug=False)       



    def get_options(self, list_location):
        """ Get options for the dropdown. Creates a list of dictionaries, which have the keys 'label' and 'value'.
        
        :param list_location: list of location (for example the list of French departmental codes)
        :type list-location: list
        """
        dict_list = []
        for i in list_location:
            dict_list.append({'label': i, 'value': i})
            return dict_list


    def build_layout(self, df):
        """ Build the layout app 
        
        :param df: pandas dataframe
        :type df: pandas.DataFrame
        """

        layout = html.Div(
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
                                options= self.get_options(df['codelocation'].unique()),
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
                                dcc.Graph(id='ts_weekly',
                                        config={'displayModeBar': False},
                                        animate=True),

                                dcc.Graph(id='ts_daily',
                                        config={'displayModeBar': False},
                                        animate=True),
                    
                                html.Div(className='div-for-charts', 
                                        children=[
                                            html.Iframe(id='map', srcDoc =open('geojson_layer.html','r').read(), width='100%', height='600' ),
                                            dcc.Graph(id='total_vacc',
                                                    config={'displayModeBar': False},
                                                    animate=True)
                                                    ])
                                                    ])
                                                    ])


                              


 
# Visualize callbacks graph


# Exemple Callback


def callback(id_input, prop_input, id_output, prop_output):
    """ 
    
    :param id_input: id of input component, for example 'selector'
    :param prop_input: property of input component for example 'value'
    :param id_output: id of output component, for example 'timeseries'
    :param prop_output: property of output component, for example 'figure'

    :type id_input: string
    :type prop_input: string
    :type id_output string
    :type prop_output: string

    """

    @app.callback(Output(id_output, prop_input),
              [Input(id_input, prop_input)])


@app.callback(Output('id of output component', 'property of output component'),
              [Input('id of input component', 'property of input component')])

def arbitrary_function(value_of_first_input):
    '''
    The property of the input component is passed to the function as value_of_first_input.
    The functions return value is passed to the property of the output component.
    '''
    return arbitrary_output


  
# Callback for timeseries number of vaccinations per week


@app.callback(Output('ts_weekly', 'figure'),
            [Input('locselector', 'value')])
            
def update_ts_week(selected_dropdown_value):
    ''' Draw traces of the feature 'value' based one the currently 
    selected location '''

    # Step 1
    trace1 = []
    df_sub = df

    #Step 2 : Draw and append traces for each location
    for codelocation in selected_dropdown_value:
        trace1.append(go.Scatter(x=df_sub[df_sub['codelocation'] == codelocation].index,
                                y=df_sub[df_sub['codelocation'] == codelocation]['weekly'],
                                mode='lines',
                                opacity=0.7,
                                name= codelocation,
                                textposition='bottom center'))
    
    #Step 3
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]

    #Step 4 : Define figure

    figure = {'data': data,
                'layout': go.Layout(
                colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                margin={'b': 15},
                hovermode='x',
                autosize=True,
                title={'text': 'Number of vaccinations per week', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
            ),

            }

    return figure
 


# Callback for timeseries number of vaccinations per day
 
@app.callback(Output('ts_daily', 'figure'),
              [Input('locselector', 'value')])

def update_ts_daily(selected_dropdown_value):


    #Draw traces of the feature 'daily' based one the currently selected location
    trace2 = []
    df_sub = df
    # Draw and append traces for each location
    for codelocation in selected_dropdown_value:
        trace2.append(go.Scatter(x=df_sub[df_sub['codelocation'] == codelocation].index,
                                 y=df_sub[df_sub['codelocation'] == codelocation]['daily'],
                                 mode='lines',
                                 opacity=0.7,
                                 name=codelocation,
                                 textposition='bottom center'))
    traces = [trace2]
    data = [val for sublist in traces for val in sublist]
 
    # Define Figure
 
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'t': 50},
                  height=500,
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Number of vaccinations per day', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
              ),
              }
 
    return figure
 
 
 # Callback for total number of vaccinations
 
@app.callback(Output('total_vacc', 'figure'),
              [Input('locselector', 'value')])

def update_total_vacc(selected_dropdown_value):

    #Draw traces of the feature 'cumul' based one the currently selected location
    trace3 = []
    df_sub = df
    # Draw and append traces for each location
    for codelocation in selected_dropdown_value:
        trace3.append(go.Scatter(x=df_sub[df_sub['codelocation'] == codelocation].index,
                                 y=df_sub[df_sub['codelocation'] == codelocation]['tot_vacc'],
                                 mode='lines',
                                 opacity=1,
                                 name=codelocation,
                                 textposition='bottom center'))
    traces = [trace3]
    data = [val for sublist in traces for val in sublist]
 
    # Define Figure
 
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'t': 50},
                  height=500,
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Total number of vaccinations', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
              ),
              }
 
    return figure


