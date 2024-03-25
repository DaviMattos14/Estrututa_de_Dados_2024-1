import numpy as np

matriz = np.array([[3,4],[1,3]])
t_matriz = np.transpose(matriz)

s = True
for i in range(2):
    for j in range(2):
        if matriz[i][j] != t_matriz[i][j]:
            s = False
if s == True:
    print('Eh simetrica')
else: print('Nao eh simetrica')