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

if __name__ == '__main__':
    alunos_calc = ['Davi', 'Julia', 'Marcos', 'Amanda', 'Mariana']
    alunos_fis = ['Davi', 'Marcos', 'Lucas', 'Luana', 'Maria']
    alunos_matriculados(alunos_calc,alunos_fis)