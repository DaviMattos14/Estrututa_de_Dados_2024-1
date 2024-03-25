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
