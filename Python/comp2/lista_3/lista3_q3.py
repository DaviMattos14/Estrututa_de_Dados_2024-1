media = open('Media.txt', 'r')
for valor in media:
    aux = valor.split(' ')
    aux2 = aux[1].strip()
    if float(aux2) >= 6:
        print(aux[0]+' | '+aux2+' | '+'APROVADO')
    else:
        print(aux[0]+' | '+aux2+' | '+'REPROVADO')