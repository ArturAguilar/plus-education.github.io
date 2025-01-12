import numpy as np
import pandas as pd

planilha = pd.read_csv('arquivo.csv') #coloque o arquivo .csv aqui!
x = planilha.head()

print(x)