def homens40(funcionarios, func_M, funcionarios_40):
    total_funcionarios = set(funcionarios)
    mulheres = set(func_M)
    func_40_mais = set(funcionarios_40)
    print((total_funcionarios - mulheres) - func_40_mais)


if __name__ == '__main__':
    func = ['Marcos', 'Lucas', 'Mariana', 'Yan', 'Carlos',
            'Larissa', 'Leticia', 'Debora', 'Alana', 'Alan', 'Caio']
    mulheres = ['Mariana', 'Larissa', 'Leticia', 'Debora', 'Alana']
    homens = ['Marcos', 'Alan', 'Carlos', 'Larissa']
    # Lucas, Yan, Caio
    homens40(func, mulheres, homens)
    