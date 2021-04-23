import pydeck as pdk
import pandas as pd
import geopandas as gpd
import ipywidgets
from ipywidgets import interact, interactive_output, Play, jslink, HBox, IntSlider



class Map_covid:
    """Creates an animated map.

    :param df_covid: dataframe with covid data
    :type df_covid: dataframe
    :param granularity: dep or region
    :type granularity: dataframe
    :param cases: column from df_covid
    :type cases: str
    """


    def __init__(self, df_covid, granularity, cases):
        """
        Construction method.
        Create an initial map.
        """
        self.df_covid = df_covid
        self.granularity = granularity
        self.cases = cases
        self.granularity = self.granularity.assign(cases=0)
        self.df_sort = pd.DataFrame(self.df_covid.sort_values(['date']))
        self.date_record = self.df_covid.groupby(['date']).size()
        if self.granularity.code[0] == '11':
            self.map_layer = pdk.Layer(
                                "GeoJsonLayer",
                                self.granularity,
                                opacity=0.8,
                                stroked=False,
                                filled=True,
                                extruded=True,
                                wireframe=True,
                                get_elevation="cases*50",
                                get_fill_color="[255, cases/200, cases/20]",
                                get_line_color=[255, 255, 255],
                            )
        else:
            self.map_layer = pdk.Layer(
                                "GeoJsonLayer",
                                self.granularity,
                                opacity=0.8,
                                stroked=False,
                                filled=True,
                                extruded=True,
                                wireframe=True,
                                get_elevation="cases*100",
                                get_fill_color="[255, cases/200, cases/20]",
                                get_line_color=[255, 255, 255],
                            )
        init_view = pdk.ViewState(latitude=50.01200, longitude=3.17270, zoom=6, max_zoom=16, pitch=45, bearing=0)
        self.map_covid = pdk.Deck(layers=[self.map_layer], initial_view_state=init_view)


    def update_plot(self, date_index):
        """
        Update the map plot accordign to a slider widget.

        :param date_index: time slider with all the date in df_covid
        :type date_index: ipywidgets.IntSlider
        """
        date = self.date_record.index[date_index]
        df_jour = self.df_sort.loc[self.df_sort['date'] == date]
        for i in self.granularity.index :
            self.granularity.loc[i,"cases"] = 0
        for i in df_jour.index :
            self.granularity.loc[self.granularity["code"] == df_jour.loc[i,"maille_code"], "cases"] = df_jour.loc[i, self.cases]
        print(date)
        self.map_layer.data = self.granularity
        return self.map_covid.update()
    

    def widget(self):
        """
        Create a widget with time slider with every date.
        """
        time_slider = ipywidgets.IntSlider(value=0, min=0, max=self.date_record.size-1, step=1)
        play = ipywidgets.Play(value=0, min=0, max=self.date_record.size-1, step=1, description='Press play', interval=50)
        ipywidgets.jslink((play, 'value'), (time_slider, 'value'))
        layout = ipywidgets.HBox([time_slider, play])
        interaction = interactive_output(self.update_plot, {'date_index': time_slider})
        return layout, interaction


    def plot_all(self):
        """
        Display the animated map with the widget.
        """
        layout, interaction = self.widget()
        self.map_covid.update()
        display(layout, interaction)
        display(self.map_covid.show())

  
    