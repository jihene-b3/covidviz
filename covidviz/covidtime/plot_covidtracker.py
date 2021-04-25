import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz
from covidviz import data 
from covidviz.preprocess.clean_df import choose_columns, choose_granularity
import matplotlib.pyplot as plt 
import pandas as pd
import matplotlib.ticker as mtick
import time


def ratio(gb_data, data_depcode, data_ratio_hospitalises,current_date, data_hospitalises, current_date_file, min_value_80p , nbhospitalises_80p) : 
    """Creates an updated chart of the ratio of in-hospital deaths to hospitalizations in french departments.

    :param gb_data: dataframe with covid data
    :type gb_data: dataframe
    :param data_depcode: column 'maille_nom' of the dataframe
    :type data_depcode: list
    :param data_ratio_hospitalises: (gb_data['deces'] / (gb_data['hospitalises'] + gb_data['gueris'])) * 100
    :type data_ratio_hospitalises: str
    :param current_date : gives the maximum date of the dataframe
    :type current_date : timestamp
    :param min_value_80p : 
    :type min_value_80p
    :param nbhospitalises_80p
    :type nbhospitalises_80p
    """
    start = time.time()
    fig, ax = plt.subplots(figsize=(12, 8))

    plt.title(f"Ratio of in-hospital deaths to hospitalizations : {current_date}", fontsize=20)
    plt.ylabel("Total number of deceases / Total number of hospitalized")
    plt.xlabel("Total number of hospitalized")

    for i, txt in enumerate(data_depcode):
        if (data_hospitalises[i] > data_hospitalises.max() * 0.20):
            ax.annotate(txt, (data_hospitalises[i], data_ratio_hospitalises[i]), xytext=(data_hospitalises[i] + 20, data_ratio_hospitalises[i]))        

    plt.axhline(data_ratio_hospitalises.mean(), color='green', linestyle='--', label=f'average death ratio ({data_ratio_hospitalises.mean():.2f}%)')

    plt.axvline(min_value_80p, color='pink', linestyle='-', label=f"80% of the number of hospitalized people in France are on the right side of the line ({nbhospitalises_80p:.0f} hospitalized)")

    ax.scatter(data_hospitalises, data_ratio_hospitalises)

    ax.annotate('updated chart',xy=(1, 0), xytext=(-15, 10), fontsize=15,
        xycoords='axes fraction', textcoords = 'offset points',
        bbox=dict(facecolor = 'white', alpha = 0.9),
        horizontalalignment = 'right', verticalalignment = 'bottom')

    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0f%%'))
    plt.legend()

    current_date_file = gb_data['date'].max().strftime('%Y%m%d')
    end = time.time()
    print("Time spent on ratio plot: {0:.5f} s.".format(end - start)) 
    plt.show()
