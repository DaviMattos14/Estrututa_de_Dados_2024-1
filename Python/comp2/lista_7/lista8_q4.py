from tkinter import *

class Produto:
    def __init__(self, nome, valor, quantidade):
        self.nome = nome
        self.valor = self.valorPositivo(float(valor))
        self.qtd = self.valorPositivo(int(quantidade))

    def valorPositivo(self, valor):
        if valor >= 0:
            return valor
        else:
            raise ValueError('Valor inválido, o valor tem que ser positivo')


class Main_Window:
    def __init__(self, tk):

        self.fr1 = Frame(tk)
        self.fr1.pack()
        self.fr2 = Frame(tk)
        self.fr2.pack()
        self.fr3 = Frame(tk)
        self.fr3.pack()
        self.fr4 = Frame(tk)
        self.fr4.pack()
        self.fr5 = Frame(tk)
        self.fr5.pack()

        self.estoque = []

        self.font = ('Times New Roman', 11, 'bold')

        self.lbNome = Label(self.fr1, text='Nome: ', font=self.font, width=5)
        self.lbNome.pack(side=LEFT)
        self.entNome = Entry(self.fr1)
        self.entNome.pack(side=RIGHT)

        self.lbValor = Label(self.fr2, text='Valor: ', font=self.font)
        self.lbValor.pack(side=LEFT)
        self.entValor = Entry(self.fr2)
        self.entValor.pack(side=RIGHT)

        self.lbQtd = Label(self.fr3, text='Qtd: ', font=self.font, width=5)
        self.lbQtd.pack(side=LEFT)
        self.entQtd = Entry(self.fr3,)
        self.entQtd.pack(side=RIGHT)

        self.btnInserirDados = Button(
            self.fr4, text='Inserir Dados', command=self.Estoque)
        self.btnInserirDados.pack(pady=10)

        self.lbStatus = Label(self.fr5, text=' ',
                              font=('Courier New', 10, 'bold'))
        self.lbStatus.pack(pady=10)

    def Estoque(self):
        try:
            self.estoque.append(
                Produto(self.entNome.get(), self.entValor.get(), self.entQtd.get()))
            self.lbStatus['text'] = 'Produto Registrado'
            self.ClearInputEntries()
        except:
            self.lbStatus['text'] = 'Valor de entrada inválido'
            self.ClearInputEntries()

    def ClearInputEntries(self):
        self.entValor.delete(0,END)
        self.entNome.delete(0,END)
        self.entQtd.delete(0,END)

root = Tk()
Main_Window(root)
root.geometry('250x180')
root.title('Controle de Estoque')
root.mainloop()
