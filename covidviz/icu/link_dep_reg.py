

def link_dep_reg(df_all_dep, ):
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
    return icu_by_reg