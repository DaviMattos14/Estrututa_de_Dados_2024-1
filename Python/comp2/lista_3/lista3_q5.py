def contagemVotos(arquivo):
    arq = open(arquivo,'r')
    lista_ordenada = []
    for linha in arq:
        candidato = linha.strip()
        candidato = candidato.split('; ')
        candidato[2] = int(candidato[2])
        lista_ordenada.append(candidato)
    lista_ordenada = sorted(lista_ordenada, key=lambda votos: votos[2], reverse=True)
    print('1º: {}\n2º: {}'.format(lista_ordenada[0][0],lista_ordenada[1][0]))

if __name__ == '__main__':
    contagemVotos('ele2016.txt')