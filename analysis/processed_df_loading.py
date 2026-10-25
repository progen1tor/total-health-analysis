import sys 
from pathlib import Path 

root = Path.cwd().parent
sys.path.insert(0, str(root))

from src.utils import df_loader
df = df_loader(raw=False)