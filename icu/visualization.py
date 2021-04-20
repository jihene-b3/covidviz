import pandas as pd
import numpy as np
import datetime
import covidmap
from covidmap.preprocess.clean_df import choose_columns, choose_granularity
from covidmap.io.load_db import Load_db
import plotly.express as px

# Load data from covidmap (because already set)
df = choose_columns(
    Load_db.save_as_df(),
    [
        'date',
        'granularite',
        'maille_code',
        'maille_nom',
        'reanimation',
        'source_nom'
    ]
)

"""
 ICU IN FRENCH DEPARTMENTS

 We generate a first DataFrame of ICU in french departments,
 with keeping one source : 'Santé publique France Data',
"""
df_dep = df.copy()
df_dep = choose_granularity(df_dep, 'departement')
df_dep.drop('granularite', axis=1, inplace=True)
df_dep.loc[df_dep['source_nom'] == "Santé publique France Data", :]
df_dep.drop(['source_nom'], 1, inplace=True)
df_dep = df_dep.set_index('date')
df_dep = df_dep.sort_index()
df_dep.index = pd.to_datetime(df_dep.index)
df_dep.fillna(0, inplace=True)
df_dep['reanimation'] = df_dep['reanimation'].astype(int)

"""
 We regroup the data by department using dictionary type
"""
dict_dep = {}
for department in df_dep['maille_nom'].unique().tolist():
    dict_dep[department] = pd.DataFrame(
        df_dep.loc[df_dep['maille_nom'] == department,
                   'reanimation']).resample("1D").sum()
    dict_dep[department] = dict_dep[department].rename(
        columns={"reanimation": department})

"""
 We create a DataFrame including all departments
"""

df_all_dep = pd.DataFrame()
for department in df_dep['maille_nom'].unique().tolist():
    df_all_dep = pd.concat([df_all_dep, dict_dep[department]], axis=1)

df_all_dep.fillna(0, inplace=True)
df_all_dep = df_all_dep.astype(int)
df_all_dep = df_all_dep.reset_index()


def icu_dep_all():
    """
    return the lineplot of intensive care beds occupied
    since 1st confinement in french departments
    """
    fig1 = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title='Intensive care beds occupied since 1st confinement in french departments',
        height=500, width=800)
    fig1.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig1.show())


def icu_dep_conf1():
    """
    return the lineplot of intensive care beds occupied
    during the 1st confinement in french departments
    """
    fig2 = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-03-17', '2020-05-10'],
        title='Intensive care beds occupied during the 1st confinement in french departments',
        height=500, width=800)
    fig2.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig2.show())


def icu_dep_dec():
    """
    return the lineplot of intensive care beds occupied
    during deconfinement in french departments
    """
    fig3 = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-05-11', '2020-10-29'],
        title='Intensive care beds occupied during deconfinement in french departments', 
        height=500, width=800)
    fig3.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig3.show())


def icu_dep_conf2():
    """
    return the lineplot of intensive care beds occupied
    during the 2nd confinement in french departments
    """
    fig4 = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-10-30', '2021-12-14'],
        title='Intensive care beds occupied during the 2nd confinement in french departments',
        height=500, width=800)
    fig4.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig4.show())


def icu_dep_curfew():
    """
    return the lineplot of intensive care beds occupied
    during curfew in french departments
    """
    fig5 = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2020-12-15', '2021-04-02'],
        title='Intensive care beds occupied during curfew in french departments',
        height=500, width=800)
    fig5.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig5.show())


def icu_dep_conf3():
    """
    return the lineplot of intensive care beds occupied
    during the 3rd confinement in french departments
    """
    fig6 = px.line(
        df_all_dep,
        x='date', y=df_all_dep.columns,
        range_x=['2021-04-03', datetime.datetime.today().strftime('%Y-%m-%d')],
        title='Intensive care beds occupied during the 3rd confinement in french departments',
        height=500, width=800)
    return(fig6.show())

