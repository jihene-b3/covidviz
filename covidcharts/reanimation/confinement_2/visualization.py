import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import plotly.express as px
import reanimation.preprocess.load_data as rld

rld.confinement_2.drop(['deces', 'hospitalises', 'nouvelles_hospitalisations', 'nouvelles_reanimations', 'gueris'],1, inplace = True)

rld.confinement_2 = rld.confinement_2.set_index('date')
rld.confinement_2 = rld.confinement_2.sort_index()
rld.confinement_2 = rld.confinement_2.loc['2020-10-30':'2020-12-14']

rld.confinement_2.index = pd.to_datetime(rld.confinement_2.index)

rld.confinement_2 = rld.confinement_2.loc[rld.confinement_2['source_nom']=="Santé publique France Data",:]
rld.confinement_2.drop(['source_nom'],1, inplace = True)

DEP_code = pd.DataFrame(rld.confinement_2['maille_code'].unique())
for i in range(len(DEP_code)) :
    DEP_code.iat[i,0] = DEP_code.iat[i,0][4:]
DEP_code = DEP_code.loc[:,0].tolist()
DEP_name = pd.DataFrame(rld.confinement_2['maille_nom'].unique())
DEP_name = DEP_name.loc[:,0].tolist()
DEP = pd.concat([pd.DataFrame(DEP_code),pd.DataFrame(DEP_name)],1)
DEP = DEP.set_axis(['code', 'nom'], axis=1)
DEP = DEP.sort_values(by = 'code')
DEP = DEP.reset_index()
DEP = DEP.drop(['index'], 1)


def confinement_2_DEP_nom(department):
    x = pd.DataFrame(rld.confinement_2.loc[rld.confinement_2['maille_nom']==f"{department}",'reanimation']).resample("1D").sum()
    x = x.rename(columns = {"reanimation": f"{department}"})
    return(x)


def confinement_2_DEP_code(num_dep):
    x = pd.DataFrame(rld.confinement_2.loc[rld.confinement_2['maille_code']==f"DEP-{num_dep}",'reanimation']).resample("1D").sum()
    x = x.rename(columns = {"reanimation": f"{num_dep}"})
    return(x)


reanimations_confinement_2_code = pd.DataFrame()
for num_dep in DEP['code'].tolist() :
    reanimations_confinement_2_code = pd.concat([reanimations_confinement_2_code, confinement_2_DEP_code(f'{num_dep}')], axis = 1)


reanimations_confinement_2_code = reanimations_confinement_2_code.astype(int)
reanimations_confinement_2_code = reanimations_confinement_2_code.reset_index()

reanimations_confinement_2_nom = pd.DataFrame()
for nom_dep in DEP['nom'].tolist() :
    reanimations_confinement_2_nom = pd.concat([reanimations_confinement_2_nom, confinement_2_DEP_nom(f'{nom_dep}')], axis = 1)

reanimations_confinement_2_nom = reanimations_confinement_2_nom.astype(int)
reanimations_confinement_2_nom = reanimations_confinement_2_nom.reset_index()


def rea_conf2_FR(reanimations_confinement_2_nom):
    fig = px.line(reanimations_confinement_2_nom, x="date", y=reanimations_confinement_2_nom.columns,
              hover_data={"date": "|%B %d, %Y"},
              title='intensive care beds occupied during the 2nd confinement in France by departments', height=500, width=800)
    fig.update_xaxes(
    dtick='M1',
    tickformat="%d\n%b")
    return(fig.show())

reanimations_confinement_2_Bretagne = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom['Finistère'], reanimations_confinement_2_nom["Côtes-d'Armor"], reanimations_confinement_2_nom["Morbihan"], reanimations_confinement_2_nom["Ille-et-Vilaine"]], axis=1)

reanimations_confinement_2_Normandie = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom['Manche'], reanimations_confinement_2_nom["Calvados"], reanimations_confinement_2_nom["Eure"], reanimations_confinement_2_nom["Orne"], reanimations_confinement_2_nom["Seine-Maritime"]], axis=1)

