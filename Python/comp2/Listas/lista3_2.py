"""
    NOME: Davi dos Santos Mattos DRE: 119133049
    [DICIONÁRIOS]
"""

"""
    Questão 1)
"""
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

"""
    Questão 2)
"""
import time
if __name__ == '__main__':
    corredores = {}
    corredor_melhor_volta = ''
    corredor_vencendor = ''
    tempo_melhor_volta = 9000000
    tempo_vencedor = 99999999
    while len(corredores) < 4:
        string = input(str())
        aux = string.split('|')
        voltas = {'Volta 1':int(aux[1]), 'Volta 2':int(aux[2]), 'Volta 3':int(aux[3]), 
        'Volta 4':int(aux[4]), 'Volta 5':int(aux[5])}
        
        corredores.update({aux[0]: voltas})
        
        if sum(voltas.values()) < tempo_vencedor:
            tempo_vencedor = sum(voltas.values())
            corredor_vencendor = aux[0]
        if min(voltas.values()) < tempo_melhor_volta:
            tempo_melhor_volta = min(voltas.values())
            corredor_melhor_volta = aux[0]

print('\n'+str(time.strftime("%M:%S", time.gmtime(tempo_melhor_volta)))+' - '+ str(corredor_melhor_volta)+' | ' +
str(list(corredores[corredor_melhor_volta].keys())[list(corredores[corredor_melhor_volta].values()).index(tempo_melhor_volta)])
)
print('\n'+str(time.strftime("%M:%S", time.gmtime(tempo_vencedor)))+' - '+ str(corredor_vencendor))

"""
    Questão 3)
"""

# Recebendo o Ano dos gastos e tratando exceção
def expt_ano_de_gasto():
    while True:
        try:
            ano_de_gasto = int(input("Digite o ano que você irá informar os gastos: "))
            return ano_de_gasto
        except ValueError:
            print('\nNão é um número válido, Digite Novamente\n')    

# Evitando que o usuário digite o mesmo gasto mais de uma vez
def expt_tipo_de_gasto(gasto_por_ano):
    tipo_gasto = input("Digite a identificação do gasto: ")
    if tipo_gasto in gasto_por_ano.keys():
        print("\nGasto respetido digite novamente\n")
        nova_entrada = input("Digite a identificação do gasto: ")
        return nova_entrada
    else: return tipo_gasto

# Recebendo o valor do gasto e tratando exceção
def expt_valor_de_gasto():
    while True:
        try:
            valor_gasto = float(input("Digite o valor gasto de {} em {}: ".format(tipo_gasto, ano_de_gasto)))
            return valor_gasto
        except ValueError:
            print('\nNão é um número válido, Digite Novamente\n') 

if __name__ == '__main__':

    gastos = {}
    gastos_por_ano = {}

    ano_de_gasto = expt_ano_de_gasto()
    while True:

        tipo_gasto = expt_tipo_de_gasto(gastos_por_ano)

        if tipo_gasto == 'fim' or tipo_gasto == 'Fim':
            gastos.update({ano_de_gasto: gastos_por_ano})
            break

        elif tipo_gasto == 'próximo' or tipo_gasto == 'Próximo' or tipo_gasto == 'proximo':
            gastos.update({ano_de_gasto: gastos_por_ano})
            gastos_por_ano = {}
            ano_de_gasto = expt_ano_de_gasto()
            tipo_gasto = input("Digite a identificação do gasto: ")

        valor_gasto = expt_valor_de_gasto()
        gastos_por_ano.update({tipo_gasto: valor_gasto})


    print("\nO relatório a seguir considera o período de {} a {} ({} anos)".format(list(gastos.keys())[0],
                                                                            list(gastos.keys())[len(list(gastos.keys()))-1],
                                                                            len(list(gastos))
    ))

gasto_total = {}
for ano in gastos:
    for t_gasto in gastos[ano]:
        if t_gasto in gasto_total:
            gasto_total.update({t_gasto:gasto_total[t_gasto]+gastos[ano][t_gasto]})
        elif t_gasto not in gasto_total:
            gasto_total.update({t_gasto:gastos[ano][t_gasto]})

for tipo_gasto in gasto_total:
    print('Total gasto de {}: R${:.2f}'.format(tipo_gasto,gasto_total[tipo_gasto]))
    print('Média de gasto com {}: R${:.2f}'.format(tipo_gasto,(gasto_total[tipo_gasto]/len(gastos))))


valor_total_gasto = 0
for ano in gastos:
    valor_no_ano = sum(list(gastos[ano].values()))
    valor_total_gasto += sum(list(gastos[ano].values()))
    print('Total gasto em {}: R$ {:.2f}'.format(ano,valor_no_ano))
print('Média de gasto no período: R${:.2f}'.format(valor_total_gasto/len(gastos)))


"""
    Questão 4)
"""
from os import system

class Aluno:
    def __init__(self, matricula, nome, notas={}):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas


listagem = {}

if __name__ == '__main__':
    opcoes = {'a)': 'Incluir aluno',
              'b)': 'Excluir aluno',
              'c)': 'Listagem geral',
              'd)': 'Troca de nota',
              'e)': 'Fim'
              }

while True:
    for i in opcoes:
        print('{} {}'.format(i, opcoes[i]))
    entrada = input("\nDigite a opcao: ")

    # e) Fim
    if (entrada == list(opcoes)[4]) or entrada == list(opcoes.values())[4]:
        break

    # d) Trocar Nota
    if (entrada == list(opcoes)[3]) or entrada == list(opcoes.values())[3]:
        matricula = int(input("Digite a Matricula: "))
        prova = input("Digite a nota que deseja alterar: ")
        nota = float(input("Digite a nova nota: "))
        listagem[matricula]['Notas'].update({prova: nota})  # error
        system('cls') or None

    # c) Listagem Geral
    if (entrada == list(opcoes)[2]) or entrada == list(opcoes.values())[2]:
        for aluno in listagem:
            print(listagem[aluno])
        print('\n')

    # b) Excluir aluno
    if (entrada == list(opcoes)[1]) or entrada == list(opcoes.values())[1]:
        matricula = int(input("Digite a Matricula: "))
        listagem.pop(matricula)
        system('cls') or None

    # Incluir Aluno
    if (entrada == list(opcoes)[0]) or (entrada == list(opcoes.values())[0]):
        matricula = int(input("Digite a Matricula: "))
        nome = input("Digite o Nome: ")
        p1 = float(input("Digite a nota da P1: "))
        p2 = float(input("Digite a nota da P2: "))
        p3 = float(input("Digite a nota da P3: "))
        aluno = Aluno(matricula, nome, {'P1': p1, 'P2': p2, 'P3': p3})
        listagem.update({matricula: {'Matricula': aluno.matricula,
                        'Nome': aluno.nome, 'Notas': aluno.notas}})
        system('cls') or None

    # Erro de entrada
    elif (entrada not in list(opcoes and list(opcoes.values()))):
        print('\nOpção digitada errada, digite novamente\n')
