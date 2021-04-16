import reanimation.preprocess.load_data as rld
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import plotly.express as px

rld.deconfinement_1.drop(['deces', 'hospitalises', 'nouvelles_hospitalisations', 'nouvelles_reanimations', 'gueris'],1, inplace = True)

rld.deconfinement_1 = rld.deconfinement_1.set_index('date')
rld.deconfinement_1 = rld.deconfinement_1.sort_index()
rld.deconfinement_1 = rld.deconfinement_1.loc['2020-05-10':'2020-10-29']

rld.deconfinement_1.index = pd.to_datetime(rld.deconfinement_1.index)

rld.deconfinement_1 = rld.deconfinement_1.loc[rld.deconfinement_1['source_nom']=="Santé publique France Data",:]
rld.deconfinement_1.drop(['source_nom'],1, inplace = True)

DEP_code = pd.DataFrame(rld.deconfinement_1['maille_code'].unique())
for i in range(len(DEP_code)) :
    DEP_code.iat[i,0] = DEP_code.iat[i,0][4:]
DEP_code = DEP_code.loc[:,0].tolist()
DEP_name = pd.DataFrame(rld.deconfinement_1['maille_nom'].unique())
DEP_name = DEP_name.loc[:,0].tolist()
DEP = pd.concat([pd.DataFrame(DEP_code),pd.DataFrame(DEP_name)],1)
DEP = DEP.set_axis(['code', 'nom'], axis=1)
DEP = DEP.sort_values(by = 'code')
DEP = DEP.reset_index()
DEP = DEP.drop(['index'], 1)
DEP


def deconfinement_1_DEP_nom(department):
    x = pd.DataFrame(rld.deconfinement_1.loc[rld.deconfinement_1['maille_nom']==f"{department}",'reanimation']).resample("1D").sum()
    x = x.rename(columns = {"reanimation": f"{department}"})
    return(x)


def deconfinement_1_DEP_code(num_dep):
    x = pd.DataFrame(rld.deconfinement_1.loc[rld.deconfinement_1['maille_code']==f"DEP-{num_dep}",'reanimation']).resample("1D").sum()
    x = x.rename(columns = {"reanimation": f"{num_dep}"})
    return(x)


reanimations_deconfinement_1_code = pd.DataFrame()
for num_dep in DEP['code'].tolist() :
    reanimations_deconfinement_1_code = pd.concat([reanimations_deconfinement_1_code, deconfinement_1_DEP_code(f'{num_dep}')], axis = 1)


reanimations_deconfinement_1_code = reanimations_deconfinement_1_code.astype(int)
reanimations_deconfinement_1_code = reanimations_deconfinement_1_code.reset_index()

reanimations_deconfinement_1_nom = pd.DataFrame()
for nom_dep in DEP['nom'].tolist() :
    reanimations_deconfinement_1_nom = pd.concat([reanimations_deconfinement_1_nom, deconfinement_1_DEP_nom(f'{nom_dep}')], axis = 1)

reanimations_deconfinement_1_nom = reanimations_deconfinement_1_nom.astype(int)
reanimations_deconfinement_1_nom = reanimations_deconfinement_1_nom.reset_index()


def rea_deconf_FR(reanimations_deconfinement_1_nom):
    fig = px.line(reanimations_deconfinement_1_nom, x="date", y=reanimations_deconfinement_1_nom.columns,
              hover_data={"date": "|%B %d, %Y"},
              title='intensive care beds occupied during the 1st deconfinement in France by departments', height=500, width=800)
    fig.update_xaxes(
        dtick='M1',
        tickformat="%d\n%b")
    fig.add_vline(x='2020-07-20', line_color="red") #début du port du masque obligatoire
    return(fig.show())


reanimations_deconfinement_1_Bretagne = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom['Finistère'], reanimations_deconfinement_1_nom["Côtes-d'Armor"], reanimations_deconfinement_1_nom["Morbihan"], reanimations_deconfinement_1_nom["Ille-et-Vilaine"]], axis=1)

reanimations_deconfinement_1_Normandie = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom['Manche'], reanimations_deconfinement_1_nom["Calvados"], reanimations_deconfinement_1_nom["Eure"], reanimations_deconfinement_1_nom["Orne"], reanimations_deconfinement_1_nom["Seine-Maritime"]], axis=1)

