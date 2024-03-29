"""
NOME: Davi dos Santos Mattos    DRE: 119133049
[Exceções]
"""

"""
QUESTÃO 1
"""
class Fracao():
    def __init__(self, numerador, denominador):
        try:
            self.__numerador = numerador
            self.__denominador = denominador
            res = self.__numerador/self.__denominador
        except ZeroDivisionError:
            print("\nDenominador inválido!")

    def getNumerador(self): return self.__numerador
    def getDenominador(self): return self.__denominador

    def __str__(self):
        return str('{} / {}'.format(self.__numerador, self.__denominador))

    def __add__(self, outro):
        num = (self.__numerador*outro.getDenominador()) + \
            (outro.getNumerador()*self.__denominador)
        den = self.__denominador * outro.getDenominador()
        return Fracao(num, den)

    def __sub__(self, outro):
        num = (self.__numerador*outro.getDenominador()) - \
            (outro.getNumerador()*self.__denominador)
        den = self.__denominador * outro.getDenominador()
        return Fracao(num, den)

    def __truediv__(self, outro):
        num = self.__numerador * outro.getDenominador()
        den = self.__denominador * outro.getNumerador()
        return Fracao(num, den)


"""
QUESTÃO 2
"""
class Pessoa:
    def __init__(self, nome, celular, telefone_fixo, email):
        if len(nome) < 3: raise Exception('Nome inválido')
        if len(email) <= 10: raise Exception('E=mail Inválido')
        if len(str(celular)) <8 or len(str(telefone_fixo)) < 8: raise Exception('Número Inválido')
        else:
            self.nome = nome
            self.celular = celular
            self.telefone_fixo = telefone_fixo
            self.email = email
     

"""
QUESTÃO 3
"""
import string


def conta_linhas_palavras(arq):
    arquivo = open(arq, 'r+')
    qtd_5_mais = 0
    linhas = 0
    for linha in arquivo:
        linhas += 1
        palavras_linha = linha.strip()
        palavras_linha = palavras_linha.split(' ')
        for palavra in palavras_linha:
            palavra = palavra.translate(
                str.maketrans('', '', string.punctuation))
            if len(palavra) > 5:
                qtd_5_mais += 1
    arquivo.write(
        '\n'*3 + 'Seu arquivo possui {} linhas e {} palavras com mais de 5 caracteres'.format(linhas, qtd_5_mais))


if __name__ == '__main__':
    while True:
        arquivo = input("Digite o nome do arquivo: ")
        try:
            conta_linhas_palavras(arquivo)
        except IOError:
            print("O Arquivo digitado não existe")
        else:
            break
        

"""
QUESTÃO 4
"""
def exception_nota(nota):
    if 0 > nota or nota > 10:
        raise Exception("Nota Inválida")
    else:
        return nota


def exception_menor0(valor):
    if valor < 0:
        raise Exception("Numéro digitado é inválido")
    else:
        return valor


class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        if 0 < len(str(cpf)) <= 11:
            self.cpf = cpf
        else:
            raise Exception("CPF Inválido!")

    def setTelefone(self, telefone):
        if 9 <= len(str(telefone)) and isinstance(telefone, int) == True: self.__telefone = telefone
        else: raise Exception("Número de telefone inválido")

    def getTelefone(self):
        return self.__telefone

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def getEndereco(self):
        return self.__endereco

    def setIdentidade(self, identidade):
        if 0 < len(str(identidade)) <= 9:
            self.__identidade = identidade
        else:
            raise Exception("Identidade Inválida!")

    def getIdentidade(self):
        return self.__identidade

    def setIdade(self, idade):
        self.__idade = exception_menor0(idade)

    def getIdade(self):
        return self.__idade


class Notas:
    def __init__(self, nota1, nota2, nota3):
        self.__nota1 = exception_nota(nota1)
        self.__nota2 = exception_nota(nota2)
        self.__nota3 = exception_nota(nota3)

    def setNota1(self, novaNota):
        self.__nota1 = exception_nota(novaNota)

    def getNota1(self):
        return self.__nota1

    def setNota2(self, novaNota):
        self.__nota2 = exception_nota(novaNota)

    def getNota2(self):
        return self.__nota2

    def setNota3(self, novaNota):
        self.__nota3 = exception_nota(novaNota)

    def getNota3(self):
        return self.__nota3

    def calcular_Media(self):
        return (self.getNota3() + self.getNota2() + self.getNota1()) / 3

    def __str__(self):
        return str('P1: {} P2: {} P3: {}'.format(self.__nota1, self.__nota2, self.__nota3))


class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, notaAluno):
        super().__init__(nome, cpf)
        self.__matricula = matricula
        self.__notaAluno = notaAluno

    def setMatricula(self, nova_matricula):
        self.__matricula = nova_matricula

    def getMatricula(self):
        return self.__matricula

    def setNotaAluno(self, nova_notaAluno):
        self.__notaAluno = nova_notaAluno

    def getMatricula(self):
        return self.__notaAluno

    def visualisarMedia(self):
        return self.__notaAluno.calcular_Media()

    def __str__(self):
        return str("Nome: {} CPF: {} Matricula: {} \nNotas: {}\n".format(self.nome, self.cpf, self.__matricula, self.__notaAluno))


