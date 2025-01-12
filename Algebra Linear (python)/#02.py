import numpy as np

a= np.array([[1,2,3], [4,5,6], [7,8,9]])
print("Essa é a matriz:\n",a,"\n")

#matriz transposta
trans = a.T
print("essa e a matriz transposta de A: \n" ,trans, "\n")

#matriz inversa
# A matriz original tem que ser quadrada: 3x3
# determinante da original tem que ser diferente de zero
inv= np.linalg.inv(a)
print("Essa e a matriz inversa de A:\n", inv, "\n")

#matriz identidade
ident=np.dot(a,inv)
print("Essa é a matriz identidade:\n" ,ident,"\n")

#ordem da matriz identidade (identity e eye)
i= np.identity(3)
print(i)