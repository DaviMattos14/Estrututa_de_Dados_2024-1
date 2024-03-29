"""
    Nome: Davi dos Santos Mattos    DRE: 119133049
"""


class Pilha:

    def __init__(self, elementos=[]):  # list → list
        """
            Método construtor, criar o atributo 'elemento' da classe Pilha,
            recebendo uma lista e retornando uma mensagem de sucesso juntamente com os itens atribuidos,
            caso a parâmetro recebido não seja uma lista,
            ele retorna uma mensagem de erro

        """
        if (isinstance(elementos, list) == True):
            self.elementos = elementos
            print(self.elementos)
            print("Sucesso\n")
            
        elif (isinstance(elementos, list) == False):
            self.elementos = []
            print(self.elementos)
            print("Erro\n")

    def __add__(self, other):  # list → list
        '''
            Realiza uma sobrecarga de operadror "+" através do método especial permitindo mesclar dois objetos
        '''
        if (isinstance(self, list) == isinstance(other, list)):
            pilha1 = Pilha(self.getPilha() + other.getPilha())
            return pilha1
        else:
            print('Erro')

    def empilhar(self, elemento):  # list → list
        """
            Adiciona um elemento no final da lista
        """
        self.elementos.append(elemento)

    def desempilhar(self):  # list → list, string
        """
            Remove o elemento no final da lista, 
            caso a lista eseteja vazia ele retona uma mensagem de erro
        """
        if (len(self.elementos) > 0):
            self.elementos.pop(len(self.elementos)-1)
        elif (len(self.elementos) == 0):
            print("Erro")

    def getPilha(self):  # list → list
        """
            Retorna uma lista
        """
        return self.elementos

    def lenPilha(self):  # list → int
        """
            Retorna a quantidade de elementos da lista
        """
        return len(self.elementos)


if __name__ == '__main__':

    # 7.a) Testando método construtor
    print('\n7.a)')
    p1 = Pilha([1, 7, 9])
    p2 = Pilha()

# 7.b) Testando método empilhar
    # A instãncia é criada com o valor padrão, porém é retornado uma mensagem de erro
    print('\n7.b)')
    p3 = Pilha(10)

# 7.c) Testando método desempilhar
    print('\n7.c)')
    p2.empilhar(4)
    p2.empilhar(10)
    print(p2.getPilha())

# 7.d)
    print('\n7.d)')
    for i in range(len(p2.elementos)+1):
        print(p2.getPilha())
        p2.desempilhar()

# 7.e)
    print('\n7.e)')
    p2.empilhar(5)
    print(p2.getPilha())

# 7. f)
    print('\n7.f)')
    p1 = Pilha([4, 2, 9])
    p2 = Pilha([0, 3, 2])
    p3 = p2 + p1
    p4 = p1 + p2


# 7.g)
    print('\n7.g)')
    print(p3.lenPilha())
