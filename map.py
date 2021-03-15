
import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt
import string
import os
import pandas as pd
import requests
import tempfile
import zipfile
import covidmap as cm


# data containing geometric data on French cities
url = 'https://www.data.gouv.fr/fr/datasets/r/07b7c9a2-d1e2-4da6-9f20-01a7b72d4b12'
temporary_location = tempfile.gettempdir() 

# unzip file or folder from an url
# to put in covidmap ??
def download_unzip(url, dirname, destname):
  myfile = requests.get(url)
  open(dirname + '/' + destname + '.zip', 'wb').write(myfile.content)
  with zipfile.ZipFile(dirname + '/' + destname + '.zip', 'r') as zip_ref:
      zip_ref.extractall(dirname + '/' + destname)


download_unzip(url, temporary_location, "borders")

# dataframe of the cities in France
cities = gpd.read_file(temporary_location + "/borders/communes-20190101.json")


# assigns a number of a department to each city thanks to insee, the postal code of each city
# 2 first number of the insee = department number
cities['dep'] = cities.insee.str[:2] 
#print(cities.head())

# dataframe of the metropolitan French departments
departments = cities[cities.dep != "97"].dissolve(by='dep')
departments.plot()

# dataframe of overseas French departments
overseas = cities[cities.dep == "97"].dissolve(by='dep')
# overseas.plot()

all_dep = cities.dissolve(by='dep')
# all_dep.plot()

plt.tight_layout(pad=0)
plt.show()







