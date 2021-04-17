import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import plotly.express as px
import reanimation.preprocess.load_data as rld

rld.curfew.drop(['deces', 'hospitalises', 'nouvelles_hospitalisations', 'nouvelles_reanimations', 'gueris'],1, inplace = True)

rld.curfew = rld.curfew.set_index('date')
rld.curfew = rld.curfew.sort_index()
rld.curfew = rld.curfew.loc['2020-12-15':]

rld.curfew.index = pd.to_datetime(rld.curfew.index)

rld.curfew = rld.curfew.loc[rld.curfew['source_nom']=="Santé publique France Data",:]
rld.curfew.drop(['source_nom'],1, inplace = True)

DEP_code = pd.DataFrame(rld.curfew['maille_code'].unique())
for i in range(len(DEP_code)) :
    DEP_code.iat[i,0] = DEP_code.iat[i,0][4:]
DEP_code = DEP_code.loc[:,0].tolist()
DEP_name = pd.DataFrame(rld.curfew['maille_nom'].unique())
DEP_name = DEP_name.loc[:,0].tolist()
DEP = pd.concat([pd.DataFrame(DEP_code),pd.DataFrame(DEP_name)],1)
DEP = DEP.set_axis(['code', 'nom'], axis=1)
DEP = DEP.sort_values(by = 'code')
DEP = DEP.reset_index()
DEP = DEP.drop(['index'], 1)


def curfew_DEP_nom(department):
    x = pd.DataFrame(rld.curfew.loc[rld.curfew['maille_nom']==f"{department}",'reanimation']).resample("1D").sum()
    x = x.rename(columns = {"reanimation": f"{department}"})
    return(x)


def curfew_DEP_code(num_dep):
    x = pd.DataFrame(rld.curfew.loc[rld.curfew['maille_code']==f"DEP-{num_dep}",'reanimation']).resample("1D").sum()
    x = x.rename(columns = {"reanimation": f"{num_dep}"})
    return(x)


reanimations_curfew_code = pd.DataFrame()
for num_dep in DEP['code'].tolist() :
    reanimations_curfew_code = pd.concat([reanimations_curfew_code, curfew_DEP_code(f'{num_dep}')], axis = 1)

reanimations_curfew_code = reanimations_curfew_code.astype(int)
reanimations_curfew_code = reanimations_curfew_code.reset_index()


reanimations_curfew_nom = pd.DataFrame()
for nom_dep in DEP['nom'].tolist() :
    reanimations_curfew_nom = pd.concat([reanimations_curfew_nom, curfew_DEP_nom(f'{nom_dep}')], axis = 1)

reanimations_curfew_nom = reanimations_curfew_nom.astype(int)
reanimations_curfew_nom = reanimations_curfew_nom.reset_index()


def rea_curfew_FR(reanimations_curfew_nom):
    fig = px.line(reanimations_curfew_nom, x="date", y=reanimations_curfew_nom.columns,
        hover_data={"date": "|%B %d, %Y"},
        title='intensive care beds occupied during the curfew in France by departments', height=500, width=800)
    fig.update_xaxes(
    dtick='M1',
    tickformat="%d\n%b")
    return(fig.show())


reanimations_curfew_Bretagne = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom['Finistère'], reanimations_curfew_nom["Côtes-d'Armor"], reanimations_curfew_nom["Morbihan"], reanimations_curfew_nom["Ille-et-Vilaine"]], axis=1)

reanimations_curfew_Normandie = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom['Manche'], reanimations_curfew_nom["Calvados"], reanimations_curfew_nom["Eure"], reanimations_curfew_nom["Orne"], reanimations_curfew_nom["Seine-Maritime"]], axis=1)

reanimations_curfew_Pays_de_la_Loire = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom['Mayenne'], reanimations_curfew_nom["Sarthe"], reanimations_curfew_nom["Vendée"], reanimations_curfew_nom["Loire-Atlantique"], reanimations_curfew_nom["Maine-et-Loire"]], axis=1)

reanimations_curfew_Centre_Val_de_Loire = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom['Cher'], reanimations_curfew_nom["Eure-et-Loir"], reanimations_curfew_nom["Indre"], reanimations_curfew_nom["Indre-et-Loire"], reanimations_curfew_nom["Loir-et-Cher"], reanimations_curfew_nom["Loiret"]], axis=1)

reanimations_curfew_Bourgogne_Franche_Comte = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom["Côte-d'Or"], reanimations_curfew_nom["Doubs"], reanimations_curfew_nom["Jura"], reanimations_curfew_nom["Nièvre"], reanimations_curfew_nom["Haute-Saône"], reanimations_curfew_nom["Saône-et-Loire"], reanimations_curfew_nom["Yonne"]], axis=1)

reanimations_curfew_Grand_Est = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom["Ardennes"], reanimations_curfew_nom["Aube"], reanimations_curfew_nom["Marne"], reanimations_curfew_nom["Haute-Marne"], reanimations_curfew_nom["Meurthe-et-Moselle"], reanimations_curfew_nom["Meuse"], reanimations_curfew_nom["Moselle"], reanimations_curfew_nom["Bas-Rhin"], reanimations_curfew_nom["Haut-Rhin"], reanimations_curfew_nom["Vosges"]], axis=1)

