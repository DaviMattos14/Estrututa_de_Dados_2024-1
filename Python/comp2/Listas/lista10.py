'''
    Nome: Davi dos Santos Mattos    DRE: 119133049
'''
import numpy as np

"""
    QUESTÃO 1
"""
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


"""
    QUESTÃO 2
"""
def produto_Matriz(arq):
    arquivo = open(arq,'r')
    lista = []
    for linha in arquivo:
        nova_linha = linha[3:]
        valores = nova_linha.strip()
        valores = valores.removesuffix('.')
        valores = valores.split(';')
        lista.append(valores)
    m1 = np.array(lista[0], dtype='i').reshape(2,2)
    m2 = np.array(lista[1], dtype='i').reshape(2,2)
    pMatrix = np.multiply(np.linalg.inv(m1), np.linalg.inv(m2))
    print(pMatrix)

if __name__ == '__main__':
    produto_Matriz('matrizes.txt')

"""
    QUESTÃO 3
"""
count = 0
matriz = np.random.randint(5,51, size=(3,3))
det = np.linalg.det(matriz)

for i in np.greater(matriz,det):
    for j in i:
        if j == True: count+=1

print(count)

"""
    QUESTÃO 4
"""
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

"""
    QUESTÃO 5
"""

A = np.array([4,1,-2,-3,2,1,2,1,-1]).reshape(3,3)
b = np.array([5,3,8])
x = np.linalg.inv(A).dot(b)

print(x)

"""
    QUESTÃO 6
"""
graus = (40*np.pi)/180
base = 8/np.tan(graus)
area = round((base*8)/2,4)
print(area)