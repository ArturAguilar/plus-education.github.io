import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ler o arquivo CSV
df = pd.read_csv('/home/arturaguilar426/GitHub/projetos/Plus-Education.github.io/Análise Exploratória de Dados (python)/planilhas/winequality-red.csv')

# Mostrar as primeiras linhas do arquivo
print("\n--------------------------------------------------------------- Primeiras Linhas do DataFrame ----------------------------------------------------------\n")
print(df.head())
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Obter e exibir as dimensões do DataFrame
print("\n--------------------------------------------------------------- Dimensões do DataFrame -----------------------------------------------------------------\n")
print(f"O arquivo CSV tem {df.shape[0]} linhas e {df.shape[1]} colunas.")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Obter e exibir os tipos de dados
print("\n------------------------------------------------------------------ Tipos de Dados ----------------------------------------------------------------------\n")
print(df.dtypes)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Exibir informações gerais sobre o DataFrame
print("\n------------------------------------------------------------- Informações do DataFrame -----------------------------------------------------------------\n")
df.info()
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Exibir as estatísticas descritivas do DataFrame
print("\n------------------------------------------------------------ Estatísticas Descritivas ------------------------------------------------------------------\n")
df_desc = df.describe()
print(df_desc)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Calcular e exibir o IQR (Intervalo Interquartil)
print("\n---------------------------------------------------------------- Intervalo Interquartil (IQR) ----------------------------------------------------------\n")
df_desc.loc["IQR"] = df_desc.loc["75%"] - df_desc.loc["25%"]
print(df_desc.loc["IQR"])
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Visualizar a distribuição de cada coluna
print("\n------------------------------------------------------ Distribuição das Variáveis ----------------------------------------------------------------------\n")
for col in df.columns:
    sns.histplot(data=df, x=col, kde=True).set_title(f"Distribuição da variável {col}")
    plt.show()
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Detectar outliers usando o método do quartil
print("\n----------------------------------------------------------------- Detecção de Outliers -----------------------------------------------------------------\n")
for col in df.drop(columns='quality'):  # Excluir a coluna 'quality' da análise
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1

    # Identificar os outliers
    aux_outliers = df[(df[col] < q1 - (1.5 * iqr)) | (df[col] > q3 + (1.5 * iqr))]
    indices_outliers = aux_outliers.index.tolist()

    # Exibir os resultados
    if len(indices_outliers) >= 1:
        print(f"A coluna {col} tem {len(indices_outliers)} outliers!")
        print(f"Os outliers da coluna {col} estão nos índices: {indices_outliers}")
    else:
        print(f"A coluna {col} não tem outliers!")
    print("=" * 80)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Exibir a contagem relativa de valores da coluna 'quality'
print("\n------------------------------------------------------------- Distribuição da Qualidade ----------------------------------------------------------------\n")
quality_counts = df['quality'].value_counts(normalize=True)
print(quality_counts)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Exibir a matriz de correlação
print("\n-------------------------------------------------------------- Matriz de Correlação --------------------------------------------------------------------\n")
correlation_matrix = df.corr()
print(correlation_matrix)

# Visualizar a matriz de correlação como um gráfico de calor
plt.figure(figsize=(12, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title('Matriz de Correlação')
plt.show()
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Exibir a correlação entre as variáveis e a qualidade
print("\n----------------------------------------------------------- Correlação com a Qualidade -----------------------------------------------------------------\n")
quality_correlation = df.corr()['quality'].sort_values()
print(quality_correlation)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Visualizar a distribuição das variáveis por qualidade
print("\n----------------------------------------------------- Distribuição das Variáveis por Qualidade ---------------------------------------------------------\n")
for col in df.drop(columns='quality'):
    sns.barplot(data=df, x='quality', y=col, errorbar=('ci', 90))
    plt.title(f"Distribuição da variável {col} por qualidade")
    plt.show()

# Binarizar a coluna 'quality' (bom ou ruim)
df['quality_bin'] = df['quality'].apply(lambda x: "bom" if x >= 5 else "ruim")
df_bin = df.drop(columns=['quality'])  # Criar um DataFrame sem a coluna 'quality'
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Exibir o DataFrame binarizado
print("\n--------------------------------------------------------------- DataFrame Binarizado -------------------------------------------------------------------\n")
print(df_bin.head())

# Salvar o DataFrame binarizado em um arquivo CSV
output_path = '/home/arturaguilar426/GitHub/projetos/Plus-Education.github.io/Análise Exploratória de Dados (python)/planilhas/winequality-red-binary.csv'
df_bin.to_csv(output_path, index=False)
print(f"\nDataFrame binarizado salvo em: {output_path}")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Exibir informações sobre o DataFrame binarizado
print("\n-------------------------------------------------- Informações do DataFrame Binarizado -----------------------------------------------------------------\n")
df_bin.info()
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

# Visualizar a distribuição das variáveis binarizadas
print("\n-------------------------------------------------- Distribuição das Variáveis Binarizadas --------------------------------------------------------------\n")
for col in df_bin.drop(columns='quality_bin'):
    sns.histplot(data=df_bin, x=col, kde=True, hue='quality_bin').set_title(f"Distribuição da variável {col} por qualidade binarizada")
    plt.show()
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")