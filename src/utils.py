import pandas as pd 
from pathlib import Path 


def df_loader(current: Path =  None) -> pd.DataFrame: 
    '''Функция, находящая исходный датафрейм из любой папки.'''
    current = current if current is not None else Path.cwd()
    for p in current.parents:
        if p.name == 'total-health-analysis':
            return pd.read_csv(p / 'raw' / 'raw.csv')
    raise FileNotFoundError('DataFrame path was not found.')