__version__ = '0.0.1'

from .io.load_db import Load_db
from .covidmap.plot_map import Map_covid
from .preprocess.format_granu import format_granularity
from .preprocess.clean_df import choose_columns, choose_granularity
from .icu.department import clean_df_dep, regroup_by_dep, create_df_all_dep, icu_dep_all, icu_dep_display
from .icu.link_dep_reg import link_dep_reg
from .icu.region import clean_df_reg, regroup_by_reg, create_df_all_reg, icu_reg_all, icu_reg_display, icu_by_reg_all, icu_by_reg_display, icu_all_reg_display, change_format_reg, create_reg_total, icu_reg_repartition, create_icu_beds_reg, heat_map_icu_reg
from .screening.plot_map import clean_public_centers, clean_dep, map_dep, regroup_map, regroup_public_center_by_dep, clean_private_centers, regroup_private_center_by_dep, markers_set, map_screening
from .screening.graphs import screening_by_age_dep, screening_by_age, screening_by_dep, daily_test, daily_test_age, daily_test_dep
from .sparse.transfer_graph import create_transfer_graph, plot_transfer_graph, plot_adjacency_matrix
