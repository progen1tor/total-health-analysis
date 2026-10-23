import pandas as pd 
import re 
from pathlib import Path 


def df_loader(current: Path =  None) -> pd.DataFrame: 
    '''Функция, находящая исходный датафрейм из любой папки.'''
    current = current if current is not None else Path.cwd()
    for p in current.parents:
        if p.name == 'total-health-analysis':
            return pd.read_csv(p / 'raw' / 'raw.csv')
    raise FileNotFoundError('DataFrame path was not found.')


def date_formatter(dt: str) -> str: 
    '''Функция, приводящая строки даты в единый формат ISO.'''
    if re.match(r'\d{4}-\d{2}-\d{2}', dt):
        return dt 
    if (match := re.search(r'(\d{2})[-/](\d{2})[-/](\d{4})', dt)):
        return f'{match.group(3)}-{match.group(2)}-{match.group(1)}'