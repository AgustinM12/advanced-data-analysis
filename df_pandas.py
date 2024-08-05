import pandas as pd

# Leer el archivo CSV en un DataFrame
def read_csv(csv):
    df = pd.read_csv(csv)
    return df


