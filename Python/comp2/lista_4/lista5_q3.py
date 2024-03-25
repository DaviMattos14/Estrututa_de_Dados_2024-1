def mercado(produtos,lista_compra):
    disponiveis = set(produtos)
    lista = set(lista_compra)
    return lista - disponiveis

if __name__ == '__main__':
    lista = ['ovo','queijo','presunto','pão']
    produtos_estoque = ['ovo','queijo','presunto','guaraná','farinha']
    print(mercado(produtos_estoque,lista))