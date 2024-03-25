def penetra(convidados, presentes):
    if ((set(presentes) - set(convidados)) != set()):
        print('Há intruso na festa\n')
    elif (((set(presentes) - set(convidados))) == set()):
        print("Não há penetras\n")

if __name__ == '__main__':
    penetra(['Lannes', 'Yan', 'Marcos'], ['Lannes', 'Yan', 'Marcos'])
    penetra(['Lannes', 'Yan', 'Marcos'], [
            'Lannes', 'Amaral', 'Gustavo', 'Yan', 'Marcos'])
