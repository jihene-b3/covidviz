import reanimation.preprocess.load_data as rld
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

rld.rea_all.drop([
    'deces', 'hospitalises', 'nouvelles_hospitalisations',
    'nouvelles_reanimations', 'gueris'],
    1, inplace=True)

rld.rea_all = rld.rea_all.set_index('date')
rld.rea_all = rld.rea_all.sort_index()
rld.rea_all = rld.rea_all.loc['2020-03-18':]
rld.rea_all = rld.rea_all.loc[
    rld.rea_all['source_nom'] == "Santé publique France Data", :]
rld.rea_all.drop(['source_nom'], 1, inplace=True)

rld.rea_all.index = pd.to_datetime(rld.rea_all.index)

DEP_code = pd.DataFrame(rld.rea_all['maille_code'].unique())
for i in range(len(DEP_code)):
    DEP_code.iat[i, 0] = DEP_code.iat[i, 0][4:]
DEP_code = DEP_code.loc[:, 0].tolist()
DEP_name = pd.DataFrame(rld.rea_all['maille_nom'].unique())
DEP_name = DEP_name.loc[:, 0].tolist()
DEP = pd.concat([pd.DataFrame(DEP_code), pd.DataFrame(DEP_name)], 1)
DEP = DEP.set_axis(['code', 'nom'], axis=1)
DEP = DEP.sort_values(by='code')
DEP = DEP.reset_index()
DEP = DEP.drop(['index'], 1)


def rea_dep_nom(department):
    x = pd.DataFrame(rld.rea_all.loc[
        rld.rea_all['maille_nom'] == f"{department}",
        'reanimation']).resample("1D").sum()
    x = x.rename(columns={"reanimation": f"{department}"})
    return(x)


def rea_dep_code(num_dep):
    x = pd.DataFrame(rld.rea_all.loc[
        rld.rea_all['maille_code'] == f"DEP-{num_dep}",
        'reanimation']).resample("1D").sum()
    x = x.rename(columns={"reanimation": f"{num_dep}"})
    return(x)


rea_all_code = pd.DataFrame()
for num_dep in DEP['code'].tolist():
    rea_all_code = pd.concat(
        [rea_all_code, rea_dep_code(f'{num_dep}')],
        axis=1)

rea_all_code = rea_all_code.astype(int)
rea_all_code = rea_all_code.reset_index()
rea_all_code.head()

rea_all_nom = pd.DataFrame()
for nom_dep in DEP['nom'].tolist():
    rea_all_nom = pd.concat([rea_all_nom, rea_DEP_nom(f'{nom_dep}')], axis=1)

rea_all_nom = rea_all_nom.astype(int)
rea_all_nom = rea_all_nom.reset_index()


def rea_all_fr(rea_all_nom):
    fig = px.line(
        rea_all_nom, x="date", y=rea_all_nom.columns,
        title='intensive care beds occupied in France by departments',
        height=500, width=800)
    fig.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig.show())


rea_all_Bretagne = pd.concat([
    rea_all_nom['date'], rea_all_nom['Finistère'],
    rea_all_nom["Côtes-d'Armor"], rea_all_nom["Morbihan"],
    rea_all_nom["Ille-et-Vilaine"]], axis=1)

rea_all_Normandie = pd.concat([
    rea_all_nom['date'], rea_all_nom['Manche'], rea_all_nom["Calvados"],
    rea_all_nom["Eure"], rea_all_nom["Orne"], rea_all_nom["Seine-Maritime"]],
    axis=1)

rea_all_Pays_de_la_Loire = pd.concat([
    rea_all_nom['date'], rea_all_nom['Mayenne'], rea_all_nom["Sarthe"],
    rea_all_nom["Vendée"], rea_all_nom["Loire-Atlantique"],
    rea_all_nom["Maine-et-Loire"]], axis=1)

rea_all_Centre_Val_de_Loire = pd.concat([
    rea_all_nom['date'], rea_all_nom['Cher'], rea_all_nom["Eure-et-Loir"],
    rea_all_nom["Indre"], rea_all_nom["Indre-et-Loire"],
    rea_all_nom["Loir-et-Cher"], rea_all_nom["Loiret"]], axis=1)

rea_all_Bourgogne_Franche_Comte = pd.concat([
    rea_all_nom['date'], rea_all_nom["Côte-d'Or"], rea_all_nom["Doubs"],
    rea_all_nom["Jura"], rea_all_nom["Nièvre"], rea_all_nom["Haute-Saône"],
    rea_all_nom["Saône-et-Loire"], rea_all_nom["Yonne"]], axis=1)

rea_all_Grand_Est = pd.concat([
    rea_all_nom['date'], rea_all_nom["Ardennes"], rea_all_nom["Aube"],
    rea_all_nom["Marne"], rea_all_nom["Haute-Marne"],
    rea_all_nom["Meurthe-et-Moselle"], rea_all_nom["Meuse"],
    rea_all_nom["Moselle"], rea_all_nom["Bas-Rhin"], rea_all_nom["Haut-Rhin"],
    rea_all_nom["Vosges"]], axis=1)