reanimations_deconfinement_1_Pays_de_la_Loire = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom['Mayenne'], reanimations_deconfinement_1_nom["Sarthe"], reanimations_deconfinement_1_nom["Vendée"], reanimations_deconfinement_1_nom["Loire-Atlantique"], reanimations_deconfinement_1_nom["Maine-et-Loire"]], axis=1)

reanimations_deconfinement_1_Centre_Val_de_Loire = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom['Cher'], reanimations_deconfinement_1_nom["Eure-et-Loir"], reanimations_deconfinement_1_nom["Indre"], reanimations_deconfinement_1_nom["Indre-et-Loire"], reanimations_deconfinement_1_nom["Loir-et-Cher"], reanimations_deconfinement_1_nom["Loiret"]], axis=1)

reanimations_deconfinement_1_Bourgogne_Franche_Comte = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom["Côte-d'Or"], reanimations_deconfinement_1_nom["Doubs"], reanimations_deconfinement_1_nom["Jura"], reanimations_deconfinement_1_nom["Nièvre"], reanimations_deconfinement_1_nom["Haute-Saône"], reanimations_deconfinement_1_nom["Saône-et-Loire"], reanimations_deconfinement_1_nom["Yonne"]], axis=1)

reanimations_deconfinement_1_Grand_Est = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom["Ardennes"], reanimations_deconfinement_1_nom["Aube"], reanimations_deconfinement_1_nom["Marne"], reanimations_deconfinement_1_nom["Haute-Marne"], reanimations_deconfinement_1_nom["Meurthe-et-Moselle"], reanimations_deconfinement_1_nom["Meuse"], reanimations_deconfinement_1_nom["Moselle"], reanimations_deconfinement_1_nom["Bas-Rhin"], reanimations_deconfinement_1_nom["Haut-Rhin"], reanimations_deconfinement_1_nom["Vosges"]], axis=1)

reanimations_deconfinement_1_Hauts_de_France = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom["Aisne"], reanimations_deconfinement_1_nom["Nord"], reanimations_deconfinement_1_nom["Oise"], reanimations_deconfinement_1_nom["Pas-de-Calais"], reanimations_deconfinement_1_nom["Somme"]], axis=1)

reanimations_deconfinement_1_Ile_de_France = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom["Paris"], reanimations_deconfinement_1_nom["Seine-et-Marne"], reanimations_deconfinement_1_nom["Yvelines"], reanimations_deconfinement_1_nom["Essonne"], reanimations_deconfinement_1_nom["Hauts-de-Seine"], reanimations_deconfinement_1_nom["Seine-Saint-Denis"], reanimations_deconfinement_1_nom["Val-de-Marne"], reanimations_deconfinement_1_nom["Val-d'Oise"]], axis=1)

reanimations_deconfinement_1_Nouvelle_Aquitaine = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom["Charente"], reanimations_deconfinement_1_nom["Charente-Maritime"], reanimations_deconfinement_1_nom["Corrèze"], reanimations_deconfinement_1_nom["Creuse"], reanimations_deconfinement_1_nom["Dordogne"], reanimations_deconfinement_1_nom["Gironde"], reanimations_deconfinement_1_nom["Landes"], reanimations_deconfinement_1_nom["Lot-et-Garonne"], reanimations_deconfinement_1_nom["Pyrénées-Atlantiques"], reanimations_deconfinement_1_nom["Deux-Sèvres"], reanimations_deconfinement_1_nom["Vienne"], reanimations_deconfinement_1_nom["Haute-Vienne"]], axis=1)

reanimations_deconfinement_1_Auvergne_Rhone_Alpes = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom["Ain"], reanimations_deconfinement_1_nom["Allier"], reanimations_deconfinement_1_nom["Ardèche"], reanimations_deconfinement_1_nom["Cantal"], reanimations_deconfinement_1_nom["Drôme"], reanimations_deconfinement_1_nom["Isère"], reanimations_deconfinement_1_nom["Loire"], reanimations_deconfinement_1_nom["Haute-Loire"], reanimations_deconfinement_1_nom["Puy-de-Dôme"], reanimations_deconfinement_1_nom["Rhône"], reanimations_deconfinement_1_nom["Savoie"], reanimations_deconfinement_1_nom["Haute-Savoie"]], axis=1)

