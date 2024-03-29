# Lista 5 - Tkinter - Questão 2 - Comp2 2022.2

from tkinter import *

class ContaCorrente:
    def __init__(self, nome='', data_criacao='', limite=0):
        self.__nome = nome
        self.__data_criacao = data_criacao
        self.__limite = limite
        self.__saldo = 0

    def getNome(self): return self.__nome
    def getDataCriacao(self): return self.__data_criacao
    def getLimite(self): return self.__limite
    def getSaldo(self): return self.__saldo

    def setLimite(self, novoLimite): self.__limite = novoLimite
    def setNome(self, novoNome): self.__nome = novoNome

    def Deposito(self, valor):
        if valor >=0:
            self.__saldo += valor
        else: raise Exception("Valor de depósito inválido")

    def Saque(self, valor):
        if valor > self.__saldo or valor < 0: raise Exception("Valor de saque é maior que o valor em conta!")
        else: self.__saldo -= valor

class Main_Window:
    def __init__(self, tk):

        self.fr1 = Frame(tk)
        self.fr1.pack(padx=25)
        self.fr2 = Frame(tk)
        self.fr2.pack(padx=25)
        self.fr3 = Frame(tk)
        self.fr3.pack(padx=25)
        self.fr4 = Frame(tk)
        self.fr4.pack(pady=5)
        self.fr5 = Frame(tk)
        self.fr5.pack(padx=25, pady=5)
        self.fr6 = Frame(tk)
        self.fr6.pack(pady=2)
        self.fr7 = Frame(tk)
        self.fr7.pack(padx=15,pady=15)

        self.Label = Label(self.fr1,text='Nome: ', fg='black', width=15,
        font=('Arial', 11)).pack(side=LEFT)
        self.entrada1 = Entry(self.fr1)
        self.entrada1['width'] = 25
        self.entrada1.pack(side=LEFT)

        Label(self.fr2, text='Data de Criação: ', fg='black',width=15,
        font=('Arial',11)).pack(side=LEFT)
        self.entrada2 = Entry(self.fr2)
        self.entrada2['width'] = 25
        self.entrada2.pack(side=LEFT)

        Label(self.fr3, text='Limite: ', fg='black', width=15,
        font='Arial 11').pack(side=LEFT)
        self.entrada3 = Entry(self.fr3)
        self.entrada3['width'] = 25
        self.entrada3.pack(side=LEFT)

        self.botaoCriarConta = Button(self.fr4, text='Criar Conta', padx=10, 
        command= self.Conta).pack()

        Label(self.fr5, text='Depósito/Saque: R$', fg='black',
        font='Arial 11').pack(side=LEFT)
        self.entradaValor = Entry(self.fr5, width=15)
        self.entradaValor.pack()

        self.botaoSaque = Button(self.fr6, text='Saque', padx=10,
        command=self.Saque).pack(side=RIGHT, padx=10)
        self.botaoDeposito = Button(self.fr6, text='Depósito', padx=10, 
        command=self.Deposito).pack(side=RIGHT, padx=10)

        self.lbStatus = Label(self.fr7, font=('Times New Roman',14,'bold'),text='...')
        self.lbStatus.pack()

    def clearTextInput(self):
        self.entrada1.delete(0,END)
        self.entrada2.delete(0,END)
        self.entrada3.delete(0,END)

    def Conta(self):
        try:
            self.conta = ContaCorrente(self.entrada1.get(),self.entrada2.get(),float(self.entrada3.get()))
            self.lbStatus['text'] = 'Saldo = ' + str(self.conta.getSaldo())
        except (ValueError, Exception):
            self.lbStatus['text'] = 'Valores de entrada inválidos'
            self.clearTextInput()

    def Saque(self):
        try:
            if float(self.entradaValor.get()) <= self.conta.getSaldo():
                self.conta.Saque(float(self.entradaValor.get()))
                self.lbStatus['text'] = 'Saldo = ' + str(self.conta.getSaldo())
            else:
                self.lbStatus['text'] = 'Saldo é insuficiente'                
        except (ValueError, Exception):
            self.lbStatus['text'] = 'Valores de entrada inválidos'
            self.entradaValor.delete(0,END)
   
    def Deposito(self):
        try:
            if float(self.entradaValor.get()) > 0:
                self.conta.Deposito(float(self.entradaValor.get()))
                self.lbStatus['text'] = 'Saldo = ' + str(self.conta.getSaldo())
            else: self.lbStatus['text'] = 'Valor inválido'
        except (ValueError,Exception):
            self.lbStatus['text'] = 'Valores de entrada inválidos'
            self.entradaValor.delete(0,END)

raiz = Tk()
Main_Window(raiz)
raiz.title('Conta')
raiz.mainloop()
