import numpy as np


x = np.empty((3,3), dtype='i')
y = np.empty((3,3), dtype='i')

for i in range(3):
    for j in range(3):
        x[i][j] = int(input(f"Digite um número para posição [{i}][{j}] da primeira matriz: "))
print('\n'*2)
for i in range(3):
    for j in range(3):
        y[i][j] = int(input(f"Digite um número para posição [{i}][{j}] da segunda matriz: "))
print('\n'*2)

soma = np.add(x,y)

print(soma)