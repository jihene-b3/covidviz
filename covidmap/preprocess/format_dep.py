def format_dep(df_covid):
    df_covid['maille_code'] = df_covid['maille_code'].map(lambda x: x.lstrip('DEP-'))
    return df_covid