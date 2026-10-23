import pandas as pd 
import re 
import calendar 
import numpy as np 
from pathlib import Path 
from datetime import date 


def df_loader(current: Path =  None, raw: bool = True) -> pd.DataFrame: 
    '''Функция, находящая нужный датафрейм из любой папки.'''
    current = current if current is not None else Path.cwd()
    for p in current.parents:
        if p.name == 'total-health-analysis':
            filename = 'raw' if raw else 'processed'
            return pd.read_csv(p / 'data' / f'{filename}.csv')
    raise FileNotFoundError('DataFrame path was not found.')


def date_formatter(dt: str) -> str: 
    '''Функция, приводящая строки даты в единый формат ISO.'''
    if re.match(r'\d{4}-\d{2}-\d{2}', dt):
        return dt 
    if (match := re.search(r'(\d{2})[-/](\d{2})[-/](\d{4})', dt)):
        return f'{match.group(3)}-{match.group(2)}-{match.group(1)}'
    

def day_name_getter(dt: date) -> str: 
    '''Получает день недели для переданной даты.'''
    if dt is pd.NaT: 
        return np.nan 
    return calendar.day_name[int(dt.day_of_week)]