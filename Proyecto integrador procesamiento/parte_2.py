from datasets import load_dataset
import numpy as np
import pandas as pd

# Importar los datos
dataset = load_dataset("mstz/heart_failure")
data = dataset['train']

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Filtrar el DataFrame con las personas que fallecieron
filtro_fallecidos = df['is_dead'] == 1
fallecidos = df[filtro_fallecidos]

# Filtrar el DataFrame con las personas que no fallecieron
filtro_no_fallecidos = df['is_dead'] != 1
no_fallecidos = df[filtro_no_fallecidos]

# Calcular el promedio de edad de ambos grupos e imprimir los resultados
print(f"Edad promedio de los fallecidos:", fallecidos['age'].mean().round(decimals=2))
print(f"Edad promedio de los que no fallecieron:", no_fallecidos['age'].mean().round(decimals=2))