"""
 ICU IN FRENCH REGIONS

 We generate a second DataFrame of ICU in french regions,
 with keeping one source : 'OpenCOVID19-fr',
"""
df_reg = df.copy()
df_reg = choose_granularity(df_reg, 'region')
df_reg.drop(['granularite', 'maille_code'], axis=1, inplace=True)
df_reg.loc[df_reg['source_nom'] == "OpenCOVID19-fr", :]
df_reg.drop(['source_nom'], 1, inplace=True)
df_reg = df_reg.set_index('date')
df_reg = df_reg.sort_index()
df_reg.index = pd.to_datetime(df_reg.index)
df_reg.fillna(0, inplace=True)
df_reg['reanimation'] = df_reg['reanimation'].astype(int)

"""
 We regroup the data by region using dictionary type
"""
dict_reg = {}
for region in df_reg['maille_nom'].unique().tolist():
    dict_reg[region] = pd.DataFrame(
        df_reg.loc[df_reg['maille_nom'] == region,
                   'reanimation']).resample("1D").sum()
    dict_reg[region] = dict_reg[region].rename(
        columns = {"reanimation": region})

"""
 We create a DataFrame including all regions
"""
df_all_reg = pd.DataFrame()
for region in df_reg['maille_nom'].unique().tolist():
    df_all_reg = pd.concat([df_all_reg, dict_reg[region]], axis=1)

df_all_reg.fillna(0, inplace=True)
df_all_reg = df_all_reg.astype(int)
df_all_reg = df_all_reg.reset_index()


def icu_reg_all():
    """
    return the lineplot of intensive care beds occupied
    since 1st confinement in french departments
    """
    fig1 = px.line(
        df_all_reg,
        x='date', y=df_all_reg.columns,
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title='Intensive care beds occupied since 1st confinement in french regions',
        height=500, width=800)
    fig1.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig1.show())


def icu_reg_conf1():
    """
    return the lineplot of intensive care beds occupied
    during the 1st confinement in french departments
    """
    fig2 = px.line(
        df_all_reg,
        x='date', y=df_all_reg.columns,
        range_x=['2020-03-17', '2020-05-10'],
        title='Intensive care beds occupied during the 1st confinement in french regions',
        height=500, width=800)
    fig2.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig2.show)


def icu_reg_dec():
    """
    return the lineplot of intensive care beds occupied
    during deconfinement in french departments
    """
    fig3 = px.line(
        df_all_reg,
        x='date', y=df_all_reg.columns,
        range_x=['2020-05-11', '2020-10-29'],
        title='Intensive care beds occupied during deconfinement in french regions',
        height=500, width=800)
    fig3.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig3.show())


def icu_reg_conf2():
    """
    return the lineplot of intensive care beds occupied
    during the 2nd confinement in french departments
    """
    fig4 = px.line(
        df_all_reg,
        x='date', y=df_all_reg.columns,
        range_x=['2020-10-30', '2021-12-14'],
        title='Intensive care beds occupied during the 2nd confinement in french regions',
        height=500, width=800)
    fig4.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig4.show())


def icu_reg_curfew():
    """
    return the lineplot of intensive care beds occupied
    during curfew in french departments
    """
    fig5 = px.line(
        df_all_reg,
        x='date', y=df_all_reg.columns,
        range_x=['2020-12-15', '2021-04-02'],
        title='Intensive care beds occupied during curfew in french regions',
        height=500, width=800)
    fig5.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig5.show())


def icu_reg_conf3():
    """
    return the lineplot of intensive care beds occupied
    during the 3rd confinement in french departments
    """
    fig6 = px.line(
        df_all_reg,
        x='date', y=df_all_reg.columns,
        range_x=['2021-04-03', datetime.datetime.today().strftime('%Y-%m-%d')],
        title='Intensive care beds occupied during the 3rd confinement in french regions',
        height=500, width=800)
    return(fig6.show())