reanimations_confinement_2_Pays_de_la_Loire = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom['Mayenne'], reanimations_confinement_2_nom["Sarthe"], reanimations_confinement_2_nom["Vendée"], reanimations_confinement_2_nom["Loire-Atlantique"], reanimations_confinement_2_nom["Maine-et-Loire"]], axis=1)

reanimations_confinement_2_Centre_Val_de_Loire = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom['Cher'], reanimations_confinement_2_nom["Eure-et-Loir"], reanimations_confinement_2_nom["Indre"], reanimations_confinement_2_nom["Indre-et-Loire"], reanimations_confinement_2_nom["Loir-et-Cher"], reanimations_confinement_2_nom["Loiret"]], axis=1)

reanimations_confinement_2_Bourgogne_Franche_Comte = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom["Côte-d'Or"], reanimations_confinement_2_nom["Doubs"], reanimations_confinement_2_nom["Jura"], reanimations_confinement_2_nom["Nièvre"], reanimations_confinement_2_nom["Haute-Saône"], reanimations_confinement_2_nom["Saône-et-Loire"], reanimations_confinement_2_nom["Yonne"]], axis=1)

reanimations_confinement_2_Grand_Est = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom["Ardennes"], reanimations_confinement_2_nom["Aube"], reanimations_confinement_2_nom["Marne"], reanimations_confinement_2_nom["Haute-Marne"], reanimations_confinement_2_nom["Meurthe-et-Moselle"], reanimations_confinement_2_nom["Meuse"], reanimations_confinement_2_nom["Moselle"], reanimations_confinement_2_nom["Bas-Rhin"], reanimations_confinement_2_nom["Haut-Rhin"], reanimations_confinement_2_nom["Vosges"]], axis=1)

reanimations_confinement_2_Hauts_de_France = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom["Aisne"], reanimations_confinement_2_nom["Nord"], reanimations_confinement_2_nom["Oise"], reanimations_confinement_2_nom["Pas-de-Calais"], reanimations_confinement_2_nom["Somme"]], axis=1)

reanimations_confinement_2_Ile_de_France = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom["Paris"], reanimations_confinement_2_nom["Seine-et-Marne"], reanimations_confinement_2_nom["Yvelines"], reanimations_confinement_2_nom["Essonne"], reanimations_confinement_2_nom["Hauts-de-Seine"], reanimations_confinement_2_nom["Seine-Saint-Denis"], reanimations_confinement_2_nom["Val-de-Marne"], reanimations_confinement_2_nom["Val-d'Oise"]], axis=1)

reanimations_confinement_2_Nouvelle_Aquitaine = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom["Charente"], reanimations_confinement_2_nom["Charente-Maritime"], reanimations_confinement_2_nom["Corrèze"], reanimations_confinement_2_nom["Creuse"], reanimations_confinement_2_nom["Dordogne"], reanimations_confinement_2_nom["Gironde"], reanimations_confinement_2_nom["Landes"], reanimations_confinement_2_nom["Lot-et-Garonne"], reanimations_confinement_2_nom["Pyrénées-Atlantiques"], reanimations_confinement_2_nom["Deux-Sèvres"], reanimations_confinement_2_nom["Vienne"], reanimations_confinement_2_nom["Haute-Vienne"]], axis=1)

reanimations_confinement_2_Auvergne_Rhone_Alpes = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom["Ain"], reanimations_confinement_2_nom["Allier"], reanimations_confinement_2_nom["Ardèche"], reanimations_confinement_2_nom["Cantal"], reanimations_confinement_2_nom["Drôme"], reanimations_confinement_2_nom["Isère"], reanimations_confinement_2_nom["Loire"], reanimations_confinement_2_nom["Haute-Loire"], reanimations_confinement_2_nom["Puy-de-Dôme"], reanimations_confinement_2_nom["Rhône"], reanimations_confinement_2_nom["Savoie"], reanimations_confinement_2_nom["Haute-Savoie"]], axis=1)

