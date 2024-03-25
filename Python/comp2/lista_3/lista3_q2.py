def media(alunos, notas):
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


if __name__ == '__main__':
    media('alunos.txt','notas.txt')