"""
 We generate a new DataFrame for each region with departments
"""
icu_bretagne = pd.concat([
    df_all_dep['date'],
    df_all_dep['Finistère'],
    df_all_dep["Côtes-d'Armor"],
    df_all_dep["Morbihan"],
    df_all_dep["Ille-et-Vilaine"]], axis=1)

icu_normandie = pd.concat([
    df_all_dep['date'],
    df_all_dep['Manche'],
    df_all_dep["Calvados"],
    df_all_dep["Eure"],
    df_all_dep["Orne"],
    df_all_dep["Seine-Maritime"]], axis=1)

icu_pays_de_la_loire = pd.concat([
    df_all_dep['date'],
    df_all_dep['Mayenne'],
    df_all_dep["Sarthe"],
    df_all_dep["Vendée"],
    df_all_dep["Loire-Atlantique"],
    df_all_dep["Maine-et-Loire"]], axis=1)

icu_centre_val_de_loire = pd.concat([
    df_all_dep['date'],
    df_all_dep['Cher'],
    df_all_dep["Eure-et-Loir"],
    df_all_dep["Indre"],
    df_all_dep["Indre-et-Loire"],
    df_all_dep["Loir-et-Cher"],
    df_all_dep["Loiret"]], axis=1)

icu_bourgogne_franche_comte = pd.concat([
    df_all_dep['date'],
    df_all_dep["Côte-d'Or"],
    df_all_dep["Doubs"],
    df_all_dep["Jura"],
    df_all_dep["Nièvre"],
    df_all_dep["Haute-Saône"],
    df_all_dep["Saône-et-Loire"],
    df_all_dep["Yonne"]], axis=1)

icu_grand_est = pd.concat([
    df_all_dep['date'],
    df_all_dep["Ardennes"],
    df_all_dep["Aube"],
    df_all_dep["Marne"],
    df_all_dep["Haute-Marne"],
    df_all_dep["Meurthe-et-Moselle"],
    df_all_dep["Meuse"],
    df_all_dep["Moselle"],
    df_all_dep["Bas-Rhin"],
    df_all_dep["Haut-Rhin"],
    df_all_dep["Vosges"]], axis=1)

icu_hauts_de_france = pd.concat([
    df_all_dep['date'],
    df_all_dep["Aisne"],
    df_all_dep["Nord"],
    df_all_dep["Oise"],
    df_all_dep["Pas-de-Calais"],
    df_all_dep["Somme"]], axis=1)

icu_ile_de_france = pd.concat([
    df_all_dep['date'],
    df_all_dep["Paris"],
    df_all_dep["Seine-et-Marne"],
    df_all_dep["Yvelines"],
    df_all_dep["Essonne"],
    df_all_dep["Hauts-de-Seine"],
    df_all_dep["Seine-Saint-Denis"],
    df_all_dep["Val-de-Marne"],
    df_all_dep["Val-d'Oise"]], axis=1)

icu_nouvelle_aquitaine = pd.concat([
    df_all_dep['date'],
    df_all_dep["Charente"],
    df_all_dep["Charente-Maritime"],
    df_all_dep["Corrèze"],
    df_all_dep["Creuse"],
    df_all_dep["Dordogne"],
    df_all_dep["Gironde"],
    df_all_dep["Landes"],
    df_all_dep["Lot-et-Garonne"],
    df_all_dep["Pyrénées-Atlantiques"],
    df_all_dep["Deux-Sèvres"],
    df_all_dep["Vienne"],
    df_all_dep["Haute-Vienne"]], axis=1)

icu_auvergne_rhone_alpes = pd.concat([
    df_all_dep['date'],
    df_all_dep["Ain"],
    df_all_dep["Allier"],
    df_all_dep["Ardèche"],
    df_all_dep["Cantal"],
    df_all_dep["Drôme"],
    df_all_dep["Isère"],
    df_all_dep["Loire"],
    df_all_dep["Haute-Loire"],
    df_all_dep["Puy-de-Dôme"],
    df_all_dep["Rhône"],
    df_all_dep["Savoie"],
    df_all_dep["Haute-Savoie"]], axis=1)

