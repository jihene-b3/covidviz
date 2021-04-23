import pandas as pd
import numpy as np
import time

def choose_columns(df_covid, col_names):
    """
    Return a dataframe with only the chosen columns,
    exctract only interresting columns of df_covid.

    :param df_covid: dataframe with covid data
    :type df_covid: dataframe
    :param col_names: column names from df_covid
    :type col_names: list of str
    """
    start = time.time()
    df = df_covid.loc[:,col_names]
    end = time.time()
    print("Time spent for choose_columns: {0:.5f} s.".format(end - start)) 
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
    start = time.time()
    df = df_covid.loc[df_covid['granularite']==granularity,:]
    end = time.time()
    print("Time spent for choose_granularity: {0:.5f} s.".format(end - start)) 
    return df