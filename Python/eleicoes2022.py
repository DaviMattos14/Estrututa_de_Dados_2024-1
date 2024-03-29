import requests
import os

os.system('cls') or None

PRES = 'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json'
GOV = 'https://resultados.tse.jus.br/oficial/ele2022/546/dados-simplificados/rj/rj-c0003-e000546-r.json'
resultado_pres = requests.get(PRES).json()
resultado_gov = requests.get(GOV).json()

tabela_pres = sorted([
    (candidate['nm'], candidate['vap'], candidate['pvap'])
    for candidate in resultado_pres['cand']
], key=lambda linha: (linha[2], linha[0]), reverse=True)  # Ordena por porcentagem


tabela_gov = sorted([
    (candidate['nm'], candidate['vap'], candidate['pvap'])
    for candidate in resultado_gov['cand']
], key=lambda linha: (linha[0:9][2]), reverse=True)  # Ordena por porcentagem


print('Nome\tVotos\tPorcentagem')
for linha in tabela_pres:
    print('\t'.join(linha))

'''
print('\nNome\tVotos\tPorcentagem')
for linha in tabela_gov:
    print('\t'.join(linha))
'''

"""
def porcentagem(lista):
    coluna = []
    for i in range(len(resultado_gov)):
        coluna.append(resultado_gov[i][2])
    return coluna
"""
