import pandas as pd
import numpy as np
import folium


def map_dep(department, dep_fr):
    """
    map_dep

    Args:
        department (str): french department or DOM code
        dep_fr (dataframe): all french departments and DOM coordinates

    Returns:
        Folium Map Object: the french department (or DOM) map selected
    """
    dep_map = folium.Map(
        location=[
            dep_fr[dep_fr['maille_code'] == f'{department}']['Latitude'],
            dep_fr[dep_fr['maille_code'] == f'{department}']['Longitude']
            ], zoom_start=8)
    return dep_map


def map_screening(dep_code, all_map_dep):
    """
    map_screening
        the map screening centers by department with all info
    Args:
        dep_code (str): french department or DOM code
        all_map_dep (dict): all french department (and DOM) regrouped
    """
    return(all_map_dep[f'{dep_code}'])
























