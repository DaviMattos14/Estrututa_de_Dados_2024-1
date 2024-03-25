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
