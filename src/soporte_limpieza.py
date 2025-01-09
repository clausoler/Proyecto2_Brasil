import pandas as pd

def reporte_nulos(df_datos_brasil):
    """
    Genera un reporte sobre los valores nulos de un DataFrame.

    Esta función analiza el DataFrame proporcionado y devuelve un nuevo DataFrame 
    con información detallada sobre la cantidad de valores nulos, el porcentaje 
    de valores nulos respecto al total de filas y el tipo de dato de cada columna.

    Parámetros:
    -----------
    df_datos_brasil : pd.DataFrame
        DataFrame que se desea analizar en busca de valores nulos.

    Retorna:
    --------
    pd.DataFrame
        Un DataFrame con las siguientes columnas:
        - "número_nulos": número de valores nulos en cada columna.
        - "porcentaje_nulos": porcentaje de valores nulos respecto al total de filas.
        - "tipo_variables": tipo de dato (dtype) de cada columna.

    """
    df_reporte = pd.DataFrame()
    df_reporte["número_nulos"] = df_datos_brasil.isnull().sum()
    df_reporte["porcentaje_nulos"] = round((df_datos_brasil.isnull().sum() / len(df_datos_brasil)) * 100, 2)
    df_reporte["tipo_variables"] = df_datos_brasil.dtypes
    return df_reporte
 