icu_occitanie = pd.concat([
    df_all_dep['date'],
    df_all_dep["Ariège"],
    df_all_dep["Aude"],
    df_all_dep["Aveyron"],
    df_all_dep["Gard"],
    df_all_dep["Haute-Garonne"],
    df_all_dep["Gers"],
    df_all_dep["Hérault"],
    df_all_dep["Lot"],
    df_all_dep["Lozère"],
    df_all_dep["Hautes-Pyrénées"],
    df_all_dep["Pyrénées-Orientales"],
    df_all_dep["Tarn"],
    df_all_dep["Tarn-et-Garonne"]], axis=1)

icu_paca = pd.concat([
    df_all_dep['date'],
    df_all_dep["Alpes-de-Haute-Provence"],
    df_all_dep["Hautes-Alpes"],
    df_all_dep["Alpes-Maritimes"],
    df_all_dep["Bouches-du-Rhône"],
    df_all_dep["Var"],
    df_all_dep["Vaucluse"]], axis=1)

icu_corse = pd.concat([
    df_all_dep['date'],
    df_all_dep["Corse-du-Sud"],
    df_all_dep["Haute-Corse"]], axis=1)

icu_dom = pd.concat([
    df_all_dep['date'],
    df_all_dep["Guadeloupe"],
    df_all_dep["Martinique"],
    df_all_dep["Guyane"],
    df_all_dep["La Réunion"],
    df_all_dep["Mayotte"]], axis=1)

icu_by_reg = {}
icu_by_reg['Bretagne'] = icu_bretagne
icu_by_reg['Normandie'] = icu_normandie
icu_by_reg['Pays de la Loire'] = icu_pays_de_la_loire
icu_by_reg['Centre-Val-de-Loire'] = icu_centre_val_de_loire
icu_by_reg['Bourgogne-Franche-Comté'] = icu_bourgogne_franche_comte
icu_by_reg['Grand-Est'] = icu_grand_est
icu_by_reg['Hauts-de-France'] = icu_hauts_de_france
icu_by_reg['Île-de-France'] = icu_ile_de_france
icu_by_reg['Nouvelle-Aquitaine'] = icu_nouvelle_aquitaine
icu_by_reg['Auvergne-Rhône-Alpes'] = icu_auvergne_rhone_alpes
icu_by_reg['Occitanie'] = icu_occitanie
icu_by_reg["Provences-Alpes-Côte-d'Azur"] = icu_paca
icu_by_reg['Corse'] = icu_corse
icu_by_reg["Régions d'Outre Mer"] = icu_dom


def icu_by_reg_all(region):
    fig1 = px.line(
        icu_by_reg[f'{region}'],
        x='date', y=icu_by_reg[f'{region}'].columns,
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title=f'Intensive care beds occupied since 1st confinement in {region}',
        height=500, width=800)
    fig1.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig1.show())


def icu_by_reg_conf1(region):
    fig2 = px.line(
        icu_by_reg[f'{region}'],
        x='date', y=icu_by_reg[f'{region}'].columns,
        range_x=['2020-03-17', '2020-05-10'],
        title=f'Intensive care beds occupied during the 1st confinement in {region}',
        height=500, width=800)
    fig2.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig2.show)


def icu_by_reg_dec(region):
    fig3 = px.line(
        icu_by_reg[f'{region}'],
        x='date', y=icu_by_reg[f'{region}'].columns,
        range_x=['2020-05-11', '2020-10-29'],
        title=f'Intensive care beds occupied during deconfinement in {region}',
        height=500, width=800)
    fig3.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig3.show())


def icu_by_reg_conf2(region):
    fig4 = px.line(
        icu_by_reg[f'{region}'],
        x='date', y=icu_by_reg[f'{region}'].columns,
        range_x=['2020-10-30', '2021-12-14'],
        title=f'Intensive care beds occupied during the 2nd confinement in {region}',
        height=500, width=800)
    fig4.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig4.show())


