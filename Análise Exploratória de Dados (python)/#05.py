import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

print("\n-------------------------------------------- Exebição da Quantidade de Espécies de cada flor -----------------------------------------------------------\n")
a = iris['species'].value_counts()
print(a) # Exibe a quantidade de cada espécie de flor
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n----------------------------------------- Exebição das 5 primeiras linhas do conjunto de dados: --------------------------------------------------------\n")
b = iris.head()
print(b) # Exibe as primeiras espécies de flor
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n-------------------------------------------- Exebição da Distribuição da Variável sepal_length  --------------------------------------------------------\n")
col = 'sepal_length'
for col in iris.drop(columns='species'):
    sns.histplot(data=iris, x=col, kde=True).set_title(f'Distribuição da variável {col}')
    plt.show() # Exibe a distribuição da variável sepal_length
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n----------------------------------------------------- Exebição da Descrição dos Dados ------------------------------------------------------------------\n")
d = iris.describe()
print(d) # Exibe a descrição dos dados
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n-------------------------------------------- Exebição da Distribuição da Variável sepal_length  --------------------------------------------------------\n")
for col in iris.drop(columns='species'):
    sns.histplot(data=iris, x=col, kde=True, hue=iris["species"]).set_title(f'Distribuição da variável {col}')
    plt.show() # Exibe a distribuição da variável sepal_length
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n-------------------------------------------- Exebição da Correlação entre as Variáveis ---------------------------------------------------------------\n")
for col in iris.drop(columns='species'):
    sns.barplot(data=iris, x=iris['species'], hue=iris["species"], y = col, ci = 90)
    plt.show() # Exibe a correlação entre as variáveis
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")