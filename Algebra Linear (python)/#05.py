#sistemas lineares
import numpy as np

#defininimos a matriz A é o vetor b
a = np.array([[1,2,3], [2,3,3], [1,2,0]])
b = np.array([1,-3,6])

#calculamos o inverso de A
inv_a = np.linalg.inv(a)

#resolvendo o sistema de equações lineares
x = np.dot(inv_a, b)

print("\nA solução usando a matriz inversa é x =", x)

#resolvendo o sistema de equaçÕes lineares diretamente
x_solve = np.linalg.solve(a,b)

print("\nA solução usando o solve é:",x_solve)

