import pandas as pd
import numpy as np
import datetime
import plotly.express as px

"""
 ICU IN FRENCH REGIONS

 We generate a second DataFrame of ICU in french regions,
 with keeping one source : 'OpenCOVID19-fr',
"""
def format_df_reg(df):
    df_reg = df.copy()
    df_reg.drop(['granularite', 'maille_code'], axis=1, inplace=True)
    df_reg.loc[df_reg['source_nom'] == "OpenCOVID19-fr", :]
    df_reg.drop(['source_nom'], 1, inplace=True)
    df_reg = df_reg.set_index('date')
    df_reg = df_reg.sort_index()
    df_reg.index = pd.to_datetime(df_reg.index)
    df_reg.fillna(0, inplace=True)
    df_reg['reanimation'] = df_reg['reanimation'].astype(int)
    return df_reg

def regroup_by_reg(df_reg):
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
    return dict_reg

def create_df_all_reg(df_reg, dict_reg):
    """
    We create a DataFrame including all regions
    """
    df_all_reg = pd.DataFrame()
    for region in df_reg['maille_nom'].unique().tolist():
        df_all_reg = pd.concat([df_all_reg, dict_reg[region]], axis=1)

    df_all_reg.fillna(0, inplace=True)
    df_all_reg = df_all_reg.astype(int)
    df_all_reg = df_all_reg.reset_index()
    return df_all_reg


def icu_reg_all(df_all_reg):
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


def icu_reg_conf1(df_all_reg):
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


def icu_reg_dec(df_all_reg):
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


def icu_reg_conf2(df_all_reg):
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


def icu_reg_curfew(df_all_reg):
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


def icu_reg_conf3(df_all_reg):
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


def icu_by_reg_all(region, icu_by_reg):
    fig1 = px.line(
        icu_by_reg[f'{region}'],
        x='date', y=icu_by_reg[f'{region}'].columns,
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title=f'Intensive care beds occupied since 1st confinement in {region}',
        height=500, width=800)
    fig1.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig1.show())


def icu_by_reg_conf1(region, icu_by_reg):
    fig2 = px.line(
        icu_by_reg[f'{region}'],
        x='date', y=icu_by_reg[f'{region}'].columns,
        range_x=['2020-03-17', '2020-05-10'],
        title=f'Intensive care beds occupied during the 1st confinement in {region}',
        height=500, width=800)
    fig2.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig2.show)


def icu_by_reg_dec(region, icu_by_reg):
    fig3 = px.line(
        icu_by_reg[f'{region}'],
        x='date', y=icu_by_reg[f'{region}'].columns,
        range_x=['2020-05-11', '2020-10-29'],
        title=f'Intensive care beds occupied during deconfinement in {region}',
        height=500, width=800)
    fig3.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig3.show())


def icu_by_reg_conf2(region, icu_by_reg):
    fig4 = px.line(
        icu_by_reg[f'{region}'],
        x='date', y=icu_by_reg[f'{region}'].columns,
        range_x=['2020-10-30', '2021-12-14'],
        title=f'Intensive care beds occupied during the 2nd confinement in {region}',
        height=500, width=800)
    fig4.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig4.show())


def icu_by_reg_curfew(region, icu_by_reg):
    fig5 = px.line(
        icu_by_reg[f'{region}'],
        x='date', y=icu_by_reg[f'{region}'].columns,
        range_x=['2020-12-15', '2021-04-02'],
        title=f'Intensive care beds occupied during curfew in {region}',
        height=500, width=800)
    fig5.update_xaxes(dtick='M1', tickformat="%d\n%b")
    return(fig5.show())


def icu_by_reg_conf3(region, icu_by_reg):
    fig6 = px.line(
        icu_by_reg[f'{region}'],
        x='date', y=icu_by_reg[f'{region}'].columns,
        range_x=['2021-04-03', datetime.datetime.today().strftime('%Y-%m-%d')],
        title=f'Intensive care beds occupied during the 3rd confinement in {region}',
        height=500, width=800)
    return(fig6.show())





def icu_all_reg(df_all_reg):
    """
    see the title
    """
    df_all_reg['Total'] = np.sum(df_all_reg.iloc[:, 1:], axis=1)
    fig = px.bar(
        df_all_reg,
        x='date', y='Total',
        range_x=['2020-03-17', datetime.datetime.today().strftime('%Y-%m-%d')],
        title=f'ICU flux in France during Covid19 crisis',
        color='Total',
        labels={'Total': 'Number of patients'},
        height=500, width=800)
    return(fig.show())

def change_format_reg(df_all_reg):
    df_all_reg["Régions d'Outre Mer"] = df_all_reg["Guadeloupe"] + df_all_reg['Martinique'] + df_all_reg['Guyane'] + df_all_reg['La Réunion'] + df_all_reg['Mayotte']
    df_all_reg_tot = df_all_reg['Total']
    df_all_reg.drop(['Guadeloupe', 'Martinique', 'Guyane', 'La Réunion', 'Mayotte', 'Total'], axis=1, inplace=True)

    df_all_reg.rename(columns={
                            "Provence-Alpes-Côte d'Azur": "Provence-Alpes-Côte-d'Azur",
                            "Centre-Val de Loire": 'Centre-Val-de-Loire',
                            "Grand Est": "Grand-Est"}, inplace=True)

def create_reg_total(df_all_reg):
    df_all_reg = change_format_reg(df_all_reg)
    icu_reg_total = pd.DataFrame(np.sum(df_all_reg.iloc[:, 1:15], axis=0))
    icu_reg_total.columns = ['Total number']
    return icu_reg_total
    


def icu_reg_repartition(icu_reg_total):
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


def create_icu_beds_reg():
    icu_beds_reg = pd.read_csv('../data/bed_rea_reg.csv', delimiter=';')

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
    return(icu_beds_reg_prop)


def heat_map_icu_reg(icu_beds_reg_prop):
    """
    see the title
    """
    fig = px.imshow(
        icu_beds_reg_prop.iloc[:, 1:],
        y=icu_beds_reg_prop['date'],
        title='Regional saturation in % in ICU during Covid19 crisis',
        height=700, width=800)
    return(fig.show())
