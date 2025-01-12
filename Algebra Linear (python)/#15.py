import numpy as np

a = (1, 2, 6)
b = (5, 2, 1)
c = (2, 2, 10)

x = np.abs(np.dot(c, np.cross(a,b)))

print(x)