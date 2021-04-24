import pandas as pd
from download import download
from covidviz.io import url_db, path_target
import time

class Load_db:
  """
  Download a file from an url to a target path and put it in a dataframe
  :param url: url 
  :param target_name: path target
  """
  def __init__(self):
    """
    Construction method
    """
    start = time.time()
    self.url = url_db
    self.target_name = path_target
    download(self.url, self.target_name, replace=False)
    end = time.time()
    print("Time spent to load data: {0:.5f} s.".format(end - start)) 
  
  @staticmethod
  def save_as_df():
    """
    Static method, save .csv as a dataframe
    """
    start = time.time()
    df_covid = pd.read_csv(path_target, na_values="", low_memory=False)
    end = time.time()
    print("Time spent to save data: {0:.5f} s.".format(end - start)) 
    return df_covid