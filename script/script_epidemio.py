#%%

# import packages :
import pandas as pd
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))
import covidviz as cvz
from matplotlib import pyplot as plt
from IPython.display import display, Markdown
from covidviz.preprocess.clean_df import choose_columns,choose_granularity
from covidviz.covidtime.viz_epidemio import data_preparation,data_preproc,axis_date_limits,plot_field_loops,enable_time_series_plot
#from covidviz.io.load_db import Load_db

#%%
data = cvz.choose_columns(cvz.Load_db.save_as_df(), ['date', 'granularite', 'maille_code', 'maille_nom', 'reanimation','deces', 'cas_confirmes','gueris','source_nom','hospitalises', 'deces_ehpad'])
#%%
data = cvz.enable_time_series_plot(data, timein_field="date", timeseries_field_out="t")

#%%
def plots_maille_code(maille_active='FRA', **kwargs):
    fra = data_preproc(data, maille_active)
    plt.close()
    # plot_field_loops(fra, "deces_ehpad", center=False, maille_active=maille_active)
    plot_field_loops(fra, "hospitalises_cumul", [7], center=True, maille_active=maille_active, **kwargs)
    plot_field_loops(fra, "reanimation_cumul", [7], center=True, maille_active=maille_active, **kwargs)
    plot_field_loops(fra, "deces", center=True, maille_active=maille_active, **kwargs)
    if maille_active == "FRA":
        plt.show()
        display(Markdown(
            "The number of cases is smoothed over 14 days with a triangular window"
        ))
        plot_field_loops(
            fra, "cas_confirmes", [14], center=True, maille_active=maille_active,
            win_type='triang', **kwargs
        )
    return fra


#%%
maille_active = 'FRA'
fra = cvz.data_preproc(data, maille_active)
fra.tail(10)

#%%
_ = plots_maille_code(maille_active='FRA', start_date='2020-04-01')

#%% Zomm in the period after the last lockdown
_ = plots_maille_code(maille_active='FRA', start_date='2021-01-01')

#%%
_ = plots_maille_code(maille_active='REG-76')

#%%list_reg = [r for r in data["maille_code"].unique() if "REG" in r]
list_reg = [r for r in data["maille_code"].unique() if "REG" in r]
for reg in list_reg:
    cvz.data_preproc(data, reg)