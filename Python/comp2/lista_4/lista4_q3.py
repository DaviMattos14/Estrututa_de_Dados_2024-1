def expt_ano_de_gasto():
    while True:
        try:
            ano_de_gasto = int(input("Digite o ano que você irá informar os gastos: "))
            return ano_de_gasto
        except ValueError:
            print('\nNão é um número válido, Digite Novamente\n')    

def expt_tipo_de_gasto(gasto_por_ano):
    tipo_gasto = input("Digite a identificação do gasto: ")
    if tipo_gasto in gasto_por_ano.keys():
        print("\nGasto respetido digite novamente\n")
        nova_entrada = input("Digite a identificação do gasto: ")
        return nova_entrada
    else: return tipo_gasto

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