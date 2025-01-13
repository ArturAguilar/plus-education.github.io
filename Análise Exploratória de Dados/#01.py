import pandas as pd

planilha = pd.read_csv('Cuisine_rating.csv') #coloque o arquivo .csv aqui!
a = planilha.head()
print(a)

b = planilha.info() #informações sobre a planilha
print(b)

c = planilha['Cuisines'].value_counts() #contagem da frequência de cada valor na coluna
print(c)

d = planilha[planilha['Cuisines'] == 'Japanese'] #filtrar a planilha para mostrar apenas as linhas que atendem a condição 
print(d)

e = planilha[planilha['Cuisines'] == 'Japanese']['Overall Rating'].mean() #calcular a média de uma coluna

