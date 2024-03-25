"""
    NOME: Davi dos Santos Mattos DRE: 119133049
"""
import time

class Caderno:
    def __init__(self, caderno=[]):
        '''
        Método construtor que cria os atributos 'caderno' e 'totalPaginas', 
        sendo uma lista e um inteiro, respectivamente
        '''
        self.carderno = caderno
        self.totalPaginas = len(self.carderno)

    def NovaFolha(self):
        '''
        Adiciona automaticamente uma lista vazia dentro de outra lista
        '''
        folha = []
        self.carderno.append(folha)
        self.totalPaginas += 1

    def RasgarFolha(self):  # list → list
        '''
        Remove a última lista (Página/Folha) da lista caderno
        '''
        print(self.carderno[len(self.carderno)-1])
        self.carderno.pop(len(self.carderno)-1)

    def Escrever(self, folha, texto):  # int, str → list
        '''
        Adiciona uma linha de texto dentro de uma página
        '''
        self.carderno[folha-1].append(texto)

    def Imprimir(self):  # list → list
        '''
        Imprime na tela as linha de uma página, e colocando sempre na ultima linha, o número da página
        '''
        numPag = 1
        for folha in self.carderno:
            aux = len(folha)
            for linha in folha:
                aux -= 1
                if aux > 0:
                    print(linha)
                elif aux == 0:
                    print(linha + "    " + str(numPag))
            print('\n')
            numPag += 1


class Diario(Caderno):
    def __init__(self, caderno=[]):
        '''
        Método construtor que herda os atributos da classe caderno, cria um novo atributo 'data' 
        para inserir a data do dia de hoje no inicio de cada página
        '''
        self.data = time.ctime()
        for folha in caderno:
            folha.insert(0,self.data)
        Caderno.__init__(self, caderno)

    def NovaFolha(self):
        '''
        Herda a função NovaFolha() da classe Caderno, e adiciona a data de hoje na primeira linha
        '''
        Caderno.NovaFolha(self)
        self.carderno[len(self.carderno)-1].append(self.data)

if __name__ == '__main__':
    meuDiario = Diario([
        ['Programação orientada a objeto', 'Clases/objetos: estruras básicas, atributos, metodo construtor, métodos mágicos',
        'instãnciamento de objeto, encapsulamento, métodos privados, getters e setters', 'Heranças simples e multiplas' ],
        ['Sobrecarga de operadores','Bibliotecas úteis', 'Normas para criação de um código pra finalidade de melhor entendimento do mesmo',
        'Utilização de editores de texto voltados para programação', 'Unittest, para teste automatizado do código,etc']
    ])
    meuDiario.Imprimir()