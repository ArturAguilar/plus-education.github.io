#transformações lineares parte 2
import numpy as np

#definindo o vetor original
v = np.array([[1], [1]])

# a) rotação
theta = np.pi / 4 # ângulo de rotação em radianos
r = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])
rotated_v = np.dot(r,v)

# b) escalonamento
s = np.array([[2, 0],
              [0, 0.5]])
scaled_v = np.dot(s,v)

# c) reflexão
f = np.array ([[1, 0],
               [0, -1]])
reflected_v = np.dot(f,v)

# d) cisalhamento
h = np.array([[1, 0.5],
              [0, 1]])
sheared_v = np.dot(h,v)

#exibindo os resultados
print("\na) rotação:")
print(rotated_v)
print("\nb) escalonamento:")
print(scaled_v)
print("\nc) reflexão:")
print(reflected_v)
print("\nd) cisalhamento:")
print(sheared_v)