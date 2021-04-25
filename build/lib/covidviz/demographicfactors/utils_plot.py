import pandas as pd
from download import download
import plotly.express as px
import matplotlib.pyplot as plt 
import time


def df_plot_rea(df) :
    """
    Creates a chart with a time slider of the number of intensive care patients by age group.
    """
    start = time.time()
    fig = px.bar(df, x="AgeGroup",
        y="nb-rea",
        color="AgeGroup",
        animation_frame="date", 
        animation_group="AgeGroup",
        range_y=[0,30])
    fig.update_layout(
        height=600,
        title_text="Number of intensive care patients by age group")
    end = time.time()
    print("Time spent on plot_rea: {0:.5f} s.".format(end - start))
    return(fig.show())


def df_plot_hosp(df):
    start = time.time()
    fig = px.bar(df, x="AgeGroup", y="nb_hosp", color="AgeGroup",
         animation_frame="date", animation_group="AgeGroup", 
         range_y = [0,150])
    fig.update_layout(
    height = 600,
    title_text="Number of patients hospitalized by age group"
    )
    end = time.time()
    print("Time spent on plot_hosp: {0:.5f} s.".format(end - start))
    return(fig.show())

def df_plot_dec(df): 
    start = time.time()
    datefrom = '2020-04-01'
    fig = px.line(df, x="date", y="dec_Tot", color="AgeGroup",range_x=[datefrom,'2021-04-19'])
    # fig.update_layout(hovermode='x unified')
    fig.update_layout(
    height = 600,
    title_text = "NNumber of patients who died because of coronavirus by age group"
    )
    end = time.time()
    print("Time spent on plot_dec: {0:.5f} s.".format(end - start))
    return(fig.show())

def df_plot_gender(df):
    start = time.time()
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
    end = time.time()
    print("Time spent on plot_gender: {0:.5f} s.".format(end - start))
    return(plt.show())