reanimations_deconfinement_1_Occitanie = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom["Ariège"], reanimations_deconfinement_1_nom["Aude"], reanimations_deconfinement_1_nom["Aveyron"], reanimations_deconfinement_1_nom["Gard"], reanimations_deconfinement_1_nom["Haute-Garonne"], reanimations_deconfinement_1_nom["Gers"], reanimations_deconfinement_1_nom["Hérault"], reanimations_deconfinement_1_nom["Lot"], reanimations_deconfinement_1_nom["Lozère"], reanimations_deconfinement_1_nom["Hautes-Pyrénées"], reanimations_deconfinement_1_nom["Pyrénées-Orientales"], reanimations_deconfinement_1_nom["Tarn"], reanimations_deconfinement_1_nom["Tarn-et-Garonne"]], axis=1)

reanimations_deconfinement_1_Provences_Alpes_Côte_Azur = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom["Alpes-de-Haute-Provence"], reanimations_deconfinement_1_nom["Hautes-Alpes"], reanimations_deconfinement_1_nom["Alpes-Maritimes"], reanimations_deconfinement_1_nom["Bouches-du-Rhône"], reanimations_deconfinement_1_nom["Var"], reanimations_deconfinement_1_nom["Vaucluse"]], axis=1)

reanimations_deconfinement_1_Corse = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom["Corse-du-Sud"], reanimations_deconfinement_1_nom["Haute-Corse"]], axis=1)

reanimations_deconfinement_1_Outre_Mer = pd.concat([reanimations_deconfinement_1_nom['date'], reanimations_deconfinement_1_nom["Guadeloupe"], reanimations_deconfinement_1_nom["Martinique"], reanimations_deconfinement_1_nom["Guyane"], reanimations_deconfinement_1_nom["La Réunion"], reanimations_deconfinement_1_nom["Mayotte"]], axis=1)

reanimation_deconfinement_1_regions = {}
reanimation_deconfinement_1_regions['Bretagne'] = reanimations_deconfinement_1_Bretagne
reanimation_deconfinement_1_regions['Normandie'] = reanimations_deconfinement_1_Normandie
reanimation_deconfinement_1_regions['Pays de la Loire'] = reanimations_deconfinement_1_Pays_de_la_Loire
reanimation_deconfinement_1_regions['Centre-Val-de-Loire'] = reanimations_deconfinement_1_Centre_Val_de_Loire
reanimation_deconfinement_1_regions['Bourgogne-Franche-Comté'] = reanimations_deconfinement_1_Bourgogne_Franche_Comte
reanimation_deconfinement_1_regions['Grand-Est'] = reanimations_deconfinement_1_Grand_Est
reanimation_deconfinement_1_regions['Hauts-de-France'] = reanimations_deconfinement_1_Hauts_de_France
reanimation_deconfinement_1_regions['Île-de-France'] = reanimations_deconfinement_1_Ile_de_France
reanimation_deconfinement_1_regions['Nouvelle-Aquitaine'] = reanimations_deconfinement_1_Nouvelle_Aquitaine
reanimation_deconfinement_1_regions['Auvergne-Rhône-Alpes'] = reanimations_deconfinement_1_Auvergne_Rhone_Alpes
reanimation_deconfinement_1_regions['Occitanie'] = reanimations_deconfinement_1_Occitanie
reanimation_deconfinement_1_regions["Provences-Alpes-Côte-d'Azur"] = reanimations_deconfinement_1_Provences_Alpes_Côte_Azur
reanimation_deconfinement_1_regions['Corse'] = reanimations_deconfinement_1_Corse
reanimation_deconfinement_1_regions["Régions d'Outre Mer"] = reanimations_deconfinement_1_Outre_Mer


def deconfinement_1_regions(region):
    fig = px.line(reanimation_deconfinement_1_regions[f'{region}'], x="date", y=reanimation_deconfinement_1_regions[f'{region}'].columns,
              title=f'intensive care beds occupied during the 1st deconfinement in {region}', height=500, width=800)
    fig.update_xaxes(
        dtick='M1',
        tickformat="%d\n%b")
    return(fig.show())
