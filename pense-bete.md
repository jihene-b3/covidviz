# DESCRIPTION DU PROJET COVID :

1ère carte (principal) : modélisation spatio-temporelle de la diffusion du coronavirus.

https://informatique-mia.inrae.fr/biosp/sites/informatique-mia.inra.fr.biosp-d7/files//field/image/spatio_temporal_covid.gif


Then you can produce various charts to illustrate how the covid19 affect population by age (e.g. a dashboard with various statistical features). 

## Dataset
https://www.data.gouv.fr/en/datasets/chiffres-cles-concernant-lepidemie-de-covid19-en-france/


# DESCRIPTION DES DONNÉES
## Noms des indicateurs (colonnes du tableau de données)
- date : année-mois-jour
- granularite : monde/pays/region/departement/collectivite-outremer
- maille_code : 
    - monde : WORLD
    - pays : FRA
    - region : REG-00
    - departement : DEP-00
    - collectivite-outremer : COM-000
- maille_nom :
    - monde : Monde
    - pays : France
    - region : Nouvelle-Aquitaine
    - departement : Charente
    - collectivite-outremer : Saint-Barthélemy
- cas_confirmes
- cas_ehpad
- cas_confirmes_ehpad
- cas_possibles_ehpad
- deces
- deces_ehpad
- reanimation
- hospitalises
- nouvelles_hospitalisations
- nouvelles_reanimations
- gueris,depistes
- source_nom
- source_url
- source_archive
- source_type

# IDÉE : 

On veut modéliser l'évolution du virus à travers le temps, jour par jour à partir du 1er janvier 2020 jusqu'à aujourd'hui, et l'espace sur une carte départementale de la France. Donc pour cette première carte, on créera un nouveau tableau de données à partir du fichier `covid.csv` en affichant seulement les indicateurs `date`, `granularite`, `maille_code`,`maille_nom` et `cas_confirmes`, et en filtrant `granularite = departement`. Il s'agira du fichier `covid_map1.csv`.

## PACKAGES UTILES :
