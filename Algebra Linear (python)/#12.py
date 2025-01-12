import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Função para plotar um cubo
def plot_cube(ax, vertices, color, alpha=0.7):
    # Definindo as faces do cubo
    faces = [
        [vertices[j] for j in [0, 1, 2, 3]],  # Face inferior
        [vertices[j] for j in [4, 5, 6, 7]],  # Face superior
        [vertices[j] for j in [0, 1, 5, 4]],  # Face frontal
        [vertices[j] for j in [2, 3, 7, 6]],  # Face traseira
        [vertices[j] for j in [1, 2, 6, 5]],  # Face direita
        [vertices[j] for j in [0, 3, 7, 4]]   # Face esquerda
    ]

    # Criando as faces como polígonos 3D
    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='black', alpha=alpha))

# Criando a figura e o subplot 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Definindo os vértices do cubo original
vertices_original = np.array([
    [0, 0, 0],  # Vértice 0
    [1, 0, 0],  # Vértice 1
    [1, 1, 0],  # Vértice 2
    [0, 1, 0],  # Vértice 3
    [0, 0, 1],  # Vértice 4
    [1, 0, 1],  # Vértice 5
    [1, 1, 1],  # Vértice 6
    [0, 1, 1]   # Vértice 7
])

# Plotando o cubo original
plot_cube(ax, vertices_original, color='cyan')

# Aplicando uma rotação ao cubo
theta = np.pi / 4  # Ângulo de rotação (45 graus)
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])

# Calculando os vértices do cubo rotacionado
vertices_rotated = np.dot(vertices_original, rotation_matrix.T)

# Plotando o cubo rotacionado
plot_cube(ax, vertices_rotated, color='orange', alpha=0.5)

# Ajustando os limites do gráfico
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)
ax.set_zlim(-1, 2)

# Configurando os rótulos dos eixos
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Exibindo o gráfico
plt.show()