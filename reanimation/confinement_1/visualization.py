import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import ipympl
import plotly.express as px
import reanimation.preprocess.load_data as rld

rld.confinement_1 = rld.confinement_1.drop(
    ['deces', 'hospitalises', 'nouvelles_hospitalisations',
     'nouvelles_reanimations', 'gueris'], 1)

rld.confinement_1 = rld.confinement_1.set_index('date')
rld.confinement_1 = rld.confinement_1.sort_index()
rld.confinement_1 = rld.confinement_1.loc['2020-03-17':'2020-05-10']

rld.confinement_1.index = pd.to_datetime(rld.confinement_1.index)

rld.confinement_1 = rld.confinement_1.loc[rld.confinement_1['source_nom'] == "Santé publique France Data",:]
rld.confinement_1.drop(['source_nom'], 1, inplace=True)

DEP_code = pd.DataFrame(rld.confinement_1['maille_code'].unique())

for i in range(len(DEP_code)) :
    DEP_code.iat[i,0] = DEP_code.iat[i,0][4:]

DEP_code = DEP_code.loc[:,0].tolist()
DEP_name = pd.DataFrame(rld.confinement_1['maille_nom'].unique())
DEP_name = DEP_name.loc[:,0].tolist()
DEP = pd.concat([pd.DataFrame(DEP_code), pd.DataFrame(DEP_name)],1)
DEP = DEP.set_axis(['code', 'nom'], axis=1)
DEP = DEP.sort_values(by='code')
DEP = DEP.reset_index()
DEP = DEP.drop(['index'], 1)


def confinement_1_DEP_nom(department):
    x = pd.DataFrame(rld.confinement_1.loc[rld.confinement_1['maille_nom']==f"{department}",
     'reanimation']).resample("1D").sum()
    x = x.rename(columns={"reanimation": f"{department}"})
    return(x)


def confinement_1_DEP_code(num_dep):
    x = pd.DataFrame(rld.confinement_1.loc[rld.confinement_1['maille_code']==f"DEP-{num_dep}",
    'reanimation']).resample("1D").sum()
    x = x.rename(columns={"reanimation": f"{num_dep}"})
    return(x)


reanimations_confinement_1_code = pd.DataFrame()
for num_dep in DEP['code'].tolist():
    reanimations_confinement_1_code = pd.concat([
        reanimations_confinement_1_code, 
        confinement_1_DEP_code(f'{num_dep}')], axis=1)

reanimations_confinement_1_code = reanimations_confinement_1_code.astype(int)
reanimations_confinement_1_code = reanimations_confinement_1_code.reset_index()

reanimations_confinement_1_nom = pd.DataFrame()
for nom_dep in DEP['nom'].tolist():
    reanimations_confinement_1_nom = pd.concat([reanimations_confinement_1_nom, 
    confinement_1_DEP_nom(f'{nom_dep}')], axis=1)

reanimations_confinement_1_nom = reanimations_confinement_1_nom.astype(int)
reanimations_confinement_1_nom = reanimations_confinement_1_nom.reset_index()


def rea_conf1_FR(reanimations_confinement_1_nom):
    fig = px.line(reanimations_confinement_1_nom, x="date", 
        y=reanimations_confinement_1_nom.columns,
        hover_data={"date": "|%B %d, %Y"},
        title='intensive care beds occupied during the 1st confinement in France by departments', 
        height=500, width=800)
    fig.update_xaxes(
        dtick='M1',
        tickformat="%d\n%b")
    return(fig.show())


reanimations_confinement_1_Bretagne = pd.concat([
    reanimations_confinement_1_nom['date'],
    reanimations_confinement_1_nom['Finistère'], 
    reanimations_confinement_1_nom["Côtes-d'Armor"], 
    reanimations_confinement_1_nom["Morbihan"], 
    reanimations_confinement_1_nom["Ille-et-Vilaine"]], axis=1)

reanimations_confinement_1_Normandie = pd.concat([
    reanimations_confinement_1_nom['date'], 
    reanimations_confinement_1_nom['Manche'], 
    reanimations_confinement_1_nom["Calvados"], 
    reanimations_confinement_1_nom["Eure"], 
    reanimations_confinement_1_nom["Orne"], 
    reanimations_confinement_1_nom["Seine-Maritime"]], axis=1)

reanimations_confinement_1_Pays_de_la_Loire = pd.concat([
    reanimations_confinement_1_nom['date'], 
    reanimations_confinement_1_nom['Mayenne'], 
    reanimations_confinement_1_nom["Sarthe"], 
    reanimations_confinement_1_nom["Vendée"], 
    reanimations_confinement_1_nom["Loire-Atlantique"], 
    reanimations_confinement_1_nom["Maine-et-Loire"]], axis=1)

