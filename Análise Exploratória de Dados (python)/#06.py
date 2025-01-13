import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

candy = pd.read_csv('/home/arturaguilar426/GitHub/projetos/Plus-Education.github.io/Análise Exploratória de Dados/planilhas/candy_production.csv')
a = candy.head(12)
print(a)

candy['observation_date'] = pd.to_datetime(candy['observation_date'])
b = candy.info()
print(b)

candy.plot(x='observation_date', y='industrial_production')
plt.title('Produção Industrial de Doces')
plt.show()

candy_filtered = candy[candy['observation_date'] >= '2010-01-01']
ax = candy_filtered.plot(x='observation_date', y='industrial_production', figsize=(12, 6))
plt.show()

ax = candy_filtered.plot(x='observation_date', y='industrial_production', figsize=(12, 6))
xcoords = ['2011-01-01', '2012-01-01', '2013-01-01', '2014-01-01','2015-01-01', '2016-01-01','2017-01-01']

for xc in xcoords:
    plt.axvline(x=xc ,color='black', linestyle='--')
plt.show()


from statsmodels.tsa.seasonal import seasonal_decompose

#candy_filtered.set_index('observation_date', inplace=True)

analysis = candy_filtered[['industrial_production']].copy()

decompose_result = seasonal_decompose(analysis, model='multiplicative')

trend = decompose_result.trend
seasonal = decompose_result.seasonal
residual = decompose_result.resid

decompose_result.plot()