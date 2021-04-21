
import geopandas as gpd
#import contextily as ctx
import matplotlib.pyplot as plt
import string
import pandas as pd
import requests
import tempfile
import zipfile


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
# print(cities.head())


# dataframe of the metropolitan French departments
departments = cities[cities.dep != "97"].dissolve(by='dep')
departments.plot(column="insee", cmap='Pastel2')

# dataframe of overseas French departments
# overseas = cities[cities.dep == "97"].dissolve(by='dep')
# overseas.plot()

# overseas departments (DOM): 
guadeloupe = cities[cities.insee.str[:3]  == "971"].dissolve(by='dep')
martinique = cities[cities.insee.str[:3]  == "972"].dissolve(by='dep')
guyane = cities[cities.insee.str[:3]  == "973"].dissolve(by='dep')
reunion = cities[cities.insee.str[:3]  == "974"].dissolve(by='dep')
mayotte = cities[cities.insee.str[:3]  == "975"].dissolve(by='dep')



# overseas departments plot 
fig, axes = plt.subplots(3, 2)

for i in range(3):
  for j in range(2):
    axes[i, j].set_axis_off()

axes[0, 0].set_title("Guadeloupe")
axes[1, 0].set_title("Martinique")
axes[2, 0].set_title("Guyane")
axes[0, 1].set_title("La Reunion")
axes[1, 1].set_title("Mayotte")
guadeloupe.plot(ax=axes[0, 0])
martinique.plot(ax=axes[1, 0])
guyane.plot(ax=axes[2, 0])
reunion.plot(ax=axes[0, 1])
mayotte.plot(ax=axes[1, 1])

axes[2, 1].remove()



# plt.tight_layout(pad=0)
plt.show()