reanimations_confinement_2_Occitanie = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom["Ariège"], reanimations_confinement_2_nom["Aude"], reanimations_confinement_2_nom["Aveyron"], reanimations_confinement_2_nom["Gard"], reanimations_confinement_2_nom["Haute-Garonne"], reanimations_confinement_2_nom["Gers"], reanimations_confinement_2_nom["Hérault"], reanimations_confinement_2_nom["Lot"], reanimations_confinement_2_nom["Lozère"], reanimations_confinement_2_nom["Hautes-Pyrénées"], reanimations_confinement_2_nom["Pyrénées-Orientales"], reanimations_confinement_2_nom["Tarn"], reanimations_confinement_2_nom["Tarn-et-Garonne"]], axis=1)

reanimations_confinement_2_Provences_Alpes_Côte_Azur = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom["Alpes-de-Haute-Provence"], reanimations_confinement_2_nom["Hautes-Alpes"], reanimations_confinement_2_nom["Alpes-Maritimes"], reanimations_confinement_2_nom["Bouches-du-Rhône"], reanimations_confinement_2_nom["Var"], reanimations_confinement_2_nom["Vaucluse"]], axis=1)

reanimations_confinement_2_Corse = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom["Corse-du-Sud"], reanimations_confinement_2_nom["Haute-Corse"]], axis=1)

reanimations_confinement_2_Outre_Mer = pd.concat([reanimations_confinement_2_nom['date'], reanimations_confinement_2_nom["Guadeloupe"], reanimations_confinement_2_nom["Martinique"], reanimations_confinement_2_nom["Guyane"], reanimations_confinement_2_nom["La Réunion"], reanimations_confinement_2_nom["Mayotte"]], axis=1)

reanimation_confinement_2_regions = {}
reanimation_confinement_2_regions['Bretagne'] = reanimations_confinement_2_Bretagne
reanimation_confinement_2_regions['Normandie'] = reanimations_confinement_2_Normandie
reanimation_confinement_2_regions['Pays de la Loire'] = reanimations_confinement_2_Pays_de_la_Loire
reanimation_confinement_2_regions['Centre-Val-de-Loire'] = reanimations_confinement_2_Centre_Val_de_Loire
reanimation_confinement_2_regions['Bourgogne-Franche-Comté'] = reanimations_confinement_2_Bourgogne_Franche_Comte
reanimation_confinement_2_regions['Grand-Est'] = reanimations_confinement_2_Grand_Est
reanimation_confinement_2_regions['Hauts-de-France'] = reanimations_confinement_2_Hauts_de_France
reanimation_confinement_2_regions['Île-de-France'] = reanimations_confinement_2_Ile_de_France
reanimation_confinement_2_regions['Nouvelle-Aquitaine'] = reanimations_confinement_2_Nouvelle_Aquitaine
reanimation_confinement_2_regions['Auvergne-Rhône-Alpes'] = reanimations_confinement_2_Auvergne_Rhone_Alpes
reanimation_confinement_2_regions['Occitanie'] = reanimations_confinement_2_Occitanie
reanimation_confinement_2_regions["Provences-Alpes-Côte-d'Azur"] = reanimations_confinement_2_Provences_Alpes_Côte_Azur
reanimation_confinement_2_regions['Corse'] = reanimations_confinement_2_Corse
reanimation_confinement_2_regions["Régions d'Outre Mer"] = reanimations_confinement_2_Outre_Mer

def confinement_2_regions(region) :
    fig = px.line(reanimation_confinement_2_regions[f'{region}'], x="date", y=reanimation_confinement_2_regions[f'{region}'].columns,
              title=f'intensive care beds occupied during the 2nd confinement in {region}', height=500, width=800)
    fig.update_xaxes(
        dtick='M1',
        tickformat="%d\n%b")
    return(fig.show())