reanimations_confinement_1_Centre_Val_de_Loire = pd.concat([
    reanimations_confinement_1_nom['date'], 
    reanimations_confinement_1_nom['Cher'], 
    reanimations_confinement_1_nom["Eure-et-Loir"], 
    reanimations_confinement_1_nom["Indre"], 
    reanimations_confinement_1_nom["Indre-et-Loire"], 
    reanimations_confinement_1_nom["Loir-et-Cher"], 
    reanimations_confinement_1_nom["Loiret"]], axis=1)

reanimations_confinement_1_Bourgogne_Franche_Comte = pd.concat([
    reanimations_confinement_1_nom['date'], 
    reanimations_confinement_1_nom["Côte-d'Or"], 
    reanimations_confinement_1_nom["Doubs"], 
    reanimations_confinement_1_nom["Jura"], 
    reanimations_confinement_1_nom["Nièvre"], 
    reanimations_confinement_1_nom["Haute-Saône"], 
    reanimations_confinement_1_nom["Saône-et-Loire"], 
    reanimations_confinement_1_nom["Yonne"]], axis=1)

reanimations_confinement_1_Grand_Est = pd.concat([
    reanimations_confinement_1_nom['date'], 
    reanimations_confinement_1_nom["Ardennes"], 
    reanimations_confinement_1_nom["Aube"], 
    reanimations_confinement_1_nom["Marne"], 
    reanimations_confinement_1_nom["Haute-Marne"], 
    reanimations_confinement_1_nom["Meurthe-et-Moselle"], 
    reanimations_confinement_1_nom["Meuse"], 
    reanimations_confinement_1_nom["Moselle"], 
    reanimations_confinement_1_nom["Bas-Rhin"], 
    reanimations_confinement_1_nom["Haut-Rhin"], 
    reanimations_confinement_1_nom["Vosges"]], axis=1)

reanimations_confinement_1_Hauts_de_France = pd.concat([
    reanimations_confinement_1_nom['date'], 
    reanimations_confinement_1_nom["Aisne"], 
    reanimations_confinement_1_nom["Nord"], 
    reanimations_confinement_1_nom["Oise"], 
    reanimations_confinement_1_nom["Pas-de-Calais"], 
    reanimations_confinement_1_nom["Somme"]], axis=1)

reanimations_confinement_1_Ile_de_France = pd.concat([
    reanimations_confinement_1_nom['date'], 
    reanimations_confinement_1_nom["Paris"], 
    reanimations_confinement_1_nom["Seine-et-Marne"], 
    reanimations_confinement_1_nom["Yvelines"], 
    reanimations_confinement_1_nom["Essonne"], 
    reanimations_confinement_1_nom["Hauts-de-Seine"], 
    reanimations_confinement_1_nom["Seine-Saint-Denis"], 
    reanimations_confinement_1_nom["Val-de-Marne"], 
    reanimations_confinement_1_nom["Val-d'Oise"]], axis=1)

reanimations_confinement_1_Nouvelle_Aquitaine = pd.concat([
    reanimations_confinement_1_nom['date'], 
    reanimations_confinement_1_nom["Charente"], 
    reanimations_confinement_1_nom["Charente-Maritime"], 
    reanimations_confinement_1_nom["Corrèze"], 
    reanimations_confinement_1_nom["Creuse"], 
    reanimations_confinement_1_nom["Dordogne"], 
    reanimations_confinement_1_nom["Gironde"], 
    reanimations_confinement_1_nom["Landes"], 
    reanimations_confinement_1_nom["Lot-et-Garonne"], 
    reanimations_confinement_1_nom["Pyrénées-Atlantiques"], 
    reanimations_confinement_1_nom["Deux-Sèvres"], 
    reanimations_confinement_1_nom["Vienne"], 
    reanimations_confinement_1_nom["Haute-Vienne"]], axis=1)

reanimations_confinement_1_Auvergne_Rhone_Alpes = pd.concat([
    reanimations_confinement_1_nom['date'], 
    reanimations_confinement_1_nom["Ain"], 
    reanimations_confinement_1_nom["Allier"], 
    reanimations_confinement_1_nom["Ardèche"], 
    reanimations_confinement_1_nom["Cantal"], 
    reanimations_confinement_1_nom["Drôme"], 
    reanimations_confinement_1_nom["Isère"], 
    reanimations_confinement_1_nom["Loire"], 
    reanimations_confinement_1_nom["Haute-Loire"], 
    reanimations_confinement_1_nom["Puy-de-Dôme"], 
    reanimations_confinement_1_nom["Rhône"], 
    reanimations_confinement_1_nom["Savoie"], 
    reanimations_confinement_1_nom["Haute-Savoie"]], axis=1)

