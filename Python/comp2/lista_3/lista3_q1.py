import datetime as dt

def questão_1():
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

if __name__ == '__main__':

    questão_1()