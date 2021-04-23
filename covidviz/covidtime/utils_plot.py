import pandas as pd
from download import download
import plotly.express as px
import matplotlib.pyplot as plt 

def df_plot_rea(df) :
    fig = px.bar(df, x="AgeGroup",
        y="nb-rea",
        color="AgeGroup",
        animation_frame="date", 
        animation_group="AgeGroup",
        range_y=[0,30])
    fig.update_layout(
        height=600,
        title_text="Nombre de patients en réanimation par classe d'âge")
    return(fig.show())


def df_plot_hosp(df):
    fig = px.bar(df, x="AgeGroup", y="nb_hosp", color="AgeGroup",
         animation_frame="date", animation_group="AgeGroup", 
         range_y = [0,150])
    fig.update_layout(
    height = 600,
    title_text="Nombre de patients hospitalisés par classe d'âge"
    )
    return(fig.show())

def df_plot_dec(df): 
    datefrom = '2020-04-01'
    fig = px.line(df, x="date", y="dec_Tot", color="AgeGroup",range_x=[datefrom,'2021-04-19'])
    # fig.update_layout(hovermode='x unified')
    fig.update_layout(
    height = 600,
    title_text = "Nombre de patients décédès par classes d'âges"
    )
    return(fig.show())

def df_plot_gender(df):
    w = 0.3
    x = df.AgeGroup
    boys = df.num_h
    girls = df.num_f
    plt.bar(x, boys, w, label= "boys")
    plt.bar(x, girls, w, bottom=boys, label="girls")
    plt.xlabel("AgeGroups")
    plt.ylabel("Number of people tested positive")
    plt.title("Distribution of tested postive people for coronavirus per gender")
    plt.legend()
    return(plt.show())


