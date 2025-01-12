#operações com matrizes
import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([[9,8,7], [6,5,4], [3,2,1]])

# adição de matrizes
x1 = a + b
print("A soma da matriz A e B: \n" , x1 ,"\n")

# subitração de matrizes
x2 = a - b
print("A subtração da matriz A e B: \n" , x2 ,"\n")

# multiplicação de matrizes
x3 = a * b
print("A multiplicação da matriz A e B: \n" , x3 ,"\n")

# NÃO EXISTE DIVISÃO DE MATRIZ