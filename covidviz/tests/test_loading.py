import os.path, sys
import pandas as pd

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)
import covidviz as cvz

def test_load_db():
    test = cvz.Load_db().save_as_df()
    assert (type(test) == pd.core.frame.DataFrame)