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
- cas_confirmes : total cumulé des cas testés positivement au test RT-PCR ou antigénique
- cas_ehpad
- cas_confirmes_ehpad
- cas_possibles_ehpad : toute personne (ici provenant d'ehpad) présentant des symptômes.
- deces (par jour)
- deces_ehpad
- reanimation (cumul - sorties de reanimation, au total)
- hospitalises (cumul - sorties, au total)
- nouvelles_hospitalisations (jour)
- nouvelles_reanimations (jour)
- gueris (cumul)
- depistes : sur un dataframe (départements) de 38594 lignes, il y a seulement 6 données numériques (le reste est `nan`). On n'utilisera donc pas cette colonne non plus.
- source_nom
- source_url
- source_archive
- source_type

Remarque : pour les départements, il n'y a pas de données concernant la propagation du virus dans les ehpad. On supprimera donc ces colonnes. De même pour la colonne cas_confirmes, il y a seulement 4% de données numériques (1649/38694).

Donc les indicateurs à prendre en compte dans notre dataframe seront : `deces`, `reanimation`, `hospitalises`, `nouvelles_hospitalisations`, 
`nouvelles_reanimations`, `gueris`.

# IDÉE : 

On veut modéliser l'évolution du virus à travers le temps, jour par jour à partir du 1er janvier 2020 jusqu'à aujourd'hui, et l'espace sur une carte départementale de la France. Donc pour cette première carte, on créera un nouveau tableau de données à partir du fichier `covid.csv` en affichant seulement certains indicateurs `date`, `granularite`, `maille_code`,`maille_nom` et `cas_confirmes`, et en filtrant `granularite = departement` .


## PACKAGES UTILES :
