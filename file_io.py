import pandas as pd

def load_csv(file_path):
    df = pd.read_csv(file_path)
    print(f'Cargados {df.shape[0]} books') #shape[0] devuelve filas/ 1 columnas
    return df