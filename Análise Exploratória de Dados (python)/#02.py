import numpy as np
import pandas as pd

cuisine_rating = pd.read_csv('/home/arturaguilar426/GitHub/projetos/Plus-Education.github.io/Análise Exploratória de Dados/planilhas/Cuisine_rating.csv') # Ler o arquivo CSV

print("\n--------------------------------------------------------- Exebição do Gráfico: -------------------------------------------------------------------------\n")
a = cuisine_rating.head()
print(a)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n--------------------------------------------------------- Exebição EstatÍstica: ------------------------------------------------------------------------\n")
b = cuisine_rating.describe()
print(b) # mostra as estatísticas da planilhA
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n--------------------------------------------------------- Frequência dos dados: ------------------------------------------------------------------------\n")
c = cuisine_rating['Location'].value_counts()
print(c) # mostra a contagem de cada localização
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")


numeric_cols = cuisine_rating.select_dtypes(include= np.number).columns.to_list()

print("\n--------------------------------------------------------- Média das Localizações: ----------------------------------------------------------------------\n")
d = cuisine_rating.groupby(['Location'])[numeric_cols].mean()
print(d) # mostra a média de cada localização para as colunas numéricas
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n--------------------------------------------------------- Média das Localizações e Tipos de Comida: ----------------------------------------------------\n")
e = cuisine_rating.groupby(['Location', 'Cuisines'])[numeric_cols].mean()
print(e) # mostra a média de cada localização e tipo de comida para as colunas
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

