if __name__ == '__main__':
    numero = 0
    numeros_digitados = []
    while numero >= 0:
        numero = int(input())
        if numero < 0:
            break
        else:
            numeros_digitados.append(numero)
    numeros_digitados.sort()
    conjunto = set(numeros_digitados)
    print(conjunto)
