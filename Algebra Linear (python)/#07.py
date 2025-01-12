import matplotlib.pyplot as plt

#definindo o vetor na base canônica
vetor_x = [1,0] #vetor unitário ao longo do eixo x
vetor_y = [0,1] #vetor unitário ao longo do eixo y

#plotando  vetor na base canônico
plt.figure()
plt.quiver(0,0, vetor_x[0], vetor_x[1], angles='xy', scale_units='xy', scale=1, color='r', label='eixo x')
plt.quiver(0,0, vetor_y[0], vetor_y[1], angles='xy', scale_units='xy', scale=1, color='b', label='eixo y')

#configurações adicionais do gráfico
plt.xlim(-1,1)
plt.ylim(-1.1)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Base Canônonica")

#exibindo o gráfico
plt.show()