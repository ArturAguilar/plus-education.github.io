import numpy as np
import matplotlib.pyplot as plt

#definido  vetor original
v = np.array([1, 1])

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

#plotando os vetores
plt.figure(figsize=(10, 8))

#original
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original')

#rotação
plt.quiver(0, 0, rotated_v[0], rotated_v[1], angles='xy', scale_units='xy', scale=1, color='red', label='Rotação')

#escalonamento
plt.quiver(0, 0, scaled_v[0], scaled_v[1], angles='xy', scale_units='xy', scale=1, color='green', label='Escalonamento')

#reflexão
plt.quiver(0, 0, reflected_v[0], reflected_v[1], angles='xy', scale_units='xy', scale=1, color='yellow', label='Reflexão')

#cisilhamento
plt.quiver(0, 0, sheared_v[0], sheared_v[1], angles='xy', scale_units='xy', scale=1, color='purple', label='Cisalhamento')

plt.xlim(-1, 3)
plt.ylim(-1, 3)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth = 0.5)
plt.axvline(0, color='black', linewidth = 0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()