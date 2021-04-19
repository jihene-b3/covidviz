import pandas as pd 
import numpy as np 


def clean_age(df): 
    #
    df = pd.read_csv("data/AgeGroups.csv", sep=';')
    df=df.rename(columns={"cl_age90": "age", "jour": "date","hosp":"nb_hosp","rea":"nb-rea","HospConv":"nb_hospconv","rad":"rad_Tot","dc":"dec_Tot"})
    df.drop(['autres'], axis = 1, inplace = True) 
    df=df[df['nb_hosp'] > 0]
    return(df)


def clean_gender(df): 
    
    """
    This function changes "age_gender.csv" file by ;
    - renaming columns, 
    - droping a column not needed for this case study,
    """
    df = pd.read_csv("data/age_gender.csv", sep=';')
    df=df.rename(columns={"cl_age90": "age","P_f":"num_f","P_h":"num_h","pop_f":"prooption_f","pop_h":"prooption_h"})
    df.drop(['fra'], axis = 1, inplace = True) 
    return(df)


def format_age(df):
    
    """
    This functun creates 10 age groups and adds a column in the dataframe referring to it.
    """
    df.loc[(df.age < 10),  'AgeGroup'] = '[0,9]'
    df.loc[(df.age > 9) & (df.age < 20),  'AgeGroup'] = '[10,19]'
    df.loc[(df.age > 19) & (df.age < 30),  'AgeGroup'] = '[20,39]'
    df.loc[(df.age > 29) & (df.age < 40),  'AgeGroup'] = '[30,39]'
    df.loc[(df.age > 39) & (df.age < 50),  'AgeGroup'] = '[40,49]'
    df.loc[(df.age > 49) & (df.age < 60),  'AgeGroup'] = '[50,59]'
    df.loc[(df.age > 59) & (df.age < 70),  'AgeGroup'] = '[60,69]'
    df.loc[(df.age > 69) & (df.age < 80),  'AgeGroup'] = '[70,79]'
    df.loc[(df.age > 79) & (df.age < 90),  'AgeGroup'] = '[80,89]'
    df.loc[(df.age > 89),  'AgeGroup'] = '[90,+]'
    return(df)

def remove_nan(df):
    """
    This function select numerical columns and remive NAN values with linear interpolation method.
    DataFrame objects have interpolate() that, by default, performs linear interpolation at missing data points
    """
    numeric = df.select_dtypes(include=np.number)
    numeric_columns = numeric.columns
    df[numeric_columns] = df[numeric_columns].interpolate(method ='linear', limit_direction ='forward')
    return(df)

def enable_time_series_plot(
    in_df, timein_field="time", timeseries_field_out="date", date_format="%Y-%m-%d",
):
    """
    We have noticed an error in "2020-11_11" date so we drop it.
    This is a small tool to add a format date of a dataframe which can be used for time series
    plotting.
    """
    if timeseries_field_out not in in_df.columns:
        # Drop the bad data row.
        in_df = in_df.loc[in_df[timein_field] != "2020-11_11", :]
        in_df[timeseries_field_out] = pd.to_datetime(
            in_df[timein_field], format=date_format
        )
    return in_df



