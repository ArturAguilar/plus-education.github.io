#criando uma matriz aleatória
import numpy as np

a= np.random.randint(0, 10, size=(5,5))
x1= np.linalg.det(a)
print("\nEssa é a matriz aleatória de tamanho 5x5:\n",a, "\n\nEsse é o determinante da matriz acima: ",x1, "\n") 

b=np.random.randint(0, 10, size=(3,4))
x2= np.linalg.det(b)
print(b,x2) #Não se calcula o determinate de uma matriz que não é quadrada (ou seja, que tem o númeroo de linhas diferente do numeros de colunas)