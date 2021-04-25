
<p align="center">
  <strong> COVIDVIZ </strong> <br>
<img src="temp/map_departments.png" style="vertical-align:middle" width="200" height='200' class='center' alt='logo'>
</p>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jihene-b3/covidviz/blob/main/covidviz/dashboard/dashboard.ipynb)
[![Documentation Status](https://readthedocs.org/projects/covidviz/badge/?version=latest)](https://covidviz.readthedocs.io/en/latest/?badge=latest)


# Spatio-temporal evolution of Covid19 cases in France


In the context of a Software Developpement project we had to analyze the spreading of the covid19 disease in France with an animated map, which allows to visualize by day covid deaths in French departments.

Then we had to produce various charts and gif to illustrate how the covid19 affect population, for instance by age (e.g. a dashboard with various statistical features).

Here is an exemple of our work : 

[<img src="temp/covid-19-h-bar-cases_departement.gif" height="500">]()

To this aim, we create the module covidviz.





## Dataset

We mainly used data from data.gouv.fr [data.gouv.fr](https://www.data.gouv.fr/en/datasets) which provides a counting of Covid-19 such as :

> - [Data on people vaccinated against Covid-19](https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1/)

> - [Global Covid-19 data with deads and hospitalized](https://www.data.gouv.fr/en/datasets/chiffres-cles-concernant-lepidemie-de-covid19-en-france/)

We also used geometry data used for maps are from [France geoJSON](https://france-geojson.gregoiredavid.fr).

## Module structure


The main code can be found in  `./covidviz` folder.

There is a jupyter notebook which contains all our visualizations in the `./report` folder.

You can find a beamer presentation in the `./beamer` folder.

You can find a some examples of our visualizations in the `./temp` folder.

## Installation

### On Windows 

To install covidviz on Windows open you git manager (`git bash`, `git kraken` or others).

Then clone the following repository with this command :

    $ git clone https://github.com/jihene-b3/covidviz.git

After that, go on Anaconda prompt, go to the root of the covidviz project cloned and type :


    $ conda env create -f environment.yml 


## On Linux and MAC


To install covidviz on Linux go to your terminal and type :

    $ git clone https://github.com/jihene-b3/covidviz.git

Then go to the root of the covidviz project cloned and type :


    $ conda env create -f environment.yml 


## Documentation

The documentation of `covidviz` can be found here : [![Documentation Status](https://readthedocs.org/projects/covidviz/badge/?version=latest)](https://covidviz.readthedocs.io/en/latest/?badge=latest)


## Members
+ Jihène Belgaied : jihene.belgaied@etu.umontpellier.fr
+ Zakaria Laabsi : zakaria.laabsi@etu.umontpellier.fr
+ Chloé Serre-Combe : chloe.serre-combe@etu.umontpellier.fr
+ Stephani Ujka : stephani.ujka@etu.umontpellier.fr

## Tasks repartition 

+ Jihène : spatio-temporal covid19 evolution statistics
+ Zakaria : vaccine statistics and map on a dashboard 
+ Chloé : covid deaths and covid hospitalized widget maps, sparse, unit tests and CI
+ Stephani : icu and screening statistic 

+ Everyone : documentation, beamer, module architecture, time and memory efficiency...




