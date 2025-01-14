import pandas as pd
import numpy as np

houses_to_rent = pd.read_csv('/home/arturaguilar426/GitHub/projetos/Plus-Education.github.io/Análise Exploratória de Dados (python)/planilhas/houses_to_rent.csv') # Ler o arquivo CSV

print("\n--------------------------------------------------------- Exebição do Gráfico: -------------------------------------------------------------------------\n")
a = houses_to_rent.head()
print(a)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n--------------------------------------------------------- Exebição das Estatísticas Descritivas: -------------------------------------------------------\n")
b = houses_to_rent.describe()
print(b) # Mostrar as estatísticas descritivas da planilha
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n--------------------------------------------------------- Exebição da Contagem de Dados: ---------------------------------------------------------------\n")
c = houses_to_rent['bathroom'].value_counts()
print(c) # Mostrar a contagem de cada valor na coluna 'bathroom' da planilha
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")


## IQR -> distancia inter quartil
q1 = houses_to_rent['bathroom'].quantile(0.25) # primeiro quartil
q3 = houses_to_rent['bathroom'].quantile(0.75) # terceiro quartil

print("\n------------------------------------------------------------ Exebição do IQR: --------------------------------------------------------------------------\n")
iqr = q3 - q1 # IQR
print("IQR:",iqr)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n---------------------------------------------------- Exebição dos Outliers e Inliers: ------------------------------------------------------------------\n")
houses_outliers = houses_to_rent[(houses_to_rent['bathroom'] < q1 - (iqr * 1.5)) | (houses_to_rent['bathroom'] > q3 + (iqr * 1.5))]
print("resultado do outlier:\n", houses_outliers) # Mostrar os outliers da coluna 'bathroom' da planilha

houses_inliers = houses_to_rent[(houses_to_rent['bathroom'] >= q1 - (iqr * 1.5)) | (houses_to_rent['bathroom'] <= q3 + (iqr * 1.5))]
print("\nresultado do inlier:\n", houses_inliers) # Mostrar os inliers da coluna 'bathroom' da planilha
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")