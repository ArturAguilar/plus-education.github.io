import numpy as np

#definindo a matriz A
A = np.array([[6, -1], 
              [2, 3]])

#calculando os autovalores e autovetores
autovalores, autovetores = np.linalg.eig(A)

#criando a matriz diaginal com os autovalores
matriz_diagonal = np.diag(autovalores)

#imprimindo
print("\nAutovalores:")
print(autovalores)
print("\nAutovetores:")
print(autovetores)

print("\nMatriz diagonal:\n" , matriz_diagonal)

##BONUS - reconstruindo a matriz
#verificando a decomposição espectral

reconstruida = autovetores @ matriz_diagonal @ np.linalg.inv(autovetores)
print("\nMatriz original:\n" , reconstruida)
