import pandas as pd

df = pd.read_csv('salida.csv')

def limpieza_datos(df: pd.DataFrame):
    print("Valores faltantes por columna:")
    print(df.isnull().sum()) # 1. Verificar que no existan valores faltantes
    print(f"Hay {df.duplicated().sum()} filas repetidas") # 2. Verificar que no existan filas repetidas
    # 3. Verificar si existen valores atípicos y eliminarlos
    q1 = df['creatinine_phosphokinase'].quantile(0.25)
    q3 = df['creatinine_phosphokinase'].quantile(0.75)
    iqr = q3 -q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df = df[(df['creatinine_phosphokinase'] >= lower_bound) & (df['creatinine_phosphokinase'] <= upper_bound)]
    age_bins = [0, 12, 19, 39, 59, float('inf')]
    age_labels = ['0-12: Niño', '13-19: Adolescente', '20-39: Jóvenes adulto', '40-59: Adulto', '60+: Adulto mayor']
    # Create a new column 'AgeGroup' based on the 'Age' column
    df['AgeGroup'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
    df.to_csv('datos_procesados.csv')
    return df

limpieza_datos(df)
