import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

print("\n------------------------------------------------- Exibe as 5 primeiras linhas do gráfico ---------------------------------------------------------------\n")
print(penguins.head()) # Exibe as 5 primeiras linhas do gráfico
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n------------------------------------------------- Exibe a quantidade de cada tipo de pinguim -----------------------------------------------------------\n")
a = penguins['species'].value_counts()
print(a) # Exibe a quantidade de cada espécie de pinguim
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n--------------------------------------------------- Exibe a correlação entre as variáveis --------------------------------------------------------------\n")
penguins_numeric = penguins.drop(columns=['species', 'island', 'sex'])
print(penguins_numeric.corr()) # Exibe a correlação entre as variáveis numéricas
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n------------------------------------------------------ Exibe a distribuição dos dados ------------------------------------------------------------------\n")
for col in penguins.drop(columns=['species', 'island', 'sex']):

    sns.barplot(data=penguins, x='species', y=col, errorbar=('ci', 90))
    plt.show() # Exibe o gráfico de barras para cada variável numérica

sns.scatterplot(x= 'body_mass_g', y='flipper_length_mm',hue='species', data=penguins)
plt.show() # Exibe o gráfico de dispersão para a variável 'body_mass_g' e 'flip per_length_mm' agrupado por 'species'

sns.scatterplot(x= 'body_mass_g', y='bill_length_mm',hue='species', data=penguins)
plt.show() # Exibe o gráfico de dispersão para a variável 'body_mass_g' e 'bill _length_mm' agrupado por 'species'

sns.pairplot(data=penguins, hue='species')
plt.show() # Exibe o gráfico de pairplot para as variáveis numéricas agrupado por ' species'
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")