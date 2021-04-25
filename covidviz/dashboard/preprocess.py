
def preprocess(df,gdf):
    
    df_vacsi = pd.read_csv(vacsi_dep)
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
        dict_df[key] = df.groupby('code').max().drop(['codelocation','where','Unnamed: 0'], axis=1)
    
    dict_df[max].head()



    gdf  = 'departements-avec-outre-mer.geojson'
    f = gpd.read_file(gdf)
    f = f.set_index('code')
    f = f.sort_index(axis=0)

    f.head()

    dict_vaccin = dict()
    for i in df_jour :
        dict_vaccin[i] = pd.concat([f,dict_df[i]], axis = 1)
    dict_vaccin[max].head(1000)

    ts_vacc = pd.concat(dict_vaccin, axis=0)
    ts_vacc.sort_index(ascending=True)

    ts_vacc = ts_vacc.dropna()
    ts_vacc['date'] = ts_vacc['date'].astype(str) +' '+ '00:00'

