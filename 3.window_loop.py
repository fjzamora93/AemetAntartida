import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os as os
import math


path = './data/'

for dirpath, dirnames, filenames in os.walk(path):
    print(f'Found directory: {dirpath}')
    for dirname in dirnames:
        station = dirname.split('_')[1]
        input_path = f'{station}_clean.csv'
        
        try:
            df = pd.read_csv(path + dirname + '/'  + input_path)
            df.head()
            print(f'Nombre de la estación: {input_path}')
        except Exception as e:
            print(f'Error: {e}')
            continue

                
        window_size = 365 * 24  
        nulls_tolerance = 15 * 24 # 2 semanas horario
        value_counts = pd.DataFrame()

        #Nos saltamos la columna de fecha e identificacion de la base
        for col in df.columns:
            if df[col].dtype != np.float64 and df[col].dtype != np.int64:        
                print(f'{col} is not a number')
                continue
            print(f'{col} is a number')
            df[f'{col}_{station}'] = df[col].rolling(window=window_size, min_periods=1).apply(
                lambda x: 0 if x.isnull().sum() > nulls_tolerance or len(x) < window_size else 1
            )
            df[f'{col}_{station}'] = df[f'{col}_{station}'].replace({np.nan: 0})
            df[f'{col}_{station}'] = df[f'{col}_{station}'].astype(np.int8)

            value_counts[col] = df[f'{col}_{station}'].value_counts().reindex([0, 1], fill_value=0)
