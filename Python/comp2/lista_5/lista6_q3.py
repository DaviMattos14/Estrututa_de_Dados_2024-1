import string


def conta_linhas_palavras(arq):
    arquivo = open(arq, 'r+')
    qtd_5_mais = 0
    linhas = 0
    for linha in arquivo:
        linhas += 1
        palavras_linha = linha.strip()
        palavras_linha = palavras_linha.split(' ')
        for palavra in palavras_linha:
            palavra = palavra.translate(
                str.maketrans('', '', string.punctuation))
            if len(palavra) > 5:
                qtd_5_mais += 1
    arquivo.write(
        '\n'*3 + 'Seu arquivo possui {} linhas e {} palavras com mais de 5 caracteres'.format(linhas, qtd_5_mais))


if __name__ == '__main__':
    while True:
        arquivo = input("Digite o nome do arquivo: ")
        try:
            conta_linhas_palavras(arquivo)
        except IOError:
            print("O Arquivo digitado não existe")
        else:
            break