"""
    NOME: Davi dos Santos Mattos DRE: 119133049
    [CONJUNTOS]
"""

"""
    Questão 1)
"""
def penetra(convidados, presentes):
    if ((set(presentes) - set(convidados)) != set()):
        print('Há intruso na festa\n')
    elif (((set(presentes) - set(convidados))) == set()):
        print("Não há penetras\n")

"""
    Questão 2
"""
def homens40(funcionarios, func_M, funcionarios_40):
    total_funcionarios = set(funcionarios)
    mulheres = set(func_M)
    func_40_mais = set(funcionarios_40)
    return (total_funcionarios - mulheres) - func_40_mais

"""
    Questão 3
"""
def mercado(produtos,lista_compra):
    disponiveis = set(produtos)
    lista = set(lista_compra)
    return lista - disponiveis

"""
    Questão 4
"""
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

"""
    Questão 5
"""
def alunos_matriculados(calculo,fisica):
    calc = set(calculo)
    fis = set(fisica)
    print('A)\nAlunos Matriculados: '+ str((calc|fis)) + '\n')
    print('B)\nAlunos cursando ambas as disciplinas: '+str((calc&fis))+'\n')
    print('C)\nAlunos cursando apenas um disciplina\nCálculo:'
    +str((calc-fis))+
    '\nFísica: '
    +str((fis-calc))
    )