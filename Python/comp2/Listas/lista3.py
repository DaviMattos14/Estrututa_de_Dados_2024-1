"""
    Nome: Davi dos Santos Mattos DRE: 119133049
"""

import datetime as dt

def questao_1(): #Questão 1
    data_atual = dt.datetime.now()

    nomes = open("nomes.txt", "r")
    arquivo = nomes.readlines()

    marte = open('Marte.txt','a+')
    jupiter = open('Jupiter.txt', 'a+')

    for dado in arquivo:
        info = dado.split(', ')

        if data_atual.year - int(info[1]) <= 30 and (info[3] == 'Marte\n' or info[3] == 'Marte'):
            marte.write(info[0]+', '+str((int(info[2])*38)/100)+'\n')
        if data_atual.year - int(info[1]) > 30 and (info[3] == 'Júpiter\n' or info[3] == 'JÃºpiter\n' or info[3] == 'JÃºpiter'):
            jupiter.write(info[0]+', '+str((int(info[2])*264)/100)+'\n')

    nomes.close()
    marte.close()
    jupiter.close()

def media(alunos, notas): # Questão 2
    alunos = open(alunos, 'r')
    notas = open(notas, 'r')
    media = open('Media.txt', 'a+')

    for aluno, nota in zip(alunos, notas):
        aux = nota.split(',')
        n = [float(valor) for valor in aux]
        nome = aluno.strip()
        media.write(nome+' '+str(round(sum(n)/len(n), 1))+'\n')

    alunos.close()
    notas.close()
    media.close()

def questao_3(): # Questão 3
    media = open('Media.txt', 'r')
    for valor in media:
        aux = valor.split(' ')
        aux2 = aux[1].strip()
        if float(aux2) >= 6:
            print(aux[0]+' | '+aux2+' | '+'APROVADO')
        else:
            print(aux[0]+' | '+aux2+' | '+'REPROVADO')

def conta_palavras(arq): # Questão 4
    arquivo = open(arq,'r')
    qtd = 0
    for linha in arquivo:
        palavra = linha.strip()
        palavra = palavra.split(' ')
        qtd += len(palavra)
    print(qtd)
    arquivo.close()

def contagemVotos(arquivo): #Questão 5
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

    print('\n--Questão 1--')
    questao_1() 

    print('\n--Questão 2--')
    media('alunos.txt','notas.txt')
    
    print('\n--Questão 3--')
    questao_3()
    
    print('\n--Questão 4--')
    conta_palavras('texto.txt')
    
    print('\n--Questão 5--')
    contagemVotos('ele2016.txt')