reanimations_confinement_1_Occitanie = pd.concat([
    reanimations_confinement_1_nom['date'], 
    reanimations_confinement_1_nom["Ariège"], 
    reanimations_confinement_1_nom["Aude"], 
    reanimations_confinement_1_nom["Aveyron"], 
    reanimations_confinement_1_nom["Gard"], 
    reanimations_confinement_1_nom["Haute-Garonne"], 
    reanimations_confinement_1_nom["Gers"], 
    reanimations_confinement_1_nom["Hérault"], 
    reanimations_confinement_1_nom["Lot"], 
    reanimations_confinement_1_nom["Lozère"], 
    reanimations_confinement_1_nom["Hautes-Pyrénées"], 
    reanimations_confinement_1_nom["Pyrénées-Orientales"], 
    reanimations_confinement_1_nom["Tarn"], 
    reanimations_confinement_1_nom["Tarn-et-Garonne"]], axis=1)

reanimations_confinement_1_Provences_Alpes_Côte_Azur = pd.concat([
    reanimations_confinement_1_nom['date'], 
    reanimations_confinement_1_nom["Alpes-de-Haute-Provence"], 
    reanimations_confinement_1_nom["Hautes-Alpes"], 
    reanimations_confinement_1_nom["Alpes-Maritimes"], 
    reanimations_confinement_1_nom["Bouches-du-Rhône"], 
    reanimations_confinement_1_nom["Var"], 
    reanimations_confinement_1_nom["Vaucluse"]], axis=1)

reanimations_confinement_1_Corse = pd.concat([
    reanimations_confinement_1_nom['date'], 
    reanimations_confinement_1_nom["Corse-du-Sud"], 
    reanimations_confinement_1_nom["Haute-Corse"]], axis=1)

reanimations_confinement_1_Outre_Mer = pd.concat([
    reanimations_confinement_1_nom['date'], 
    reanimations_confinement_1_nom["Guadeloupe"], 
    reanimations_confinement_1_nom["Martinique"], 
    reanimations_confinement_1_nom["Guyane"], 
    reanimations_confinement_1_nom["La Réunion"], 
    reanimations_confinement_1_nom["Mayotte"]], axis=1)

reanimation_confinement_1_regions = {}
reanimation_confinement_1_regions['Bretagne'] = reanimations_confinement_1_Bretagne
reanimation_confinement_1_regions['Normandie'] = reanimations_confinement_1_Normandie
reanimation_confinement_1_regions['Pays de la Loire'] = reanimations_confinement_1_Pays_de_la_Loire
reanimation_confinement_1_regions['Centre-Val-de-Loire'] = reanimations_confinement_1_Centre_Val_de_Loire
reanimation_confinement_1_regions['Bourgogne-Franche-Comté'] = reanimations_confinement_1_Bourgogne_Franche_Comte
reanimation_confinement_1_regions['Grand-Est'] = reanimations_confinement_1_Grand_Est
reanimation_confinement_1_regions['Hauts-de-France'] = reanimations_confinement_1_Hauts_de_France
reanimation_confinement_1_regions['Île-de-France'] = reanimations_confinement_1_Ile_de_France
reanimation_confinement_1_regions['Nouvelle-Aquitaine'] = reanimations_confinement_1_Nouvelle_Aquitaine
reanimation_confinement_1_regions['Auvergne-Rhône-Alpes'] = reanimations_confinement_1_Auvergne_Rhone_Alpes
reanimation_confinement_1_regions['Occitanie'] = reanimations_confinement_1_Occitanie
reanimation_confinement_1_regions["Provences-Alpes-Côte-d'Azur"] = reanimations_confinement_1_Provences_Alpes_Côte_Azur
reanimation_confinement_1_regions['Corse'] = reanimations_confinement_1_Corse
reanimation_confinement_1_regions["Régions d'Outre Mer"] = reanimations_confinement_1_Outre_Mer


def confinement_1_regions(region):
    fig = px.line(reanimation_confinement_1_regions[f'{region}'], 
        x="date", y=reanimation_confinement_1_regions[f'{region}'].columns,
        title=f'intensive care beds occupied during the 1st confinement in {region}', 
        height=500, width=800)
    fig.update_xaxes(
        dtick='M1',
        tickformat="%d\n%b")
    return(fig.show())