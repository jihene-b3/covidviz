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


                            