class Professor(Pessoa):
    def __init__(self, nome, cpf, salario=0):
        super().__init__(nome, cpf)
        self.salario = exception_menor0(salario)

    def mostrarSalario(self):
        print(self.salario)

    def __str__(self):
        return str("Nome: {} CPF: {} Salario: R${} \n".format(self.nome, self.cpf, self.salario))


class Professor_Horista(Professor):
    def __init__(self, nome, cpf, salario, hora_de_aula, valor_de_aula):
        super().__init__(nome, cpf, salario)
        self.hora_de_aula = exception_menor0(hora_de_aula)
        self.valor_de_aula = exception_menor0(valor_de_aula)

    def calcula_salario(self):
        return self.hora_de_aula * self.valor_de_aula


class Controller:
    lista_professor = []
    lista_aluno = []

    def incluir_professor(
        self, professor): self.lista_professor.append(professor)

    def incluir_aluno(self, aluno): self.lista_aluno.append(aluno)

    def pesquisa_aluno_nome(self, nome_aluno):
        aux = ''
        for aluno in self.lista_aluno:
            if aluno.nome == nome_aluno:
                aux = str(aluno)
        if aux != '':
            print(aux)
        else:
            print("O Aluno não consta na listagem")

    def pesquisa_aluno_cpf(self, cpf_aluno):
        aux = 0
        for aluno in self.lista_aluno:
            if aluno.cpf == cpf_aluno:
                aux = str(aluno)
        if aux != 0:
            print(aux)
        else:
            print("O Aluno não consta na listagem")

    def pesquisa_professor_nome(self, nome_professor):
        aux = ''
        for professor in self.lista_professor:
            if professor.nome == nome_professor:
                aux = str(professor)
        if aux != '':
            print(aux)
        else:
            print("O Professor não consta na listagem")

    def pesquisa_professor_cpf(self, cpf_professor):
        aux = 0
        for professor in self.lista_professor:
            if professor.cpf == cpf_professor:
                aux = str(professor)
        if aux != 0:
            print(aux)
        else:
            print("O Professor não consta na listagem")


"""
QUESTÃO 5
"""
class Produto:
    def __init__(self, codigo=99999, descricao='Produto sem descrição', preco=0.0):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco

    def cadastrarProduto(self, codigo, descricao, preco):
        if codigo < 0:
            raise Exception("O valor do código não é válido")
        try:
            if float(preco) > 0:
                self.codigo = codigo
                self.descricao = descricao
                self.preco = preco
            else:
                raise Exception("O Preço não é válido")
        except ValueError:
            print("O preço digitado não é um valor válido")

    def armazenarNoArquivo(self, arq):
        try:
            arquivo = open(arq, 'a')
            arquivo.write("{};{};{}\n".format(
                self.codigo, self.descricao, self.preco))
            arquivo.close()
            print(f"Produto armazenado em [{arq}]")
        except (OSError, NameError, IOError):
            print("Nome do arquivo errado, digite 'nome_do_arquivo.txt'")
        finally:
            print("Armazenando o produto em 'lista_produto.txt'...")
            novo_arquivo = open('lista_produto.txt', 'a')
            novo_arquivo.write("{};{};{}\n".format(
                self.codigo, self.descricao, self.preco))
            novo_arquivo.close()


class Manipula:
    def leProdutosAcimaValor(self, nome_arquivo, valor):
        try:
            arquivo = open(nome_arquivo, 'r')
            aux = 0
            for linha in arquivo:
                linha = linha.strip()
                linha = linha.split(';')
                if float(linha[2]) > valor:
                    print(
                        f"Id: {linha[0]} | Descrição: {linha[1]} | Preço: R${linha[2]}")
                    aux += 1
            if aux == 0:
                print("Não há produtos acima do preço!")
            arquivo.close()
        except IOError:
            print("Arquivo inexistente")
        except TypeError:
            print("O preço não é um valor válido")

    def buscaPreco(self, nome_arquivo, id_produto):
        try:
            arquivo = open(nome_arquivo, 'r')
            aux = 0
            for linha in arquivo:
                linha = linha.strip()
                linha = linha.split(';')
                if str(id_produto) in linha:
                    print(f"{linha[1]} - R${linha[2]}")
                    aux += 1
            if aux == 0:
                print("Não há produtos com esse id!")
            arquivo.close()
        except IOError:
            print("Arquivo inexistente")
        except TypeError:
            print("O preço não é um valor válido")

"""
QUESTÃO 6
"""
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
            if float(n) >= 0 and float(n) <= 10:
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

"""
QUESTÃO 7
"""
import math

class ErroAritimetico(Exception): pass
class RaizNegativa(ErroAritimetico): pass
class ModuloMaior(ErroAritimetico):pass


def raizQuadrada(num):
    if num > 0: return math.sqrt(num)
    else: raise RaizNegativa

def modulo(a,b):
    if a > b: return a % b
    else: raise ModuloMaior


try:
    raizQuadrada(81)
    raizQuadrada(-9)
    modulo(8,3)
    modulo(3,8)
except RaizNegativa: print("Raiz Negativa!")
except ModuloMaior: print("Modulo Maior")
