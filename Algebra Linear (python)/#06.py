#transformações lineares
import matplotlib.pyplot as plt

#definindo o vetor (2,2)
vetor = [2,2]

#definindo as origens para o vetor
origens = [(0,-1), (0,1), (0,0), (0,2)]

#extraindo as coordenadas x e y das origens
origem_x = [origem[0] for origem in origens]
origem_y = [origem[1] for origem in origens]

#plotando o vetor (2,2) com as origens especificadas
plt.figure()
plt.quiver(origem_x, origem_y, [vetor[0]]*len(origem_x),[vetor[1]]*len(origem_y), angles = 'xy', scale_units = 'xy', scale = 1, color='g')

#configurações adicionais do grafico
plt.xlim(-1,5)
plt.ylim(-2,5)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle = '--', linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable = 'box')
plt.title("Um vetor com diferentes pontos de origem")

#exibindo o gráfico
plt.show()