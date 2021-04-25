[![Documentation Status](https://readthedocs.org/projects/covidviz/badge/?version=latest)](https://covidviz.readthedocs.io/en/latest/?badge=latest)

# Spatio-temporal evolution of Covid19 cases in France

## Plot interactive maps

The goal of this project is to analyze the spreading of the covid19 disease in France with an animated map. Which allows to visualize by day covid cases in French departments like that :


![Map - Animated map](temp/map_departments.png)


 

Then we'll produce various charts and gif to illustrate how the covid19 affect population, for instance by age (e.g. a dashboard with various statistical features). 


[<img src="temp/covid-19-h-bar-cases_departement.gif" height="500">]()




## Dataset

We mainly used data from data.gouv.fr [data.gouv.fr](https://www.data.gouv.fr/en/datasets) which provides a counting of Covid-19 such as :

> - [Data on people vaccinated against Covid-19](https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1/)

> - [Global Covid-19 data with deads and hospitalized](https://www.data.gouv.fr/en/datasets/chiffres-cles-concernant-lepidemie-de-covid19-en-france/)

We also used geometry data used for maps are from [France geoJSON](https://france-geojson.gregoiredavid.fr).


## Members
+ Jihène Belgaied : jihene.belgaied@etu.umontpellier.fr
+ Zakaria Laabsi : zakaria.laabsi@etu.umontpellier.fr
+ Chloé Serre-Combe : chloe.serre-combe@etu.umontpellier.fr
+ Stephani Ujka : stephani.ujka@etu.umontpellier.fr

## Tasks repartition 

+ Jihène : spatio-temporal covid19 evolution statistics
+ Zakaria : vaccine statistics and map on a dashboard 
+ Chloé : covid deaths and covid hospitalized widget maps, unit tests and wheel
+ Stephani : icu and screening statistic 

+ Everyone : documentation, beamer, module architecture, time and memory efficiency...




