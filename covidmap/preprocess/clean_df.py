import pandas as pd
import numpy as np


def choose_columns(df_covid, col_names):
    """
    Return a dataframe with only the chosen columns,
    exctract only interresting columns of df_covid
    :param df_covid: dataframe with covid data
    :param col_names: list of strings containing column names from df_covid
    """
    df = df_covid.loc[:,col_names]
    return df

def choose_granularity(df_covid, granularity):
    """
    Return a dataframe with only the chosen granularity
    :param df_covid: dataframe with covid data
    :param granularity: str in ["departement", "region", "pays", "monde"]
    """
    # keep only departements for the granularity
    df = df_covid.loc[df_covid['granularite']==granularity,:]
    return df