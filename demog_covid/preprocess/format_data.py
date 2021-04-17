import pandas as pd 

def clean_age(df): 

    df = pd.read_csv("AgeGroups.csv", sep=';')
    df=df.rename(columns={"cl_age90": "age", "jour": "date","hosp":"nb_hosp","rea":"nb-rea","HospConv":"nb_hospconv","rad":"rad_Tot","dc":"dec_Tot"})
    df.drop(['autres'], axis = 1, inplace = True) 
    df=df[df['nb_hosp'] > 0]
    return(df)

def class_age(df):
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



