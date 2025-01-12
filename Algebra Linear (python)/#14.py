import numpy as np

#base canonica
e1 = np.array([1, 0])
e2 = np.array([0, 1])

#componentes dos vetores
v1, v2 = np.array([1, 3])
w1, w2 = np.array([2, -1])

#vetores expandidos na base canonica
v = v1*e1 + v2*e2
w = w1*e1 + w2*e2

#produto escalar, diretamente
x = (v*w).sum()
print(x)

#produto escalar, com a função np.dot()
z = np.dot(v, w)
print(z)