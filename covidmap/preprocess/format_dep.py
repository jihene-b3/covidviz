
def format_dep(df_covid):
    """
    Format the dataframe by changing 'maille_code' with the format 'DEP-XX' in the format 'XX'.
    For instance, "DEP-33" becomes "33".
    :param df_covid: dataframe with covid data
    """
    df = df_covid.copy()
    df['maille_code'] = df_covid.loc[:,'maille_code'].map(lambda x: x.lstrip('DEP-') if type(x) == str else -1)
    return df