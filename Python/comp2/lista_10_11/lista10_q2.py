import numpy as np
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