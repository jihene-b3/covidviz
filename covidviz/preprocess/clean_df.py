import pandas as pd
import numpy as np


def choose_columns(df_covid, col_names):
    """
    Return a dataframe with only the chosen columns,
    exctract only interresting columns of df_covid.

    :param df_covid: dataframe with covid data
    :type df_covid: dataframe
    :param col_names: column names from df_covid
    :type col_names: list of str
    """
    df = df_covid.loc[:,col_names]
    return df


def choose_granularity(df_covid, granularity):
    """
    Return a dataframe with only the chosen granularity.

    :param df_covid: dataframe with covid data
    :type df_covid: dataframe
    :param granularity: element in ["departement", "region", "pays", "monde"]
    :type granularity: str
    """
    # keep only departements for the granularity
    df = df_covid.loc[df_covid['granularite']==granularity,:]
    return df