def icu_by_reg_curfew(region):
    fig5 = px.line(
        icu_by_reg[f'{region}'],
        x='date', y=icu_by_reg[f'{region}'].columns,
        range_x=['2020-12-15', '2021-04-02'],
        title=f'Intensive care beds occupied during curfew in {region}',
        height=500, width=800)
    fig5.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig5.show())


def icu_by_reg_conf3(region):
    fig6 = px.line(
        icu_by_reg[f'{region}'],
        x='date', y=icu_by_reg[f'{region}'].columns,
        range_x=['2021-04-03', datetime.datetime.today().strftime('%Y-%m-%d')],
        title=f'Intensive care beds occupied during the 3rd confinement in {region}',
        height=500, width=800)
    return(fig6.show())


df_all_reg['Total'] = np.sum(df_all_reg.iloc[:, 1:], axis=1)


def icu_all_reg():
    """
    see the title
    """
    fig = px.bar(
        df_all_reg,
        x='date', y='Total',
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title=f'ICU flux in France during Covid19 crisis',
        color='Total',
        labels={'Total': 'Number of patients'},
        height=500, width=800)
    return(fig.show())


df_all_reg["Régions d'Outre Mer"] = df_all_reg["Guadeloupe"] + df_all_reg['Martinique'] + df_all_reg['Guyane'] + df_all_reg['La Réunion'] + df_all_reg['Mayotte']
df_all_reg_tot = df_all_reg['Total']
df_all_reg.drop(['Guadeloupe', 'Martinique', 'Guyane', 'La Réunion', 'Mayotte', 'Total'], axis=1, inplace=True)

df_all_reg.rename(columns={
                        "Provence-Alpes-Côte d'Azur": "Provence-Alpes-Côte-d'Azur",
                        "Centre-Val de Loire": 'Centre-Val-de-Loire',
                        "Grand Est": "Grand-Est"}, inplace=True)

icu_reg_total = pd.DataFrame(np.sum(df_all_reg.iloc[:, 1:15], axis=0))
icu_reg_total.columns = ['Total number']


def icu_reg_repartition():
    """
    see the title
    """
    fig = px.pie(
        icu_reg_total,
        values='Total number',
        names=icu_reg_total.index,
        title='Regional repartition of ICU during Covid19 crisis',
        color_discrete_sequence=px.colors.sequential.RdBu,
        height=500, width=800)
    return(fig.show())


icu_beds_reg = pd.read_csv('icu/bed_rea_reg.csv', delimiter=';')

icu_beds_reg = icu_beds_reg.rename(columns={'Unnamed: 0': 'Région'})
icu_beds_reg = icu_beds_reg.drop(['CHR', 'Autres'], 1)

icu_beds_reg = icu_beds_reg.loc[:13]
icu_beds_reg = icu_beds_reg.rename(columns={'Confondu': 'Nombre de lits'})
icu_beds_reg = icu_beds_reg.reindex(index=[7, 8, 9, 4, 6, 5, 3, 1, 2, 0, 10, 11, 12, 13])
icu_beds_reg = icu_beds_reg.reset_index()
icu_beds_reg = icu_beds_reg.drop(['index'], 1)
icu_beds_reg = icu_beds_reg.rename(index={"Provence-Alpes-Côte-d'Azur": "Provence-Alpes-Côte d'Azur" })

icu_beds_reg = icu_beds_reg.set_index('Région')

icu_beds_reg_prop = df_all_reg.copy()
for col in icu_beds_reg.index.tolist():
    for row in range(len(icu_beds_reg_prop)):
        icu_beds_reg_prop.loc[row, col] = (icu_beds_reg_prop.loc[row, col]/int(icu_beds_reg.loc[col, 'Nombre de lits']))*100


def heat_map_icu_reg():
    """
    see the title
    """
    fig = px.imshow(
        icu_beds_reg_prop.iloc[:, 1:],
        y=icu_beds_reg_prop['date'],
        title='Regional saturation in % in ICU during Covid19 crisis',
        height=700, width=800)
    return(fig.show())
