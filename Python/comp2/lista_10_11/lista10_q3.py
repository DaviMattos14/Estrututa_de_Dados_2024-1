import numpy as np

count = 0
matriz = np.random.randint(5,51, size=(3,3))
det = np.linalg.det(matriz)

for i in np.greater(matriz,det):
    for j in i:
        if j == True: count+=1

print(count)