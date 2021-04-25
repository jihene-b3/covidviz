import pandas as pd 
import numpy as np 
import time


def clean_age(df): 
    """
    This function reads "AgeGroups.csv" file and reformate data.

    """  
    start = time.time()
    
    df = df.rename(columns={"cl_age90": "age", "jour": "date", "hosp":"nb_hosp", "rea":"nb-rea", "HospConv":"nb_hospconv", "rad":"rad_Tot", "dc":"dec_Tot"})
    df.drop(['autres'], axis = 1, inplace = True) 
    df = df[df['nb_hosp'] > 0]
    
    end = time.time()
    print("Time spent on clean_age: {0:.5f} s.".format(end - start))

    return(df)


def clean_gender(df): 
    """
    This function changes "age_gender.csv" file by ;
    - renaming columns, 
    - droping a column not needed for this case study,
    """
    start = time.time()

    df = df.rename(columns={"cl_age90": "age", "P_f":"num_f", "P_h":"num_h", "pop_f":"prooption_f", "pop_h":"prooption_h"})
    df.drop(['fra'], axis = 1, inplace = True) 

    end = time.time()
    print("Time spent on clean_gender: {0:.5f} s.".format(end - start))

    return(df)


def format_age(df):
    
    """
    This functun creates 10 age groups and adds a column in the dataframe referring to it.
    """
    start = time.time()

    df.loc[(df.age < 10), 'AgeGroup'] = '[0,9]'
    df.loc[(df.age > 9) & (df.age < 20), 'AgeGroup'] = '[10,19]'
    df.loc[(df.age > 19) & (df.age < 30), 'AgeGroup'] = '[20,39]'
    df.loc[(df.age > 29) & (df.age < 40), 'AgeGroup'] = '[30,39]'
    df.loc[(df.age > 39) & (df.age < 50), 'AgeGroup'] = '[40,49]'
    df.loc[(df.age > 49) & (df.age < 60), 'AgeGroup'] = '[50,59]'
    df.loc[(df.age > 59) & (df.age < 70), 'AgeGroup'] = '[60,69]'
    df.loc[(df.age > 69) & (df.age < 80), 'AgeGroup'] = '[70,79]'
    df.loc[(df.age > 79) & (df.age < 90), 'AgeGroup'] = '[80,89]'
    df.loc[(df.age > 89), 'AgeGroup'] = '[90,+]'

    end = time.time()
    print("Time spent on format_age: {0:.5f} s.".format(end - start))

    return(df)


def group(df1):
    start = time.time()

    df_group = df1.groupby('AgeGroup')[['num_f', 'num_h', 'P']].aggregate(lambda x: x.mean())
    df_group.reset_index(inplace=True)

    end = time.time()
    print("Time spent on group: {0:.5f} s.".format(end - start))

    return df1




def remove_nan(df):
    """
    This function select numerical columns and remive NAN values with linear interpolation method.
    DataFrame objects have interpolate() that, by default, performs linear interpolation at missing data points
    """
    start = time.time()

    numeric = df.select_dtypes(include=np.number)
    numeric_columns = numeric.columns
    df[numeric_columns] = df[numeric_columns].interpolate(method ='linear', limit_direction ='forward')

    end = time.time()
    print("Time spent on remove_nan: {0:.5f} s.".format(end - start))

    return(df)


def enable_time_series_plot(
    in_df, timein_field="time", timeseries_field_out="date", date_format="%Y-%m-%d",
):
    """
    We have noticed an error in "2020-11_11" date so we drop it.
    This is a small tool to add a format date of a dataframe which can be used for time series
    plotting.
    """
    start = time.time()

    if timeseries_field_out not in in_df.columns:
        # Drop the bad data row.
        in_df = in_df.loc[in_df[timein_field] != "2020-11_11", :]
        in_df[timeseries_field_out] = pd.to_datetime(
            in_df[timein_field], format=date_format
        )
    
    end = time.time()
    print("Time spent on enable_time_series_plot: {0:.5f} s.".format(end - start))

    return in_df