rea_all_Hauts_de_France = pd.concat([
    rea_all_nom['date'], rea_all_nom["Aisne"], rea_all_nom["Nord"],
    rea_all_nom["Oise"], rea_all_nom["Pas-de-Calais"], rea_all_nom["Somme"]],
    axis=1)

rea_all_Ile_de_France = pd.concat([
    rea_all_nom['date'], rea_all_nom["Paris"],
    rea_all_nom["Seine-et-Marne"], rea_all_nom["Yvelines"],
    rea_all_nom["Essonne"], rea_all_nom["Hauts-de-Seine"],
    rea_all_nom["Seine-Saint-Denis"], rea_all_nom["Val-de-Marne"],
    rea_all_nom["Val-d'Oise"]], axis=1)

rea_all_Nouvelle_Aquitaine = pd.concat([
    rea_all_nom['date'], rea_all_nom["Charente"],
    rea_all_nom["Charente-Maritime"], rea_all_nom["Corrèze"],
    rea_all_nom["Creuse"], rea_all_nom["Dordogne"], rea_all_nom["Gironde"],
    rea_all_nom["Landes"], rea_all_nom["Lot-et-Garonne"],
    rea_all_nom["Pyrénées-Atlantiques"], rea_all_nom["Deux-Sèvres"],
    rea_all_nom["Vienne"], rea_all_nom["Haute-Vienne"]], axis=1)

rea_all_Auvergne_Rhone_Alpes = pd.concat([
    rea_all_nom['date'], rea_all_nom["Ain"], rea_all_nom["Allier"],
    rea_all_nom["Ardèche"], rea_all_nom["Cantal"], rea_all_nom["Drôme"],
    rea_all_nom["Isère"], rea_all_nom["Loire"], rea_all_nom["Haute-Loire"],
    rea_all_nom["Puy-de-Dôme"], rea_all_nom["Rhône"], rea_all_nom["Savoie"],
    rea_all_nom["Haute-Savoie"]], axis=1)

rea_all_Occitanie = pd.concat([
    rea_all_nom['date'], rea_all_nom["Ariège"], rea_all_nom["Aude"],
    rea_all_nom["Aveyron"], rea_all_nom["Gard"], rea_all_nom["Haute-Garonne"],
    rea_all_nom["Gers"], rea_all_nom["Hérault"], rea_all_nom["Lot"],
    rea_all_nom["Lozère"], rea_all_nom["Hautes-Pyrénées"],
    rea_all_nom["Pyrénées-Orientales"], rea_all_nom["Tarn"],
    rea_all_nom["Tarn-et-Garonne"]], axis=1)

rea_all_Provence_Alpes_Côte_Azur = pd.concat([
    rea_all_nom['date'], rea_all_nom["Alpes-de-Haute-Provence"],
    rea_all_nom["Hautes-Alpes"], rea_all_nom["Alpes-Maritimes"],
    rea_all_nom["Bouches-du-Rhône"], rea_all_nom["Var"],
    rea_all_nom["Vaucluse"]], axis=1)

rea_all_Corse = pd.concat([
    rea_all_nom['date'], rea_all_nom["Corse-du-Sud"],
    rea_all_nom["Haute-Corse"]], axis=1)

rea_all_Outre_Mer = pd.concat([
    rea_all_nom['date'], rea_all_nom["Guadeloupe"], rea_all_nom["Martinique"],
    rea_all_nom["Guyane"], rea_all_nom["La Réunion"], rea_all_nom["Mayotte"]],
    axis=1)


rea_all_regions = {}

rea_all_regions['Bretagne'] = rea_all_Bretagne

rea_all_regions['Normandie'] = rea_all_Normandie

rea_all_regions['Pays de la Loire'] = rea_all_Pays_de_la_Loire
rea_all_regions['Centre-Val-de-Loire'] = rea_all_Centre_Val_de_Loire
rea_all_regions['Bourgogne-Franche-Comté'] = rea_all_Bourgogne_Franche_Comte
rea_all_regions['Grand-Est'] = rea_all_Grand_Est
rea_all_regions['Hauts-de-France'] = rea_all_Hauts_de_France
rea_all_regions['Île-de-France'] = rea_all_Ile_de_France
rea_all_regions['Nouvelle-Aquitaine'] = rea_all_Nouvelle_Aquitaine
rea_all_regions['Auvergne-Rhône-Alpes'] = rea_all_Auvergne_Rhone_Alpes
rea_all_regions['Occitanie'] = rea_all_Occitanie

rea_all_regions["Provence-Alpes-Côte-d'Azur"] =
rea_all_Provence_Alpes_Côte_Azur

rea_all_regions['Corse'] = rea_all_Corse
rea_all_regions["Régions d'Outre Mer"] = rea_all_Outre_Mer


