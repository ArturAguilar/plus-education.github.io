import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D

# Definindo as coordenadas do quadrado original
square = np.array([[0, 1, 1, 0, 0],
                   [0, 0, 1, 1, 0]])

# Função para plotar o quadrado
def plot_square(ax, square, color, label):
    ax.plot(square[0], square[1], color=color, label=label)

# Criando a figura
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
plt.subplots_adjust(hspace=0.5)

# Definindo as transformações
transformations = [
    ("Rotação", Affine2D().rotate_deg(45)),
    ("Escalonamento", Affine2D().scale(2, 0.5)),
    ("Reflexão", Affine2D().scale(1, -1)),
    ("Cisalhamento", Affine2D().skew_deg(45, 0))
]

# Aplicando as transformações e plotando o quadrado
for i, (name, transformation) in enumerate(transformations):
    ax = axs.flatten()[i]
    transformed_square = transformation.transform(square.T).T
    plot_square(ax, transformed_square, color='blue', label='Transformado')
    plot_square(ax, square, color='red', label='Original')
    ax.set_title(name)
    ax.set_xlim(-2, 3)
    ax.set_ylim(-2, 3)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.legend()

# Exibindo o gráfico
plt.show()