import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

candy = pd.read_csv('/home/arturaguilar426/GitHub/projetos/Plus-Education.github.io/Análise Exploratória de Dados (python)/planilhas/candy_production.csv')

print("\n------------------------------------------------------- Exebição da Tabela: ----------------------------------------------------------------------------\n")
a = candy.head(12)
print(a) # Mostra as primeiras 12 linhas da tabela
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n----------------------------------------------------------------- Informações da Tabela: ---------------------------------------------------------------\n")
candy['observation_date'] = pd.to_datetime(candy['observation_date'])
b = candy.info()
print(b) # Mostra informações sobre a tabela
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("\n--------------------------------------------------------------- Amostra do Gráfico: --------------------------------------------------------------------\n")
candy.plot(x='observation_date', y='industrial_production')
plt.title('Produção Industrial de Doces')
plt.show() # Mostra o gráfico

candy_filtered = candy[candy['observation_date'] >= '2010-01-01']
ax = candy_filtered.plot(x='observation_date', y='industrial_production', figsize=(12, 6))
plt.show() # Mostra o gráfico

ax = candy_filtered.plot(x='observation_date', y='industrial_production', figsize=(12, 6))
xcoords = ['2011-01-01', '2012-01-01', '2013-01-01', '2014-01-01','2015-01-01', '2016-01-01','2017-01-01']

for xc in xcoords:
    plt.axvline(x=xc ,color='black', linestyle='--')
plt.show() # Mostra o gráfico


from statsmodels.tsa.seasonal import seasonal_decompose

#candy_filtered.set_index('observation_date', inplace=True)

analysis = candy_filtered['industrial_production']

decompose_result = seasonal_decompose(analysis, model='multiplicative')

trend = decompose_result.trend
seasonal = decompose_result.seasonal
residual = decompose_result.resid

decompose_result.plot() # Mostra o gráfico
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")