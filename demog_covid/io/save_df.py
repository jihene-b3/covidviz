import pandas as pd
from download import download
from demog_covid.io import url_db, path_target
import os 
   
url_ag = "https://www.data.gouv.fr/fr/datasets/r/08c18e08-6780-452d-9b8c-ae244ad529b3'"
path_target_ag = os.path.join(path_target, "AgeGroups.csv")


class Load_transfer:
    """
    
    """
    def __init__(self, url=url_ag, target_name=path_target_ag):
        download(url, target_name, replace=True)
        # above, set replace to True to always get the updated version

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target_ag)
        return df
  
  
  
