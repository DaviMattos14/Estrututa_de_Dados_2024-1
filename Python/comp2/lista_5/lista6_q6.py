class NotaInvalida(Exception):
    pass


def exception_nome(nome):
    try:
        if len(str(nome)) >= 3:
            return nome
        else:
            print("Não é um nome válido")
    except TypeError:
        print("Não é um nome válido")


def exception_dre(dre):
    try:
        if len(str(dre)) > 0 and int(dre) > 0:
            return dre
        else:
            raise Exception('DRE inválido')
    except (TypeError, ValueError):
        print("DRE inválido")


def exception_cpf(cpf):
    try:
        if len(str(cpf)) > 9 and int(cpf) > 0:
            return cpf
        else:
            raise Exception('CPF inválido')
    except (TypeError, ValueError):
        print("CPF inválido")


def exception_lista_notas(notas):
    try:
        lista_notas = []
        for n in notas:
            if float(n) > 0 and float(n) < 10:
                lista_notas.append(n)
            else:
                raise Exception(f"{n} é Nota inválida")
        return lista_notas
    except (TypeError, ValueError):
        print("Nota inválida")


class Estudante:
    def __init__(self, nome, dre, cpf, notas=[]):
        self.__nome = exception_nome(nome)
        self.__dre = exception_dre(dre)
        self.__cpf = exception_cpf(cpf)
        self.__notas = exception_lista_notas(notas)

    def setNome(self, n_nome): self.__nome = exception_nome(n_nome)
    def getNome(self): return self.__nome

    def setDRE(self, n_dre): self.__dre = exception_dre(n_dre)
    def getDRE(self): return self.__dre

    def setCPF(self, n_cpf): self.__cpf = exception_cpf(n_cpf)
    def getCPF(self): return self.__cpf

    def setNotas(self, n_Notas): self.__notas = exception_lista_notas(n_Notas)
    def getNotas(self): return self.__notas

    def adicionarNota(self, nota):
        try:
            if float(nota) >= 0 and float(nota) <= 10:
                self.__notas.append(nota)
            else:
                raise NotaInvalida
        except NotaInvalida:
            print("Nota inválida!")
        except (TypeError, ValueError):
            print("Não é um número válido")


a = Estudante('Davi', 11, 1766042735, [6.4, 7.7, 8.9])
a.adicionarNota(2)