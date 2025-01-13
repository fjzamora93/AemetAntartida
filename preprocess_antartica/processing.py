import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os as os
import math

def greet():
    print("Hello, world!")

def acum_prec(df: pd.DataFrame, acumulation: int = 6) -> pd.DataFrame:
    """
    Function to calculate the accumulated precipitation in a given dataframe.
    """
    df = df[['date', 'prec']].copy()
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df_resampled = df.resample(f'{acumulation}H').sum(min_count=1)
    df_resampled.reset_index(inplace=True)
    return df_resampled


def hours_sequential(df, frequency='H'):
    print('Serializando horas')
    df['date'] = pd.to_datetime(df['date'])
    df.drop_duplicates('date', inplace=True)
    full_range = pd.date_range(start=df['date'].min(), end=df['date'].max(), freq=frequency)
    df_full = pd.DataFrame(full_range, columns=['date'])
    df_merged = pd.merge(df_full, df, on='date', how='left')
    count_sequentials = len(df_merged) - len(df)
    print(f"Se han creado {count_sequentials} filas nuevas para completar la secuencia.")
    return df_merged