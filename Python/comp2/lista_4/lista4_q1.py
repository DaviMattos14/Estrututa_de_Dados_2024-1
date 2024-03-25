def ler_texto(texto):
    palavra_repetidas = {}
    pontuacao = {1: '.', 2: ',', 3: ';', 4: '?', 5: '!', 6: ':'}
    string = ''.join(
        caractere for caractere in texto if caractere not in pontuacao.values())

    aux = string.split()
    for palavra in aux:
        if palavra not in palavra_repetidas:
            palavra_repetidas[palavra] = 1
        elif palavra in palavra_repetidas:
            palavra_repetidas[palavra] += 1
    print(palavra_repetidas)


if __name__ == '__main__':
    txt = '''esclamação! virgula, dois pontos:, ponto e virgula; interrogação? ponto final.'''
    ler_texto(txt)
