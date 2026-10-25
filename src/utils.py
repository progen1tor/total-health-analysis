import pandas as pd 
import re 
import calendar 
import numpy as np 
import src.constants as cn
from pathlib import Path 
from datetime import date 
from matplotlib.axes import Axes 


def df_loader(current: Path =  None, raw: bool = True) -> pd.DataFrame: 
    '''Функция, находящая нужный датафрейм из любой папки.'''
    current = current if current is not None else Path.cwd()
    for p in current.parents:
        if p.name == 'total-health-analysis':
            filename = 'raw' if raw else 'processed'
            return pd.read_csv(p / 'data' / f'{filename}.csv', index_col=0)
    raise FileNotFoundError('DataFrame path was not found.')


def date_formatter(dt: str) -> str: 
    '''Функция, приводящая строки даты в единый формат ISO.'''
    if pd.isna(dt): 
        return np.nan 
    if re.match(r'\d{4}-\d{2}-\d{2}', dt):
        return dt 
    if (match := re.search(r'(\d{2})[-/](\d{2})[-/](\d{4})', dt)):
        return f'{match.group(3)}-{match.group(2)}-{match.group(1)}'
    return np.nan 
    

def day_name_getter(dt: date) -> str: 
    '''Функция, получающая день недели для переданной даты.'''
    if pd.isna(dt): 
        return np.nan 
    return calendar.day_name[int(dt.day_of_week)]


def autopct(pct: float) -> str | None:  
    '''Функция, форматирующая отображение процентов на pie plot.'''
    if pct < 5:
        return None 
    return f'{pct:.1f}%'


def normalize_and_draw_bar(df: pd.DataFrame, ax: Axes) -> None:  
    '''Функция, рисующая барплоты по заданному паттерну.'''
    
    colors = ["#13007C", "#6D0000", "#009425"]
    normal_vals = df.normal_bmi 
    df_norm = df.div(normal_vals, axis=0) 
    
    for i, (label, data) in enumerate(df_norm.T.iterrows()): 
        width = .8 / 3
        offset = (i - (3 - 1) / 2) * width
        x = list(map(lambda n: n + offset, range(len(data.index))))
        ax.bar(
            x=x, height=data, 
            width=width, label=label, color=colors[i]
            )
        
        ax.set_xticks(range(len(data.index)))
        ax.set_ylabel('Доля от нормы', **cn.LABEL_PARAMS)
        ax.legend(labels=['низкий ИМТ', 'высокий ИМТ', 'нормальный ИМТ'], **cn.LEGEND_PARAMS)