def rea_regions(region):
    fig = px.line(
        rea_all_regions[f'{region}'],
        x="date",
        y=rea_all_regions[f'{region}'].columns,
        title=f'intensive care beds occupied since in {region}',
        height=500, width=800)
    fig.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig.show())


regions = [
    'Bretagne', 'Normandie', 'Pays de la Loire', 'Centre-Val-de-Loire',
    'Bourgogne-Franche-Comté', 'Grand-Est', 'Hauts-de-France', 'Île-de-France',
    'Nouvelle-Aquitaine', 'Auvergne-Rhône-Alpes', 'Occitanie',
    "Provence-Alpes-Côte-d'Azur", 'Corse', "Régions d'Outre Mer"
]

for name_region in regions:
    rea_all_regions[f'{name_region}']['Total'] =
    np.sum(rea_all_regions[f'{name_region}'].iloc[:, 1:], 1)

rea_region_tot = pd.DataFrame()

for name_region in regions:
    rea_region_tot = pd.concat([
        rea_region_tot, rea_all_regions[f'{name_region}']['Total']], 1)


rea_region_tot.columns = regions
rea_region_tot.insert(0, 'date', rea_all_nom['date'])


def rea_all_reg(rea_region_tot):
    fig = px.line(
        rea_region_tot,
        x="date", y=rea_region_tot.columns,
        title=f'intensive care beds occupied by regions',
        height=500, width=800)
    fig.update_xaxes(
        dtick='M1',
        tickformat="%b")
    return(fig.show())


rea_region_tot['Total'] = np.sum(rea_region_tot.iloc[:, 1:], 1)


def rea_flux(rea_region_tot):
    fig = px.bar(
        rea_region_tot,
        x='date', y='Total',
        title=f'the flow of patients in ICU in France during Covid19 crisis',
        color='Total', labels={'Total': 'Number of patients'},
        height=500, width=800)
    return(fig.show())


rea_all_period_by_region = pd.DataFrame(
    np.sum(rea_region_tot.iloc[:, 1:15], 0))
rea_all_period_by_region.columns = ['Total number']


def repartition_rea_reg(rea_all_period_by_region):
    fig = px.pie(
        rea_all_period_by_region,
        values='Total number', names=rea_all_period_by_region.index,
        title='Distribution of ICU by region',
        color_discrete_sequence=px.colors.sequential.RdBu,
        height=500, width=800)
    return(fig.show())


rld.beds_in_rea_reg = rld.beds_in_rea_reg.rename(
    columns={'Unnamed: 0': 'Région'})
rld.beds_in_rea_reg = rld.beds_in_rea_reg.drop(['CHR', 'Autres'], 1)

rld.beds_in_rea_reg = rld.beds_in_rea_reg.loc[:13]
rld.beds_in_rea_reg = rld.beds_in_rea_reg.rename(
    columns={'Confondu': 'Nombre de lits'})
rld.beds_in_rea_reg = rld.beds_in_rea_reg.reindex(
    index=[2, 8, 11, 3, 1, 5, 6, 7, 9, 0, 10, 12, 4, 13])
rld.beds_in_rea_reg = rld.beds_in_rea_reg.reset_index()
rld.beds_in_rea_reg = rld.beds_in_rea_reg.drop(['index'], 1)

rld.beds_in_rea_reg = rld.beds_in_rea_reg.set_index('Région')

rld.beds_in_rea_dep = rld.beds_in_rea_dep.drop(['NUM_DEP'], 1)
rld.beds_in_rea_dep = rld.beds_in_rea_dep.set_index('DEP')

rea_reg_prop = rea_region_tot.drop(['Total'], 1)


for col in regions:
    for row in range(len(rea_reg_prop)):
        rea_reg_prop.loc[row, f'{col}'] = rea_reg_prop.loc[
            row, f'{col}']/int(rld.beds_in_rea_reg.loc[f'{col}',
                                                       'Nombre de lits'])


rea_dep_prop = rea_all_nom.copy()

for col in rld.beds_in_rea_dep.index:
    for row in range(len(rea_dep_prop)):
        rea_dep_prop.loc[row, f'{col}'] = rea_dep_prop.loc[
            row, f'{col}']/int(rld.beds_in_rea_dep.loc[f'{col}',
                                                       'Lits rea dispo'])

df_reg = rea_reg_prop.iloc[:, 1:].copy()
df_dep = rea_dep_prop.iloc[:, 1:].copy()


def rea_sat_reg(df_reg):
    fig = px.imshow(
        df_reg, y=rea_reg_prop['date'],
        title='Regional saturation in ICU',
        height=700, width=800)
    return(fig.show())


def rea_sat_dep(df_dep):
    fig = px.imshow(
        df_dep, y=rea_reg_prop['date'],
        title='Regional saturation in ICU',
        height=700, width=800)
    return(fig.show())
