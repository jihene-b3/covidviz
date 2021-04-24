import time

def format_granularity(df_covid, granularity):
    """
    Format the dataframe by changing 'maille_code' with the format '___-XX' in the format 'XX',
    according to the granularity.
    For instance, "DEP-33" becomes "33" or "REG-11" becomes "11".

    :param df_covid: dataframe with covid data
    :type df_covid: dataframe
    :param granularity: region or departement
    :type granularity: str
    """
    start = time.time()
    df = df_covid.copy()
    if granularity == "region":
        df['maille_code'] = df_covid.loc[:,'maille_code'].map(lambda x: x.lstrip('REG-') if type(x) == str else -1)

    if granularity == "departement":
        df['maille_code'] = df_covid.loc[:,'maille_code'].map(lambda x: x.lstrip('DEP-') if type(x) == str else -1)
    end = time.time()
    print("Time spent to load data: {0:.5f} s.".format(end - start)) 
    return df