reanimations_curfew_Hauts_de_France = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom["Aisne"], reanimations_curfew_nom["Nord"], reanimations_curfew_nom["Oise"], reanimations_curfew_nom["Pas-de-Calais"], reanimations_curfew_nom["Somme"]], axis=1)

reanimations_curfew_Ile_de_France = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom["Paris"], reanimations_curfew_nom["Seine-et-Marne"], reanimations_curfew_nom["Yvelines"], reanimations_curfew_nom["Essonne"], reanimations_curfew_nom["Hauts-de-Seine"], reanimations_curfew_nom["Seine-Saint-Denis"], reanimations_curfew_nom["Val-de-Marne"], reanimations_curfew_nom["Val-d'Oise"]], axis=1)

reanimations_curfew_Nouvelle_Aquitaine = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom["Charente"], reanimations_curfew_nom["Charente-Maritime"], reanimations_curfew_nom["Corrèze"], reanimations_curfew_nom["Creuse"], reanimations_curfew_nom["Dordogne"], reanimations_curfew_nom["Gironde"], reanimations_curfew_nom["Landes"], reanimations_curfew_nom["Lot-et-Garonne"], reanimations_curfew_nom["Pyrénées-Atlantiques"], reanimations_curfew_nom["Deux-Sèvres"], reanimations_curfew_nom["Vienne"], reanimations_curfew_nom["Haute-Vienne"]], axis=1)

reanimations_curfew_Auvergne_Rhone_Alpes = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom["Ain"], reanimations_curfew_nom["Allier"], reanimations_curfew_nom["Ardèche"], reanimations_curfew_nom["Cantal"], reanimations_curfew_nom["Drôme"], reanimations_curfew_nom["Isère"], reanimations_curfew_nom["Loire"], reanimations_curfew_nom["Haute-Loire"], reanimations_curfew_nom["Puy-de-Dôme"], reanimations_curfew_nom["Rhône"], reanimations_curfew_nom["Savoie"], reanimations_curfew_nom["Haute-Savoie"]], axis=1)

reanimations_curfew_Occitanie = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom["Ariège"], reanimations_curfew_nom["Aude"], reanimations_curfew_nom["Aveyron"], reanimations_curfew_nom["Gard"], reanimations_curfew_nom["Haute-Garonne"], reanimations_curfew_nom["Gers"], reanimations_curfew_nom["Hérault"], reanimations_curfew_nom["Lot"], reanimations_curfew_nom["Lozère"], reanimations_curfew_nom["Hautes-Pyrénées"], reanimations_curfew_nom["Pyrénées-Orientales"], reanimations_curfew_nom["Tarn"], reanimations_curfew_nom["Tarn-et-Garonne"]], axis=1)

reanimations_curfew_Provences_Alpes_Côte_Azur = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom["Alpes-de-Haute-Provence"], reanimations_curfew_nom["Hautes-Alpes"], reanimations_curfew_nom["Alpes-Maritimes"], reanimations_curfew_nom["Bouches-du-Rhône"], reanimations_curfew_nom["Var"], reanimations_curfew_nom["Vaucluse"]], axis=1)

reanimations_curfew_Corse = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom["Corse-du-Sud"], reanimations_curfew_nom["Haute-Corse"]], axis=1)

reanimations_curfew_Outre_Mer = pd.concat([reanimations_curfew_nom['date'], reanimations_curfew_nom["Guadeloupe"], reanimations_curfew_nom["Martinique"], reanimations_curfew_nom["Guyane"], reanimations_curfew_nom["La Réunion"], reanimations_curfew_nom["Mayotte"]], axis=1)

reanimation_curfew_regions = {}
reanimation_curfew_regions['Bretagne'] = reanimations_curfew_Bretagne
reanimation_curfew_regions['Normandie'] = reanimations_curfew_Normandie
reanimation_curfew_regions['Pays de la Loire'] = reanimations_curfew_Pays_de_la_Loire
reanimation_curfew_regions['Centre-Val-de-Loire'] = reanimations_curfew_Centre_Val_de_Loire
reanimation_curfew_regions['Bourgogne-Franche-Comté'] = reanimations_curfew_Bourgogne_Franche_Comte
reanimation_curfew_regions['Grand-Est'] = reanimations_curfew_Grand_Est
reanimation_curfew_regions['Hauts-de-France'] = reanimations_curfew_Hauts_de_France
reanimation_curfew_regions['Île-de-France'] = reanimations_curfew_Ile_de_France
reanimation_curfew_regions['Nouvelle-Aquitaine'] = reanimations_curfew_Nouvelle_Aquitaine
reanimation_curfew_regions['Auvergne-Rhône-Alpes'] = reanimations_curfew_Auvergne_Rhone_Alpes
reanimation_curfew_regions['Occitanie'] = reanimations_curfew_Occitanie
reanimation_curfew_regions["Provences-Alpes-Côte-d'Azur"] = reanimations_curfew_Provences_Alpes_Côte_Azur
reanimation_curfew_regions['Corse'] = reanimations_curfew_Corse
reanimation_curfew_regions["Régions d'Outre Mer"] = reanimations_curfew_Outre_Mer


def curfew_regions(region) :
    fig = px.line(reanimation_curfew_regions[f'{region}'], x="date", y=reanimation_curfew_regions[f'{region}'].columns,
              title=f'intensive care beds occupied during the curfew in {region}', height=500, width=800)
    fig.update_xaxes(
        dtick='M1',
        tickformat="%d\n%b")
    return(fig.show())