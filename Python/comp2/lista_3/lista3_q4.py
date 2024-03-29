
def conta_palavras(arq):
    arquivo = open(arq,'r')
    qtd = 0
    for linha in arquivo:
        palavra = linha.strip()
        palavra = palavra.split(' ')
        qtd += len(palavra)
    print(qtd)
    arquivo.close()

if __name__ == '__main__':
    conta_palavras('texto.txt')