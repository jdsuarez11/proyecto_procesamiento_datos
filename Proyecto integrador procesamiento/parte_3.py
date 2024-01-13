from datasets import load_dataset
import numpy as np
import pandas as pd

# Importar los datos
dataset = load_dataset("mstz/heart_failure")
data = dataset['train']

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Revisar los tipos de dato de cada columna
print(df.dtypes)

# Calcular la cantidad de hombres fumadores vs mujeres fumadoras (usando agregaciones en Pandas).
filtro_fumadores = df['is_smoker'] == True # Solo conserva los fumadores de df
solo_fumadores = df[filtro_fumadores] # aplica el filtro a df y crea un DataFrame nuevo llamado solo_fumadores
solo_fumadores = solo_fumadores[['is_male', 'is_smoker']] # Conserva unicamente las columnas que nos interesan
print(solo_fumadores.groupby('is_male').count()) # Imprime el resultado