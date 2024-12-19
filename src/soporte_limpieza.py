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
    


# 1. Distribución de Ingresos por Categoría económica
 
# Función para calcular la distribución de ingresos por categoría económica
def calcular_distribucion_categorias(dataframe, columna):
    """
    Calcula la distribución de una columna categórica, incluyendo frecuencias y porcentajes.

    Args:
        dataframe (pd.DataFrame): El DataFrame que contiene los datos.
        columna (str): Nombre de la columna categórica.

    Returns:
        pd.DataFrame: DataFrame con las categorías, su frecuencia y porcentaje.
    """
    # Calcular la frecuencia de cada categoría
    distribucion = dataframe[columna].value_counts()
    
    # Calcular el porcentaje de cada categoría
    total = distribucion.sum()
    porcentaje = round((distribucion / total) * 100, 2)
    
    # Crear un DataFrame con los resultados
    resultado = pd.DataFrame({
        "CATEGORÍA ECONÓMICA": distribucion.index,
        "Frecuencia": distribucion.values,
        "Porcentaje (%)": porcentaje.values
    }).reset_index(drop=True)
    
    return resultado

# Aplicar la función al DataFrame
resultado_distribucion = calcular_distribucion_categorias(df_datos_brasil, "CATEGORÍA ECONÓMICA")

# Mostrar el resultado
resultado_distribucion

 
  
# Función ajustada para evitar la advertencia de pandas
def calcular_diferencia_promedio(dataframe, columna_categoria, columna_previsto, columna_realizado):
    """
    Calcula la diferencia promedio entre ingresos previstos y realizados por cada categoría,
    manejando valores no numéricos o vacíos, y evitando advertencias de pandas.

    Args:
        dataframe (pd.DataFrame): El DataFrame que contiene los datos.
        columna_categoria (str): Nombre de la columna categórica.
        columna_previsto (str): Nombre de la columna con los valores previstos.
        columna_realizado (str): Nombre de la columna con los valores realizados.

    Returns:
        pd.DataFrame: DataFrame con las categorías y sus diferencias promedio.
    """

    # Calcular la diferencia promedio por categoría
    diferencias = dataframe.groupby(columna_categoria)[[columna_previsto, columna_realizado]].apply(
        lambda x: (x[columna_previsto] - x[columna_realizado]).mean()
    ).reset_index(name='Diferencia Promedio')

    return diferencias

# Aplicar la función ajustada
diferencias_promedio = calcular_diferencia_promedio(
    df_datos_brasil, 
    'CATEGORÍA ECONÓMICA', 
    'VALOR PREVISTO ACTUALIZADO', 
    'VALOR REALIZADO'
)

# Mostrar el resultado
diferencias_promedio