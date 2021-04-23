import pandas as pd
from download import download
from covidviz.io import url_db, path_target

class Load_db:
  """
  Download a file from an url to a target path and put it in a dataframe
  :param url: url 
  :param target_name: path target
  """
  def __init__(self, url, target_name):
    self.url = url_db
    self.target_name = path_target
    download(self.url, self.target_name, replace=False)
  
  @staticmethod
  def save_as_df():
  """
  Static method, save .csv as a dataframe
  """
    df_covid = pd.read_csv(path_target, na_values="", low_memory=False)
    return df_covid