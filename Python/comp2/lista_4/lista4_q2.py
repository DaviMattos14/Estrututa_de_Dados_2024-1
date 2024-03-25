'''
Amaral|130|135|190|89|100 
Lannes|120|125|110|90|92
Yan|120|120|150|100|75
Kaio|119|120|125|91|90
'''
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
        voltas = {'Volta 1':int(aux[1]), 'Volta 2':int(aux[2]), 'Volta 3':int(aux[3]), 'Volta 4':int(aux[4]), 'Volta 5':int(aux[5])}
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