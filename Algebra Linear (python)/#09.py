import numpy as np
import matplotlib.pyplot as plt

#definido  vetor original
v = np.array([1, 1])

#definindo as tranformações
theta = np.pi / 4 # ângulo de rotação em radianos
tranformations = [
    ("rotação" , np.array([[np.cos(theta), -np.sin(theta)],
                           [np.sin(theta), np.cos(theta)]])),
    
    ("escalonamento", np.array([[2, 0], 
                                [0, 0.5]])), 

    ("reflexão" , np.array([[1, 0],
                            [0, -1]])),

    ("cisalhamento" , np.array([[1, 0.5],
                                [0, 1]]))
]

for i, (name, T) in enumerate(tranformations, start=1):
    plt.subplot(2, 2, i)
    plt.title(name)
    transformed_v = np.dot(T, v)
    plt.quiver([0, 0], [0, 0], [v[0], transformed_v[0]], [v[1], transformed_v[1]], angles='xy', scale_units='xy', scale=1, color='blue')
    plt.xlim(-2, 3)
    plt.ylim(-2, 3)
    plt.grid(True)

    plt.tight_layout()
    plt.show()