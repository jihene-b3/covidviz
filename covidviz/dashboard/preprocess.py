import pandas as pd
import geopandas as gpd


def preprocess(df,gdf):
    """ Does the processing by concatenating a dataset and a geodataframe with the index(department code for example) in common. 
    This gives a Pandas dataframe containing for each date a list of departments with their associated geometric contours 
    
    :param df: dataset (CSV file)
    :param gdf: GeoJSON file
    :type df : string
    :type gdf : string
    """

    
    df_vacsi = pd.read_csv(df)
    df_vacsi = df_vacsi[1:]
    df_vacsi['date'] = pd.to_datetime(df_vacsi['date'])
    df_vacsi.head(10)

    df_jour = df_vacsi['date'].drop_duplicates()
    max = df_jour.max()


    df_vacsi['code'] = df_vacsi['codelocation']

    temp_df = dict()
    for i in df_jour :
        temp_df[i] = df_vacsi.loc[ df_vacsi['date'] == i]
    dict_df = dict()
    for key, df in temp_df.items() :
        dict_df[key] = df.groupby('code').max().drop(['codelocation','where','Unnamed: 0'], axis=1



    #gdf  = 'departements-avec-outre-mer.geojson'
    f = gpd.read_file(gdf)
    f = f.set_index('code')
    f = f.sort_index(axis=0)

    

    dict_vaccin = dict()
    for i in df_jour :
        dict_vaccin[i] = pd.concat([f,dict_df[i]], axis = 1)
    

    ts_vacc = pd.concat(dict_vaccin, axis=0)
    ts_vacc.sort_index(ascending=True)

    ts_vacc = ts_vacc.dropna()
    ts_vacc['date'] = ts_vacc['date'].astype(str) +' '+ '00:00'

