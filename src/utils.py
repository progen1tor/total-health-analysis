from pathlib import Path 


def df_path_finder(current: Path =  None) -> Path: 
    '''Функция, находящая исходный датафрейм из любой папки.'''
    current = current if current is not None else Path.cwd()
    for p in current.parents:
        if p.name == 'total-health-analysis':
            return p / 'raw' / 'raw.csv'
    raise FileNotFoundError('DataFrame path was not found.')