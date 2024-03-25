'''
    NOME: Davi dos Santos Mattos    DRE: 119133049
'''

from tkinter import *

# Questão 1
class Janela:
    def __init__(self, tk):
        self.fr1 = Frame(tk)
        self.fr1.pack()
        self.label = Label(self.fr1, fg = 'blue', 
        font = ('Times New Roman', 14, 'bold'), 
        text = 'PASSWORDS', height = 2)
        self.label.pack()

        self.fr2 = Frame(tk)
        self.fr2.pack(padx = 10)
        Label(self.fr2, 
        text = 'Nome:', fg = 'black', 
        font = ("Courier New", 10, 'bold')).pack(side=LEFT)
        self.entrada1 = Entry(self.fr2)
        self.entrada1.pack(side=RIGHT, padx = 10)

        self.fr3 = Frame(tk)
        self.fr3.pack()
        Label(self.fr3, 
        text = 'Senha:', fg = 'black', 
        font = ("Courier New", 10, 'bold')).pack(side=LEFT)
        self.entrada2 = Entry(self.fr3, show = '*')
        self.entrada2.pack(side=RIGHT, padx = 10)
        
        self.fr4 = Frame(tk)
        self.fr4.pack(pady = 4)
        Button(self.fr4, text = 'Conferir', fg = 'black', 
        bg = 'pink', font=("Arial", 10, 'bold'), 
        command = self.confereSenha).pack()

        self.fr5 = Frame(tk)
        self.fr5.pack()
        self.label2 = Label(self.fr5, fg = 'Blue', 
        font = ("Arial", 14, 'bold'),
        text = 'AGUARDANDO', height = 3)
        self.label2.pack() 

    def confereSenha(self):
        if self.entrada2.get() == self.entrada1.get():
            self.label2['text'] = 'ACESSO PERMITIDO'
            self.label2['fg'] = 'green'
        else:
            self.label2['text'] = 'ACESSO NEGADO'
            self.label2['fg'] = 'pink'

raiz = Tk()
Janela(raiz)
raiz.mainloop()

# Questão 2

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

# Questão 3
from datetime import datetime
from tkinter import *

class EntradaDeCinema:
    def __init__(self, nomeDoFilme, dataDoFilme, horario, sala, valor=28):
        self.nome_do_filme = nomeDoFilme
        self.data_do_filme = dataDoFilme
        self.horario = datetime.strptime(horario, '%H:%M').time()
        self.sala = sala
        self.valor = float(valor)

    def calculaDesconto(self, idade, numCartEstudante=0):
        if idade < 12: 
            self.valor -= self.valor * 0.5
            self.CalculaDescontoHorario()
        if numCartEstudante != 0 and 12 < idade < 20: 
            self.valor -= self.valor *0.4
            self.CalculaDescontoHorario()
        if len(str(numCartEstudante)) > 4 and 20 < idade: 
            self.valor -= self.valor * 0.3
            self.CalculaDescontoHorario()
        else: self.CalculaDescontoHorario()

    def CalculaDescontoHorario(self):
        if self.horario < datetime.strptime('16:00','%H:%M').time():
            self.valor -= self.valor * 0.1

class Main_Winddow:
    def __init__(self, tk):
        
        self.font = 'Arial 11 bold'

        self.fr1 = Frame(tk) # Frame 1
        self.fr1.pack(pady=10)

        self.lb = Label(self.fr1, text='Cadastrar Sessão', font=('Times New Roman', 14)).pack(padx=15)

        self.fr2 = Frame(tk) # Frame 2
        self.fr2.pack(padx=18)
        
        Label(self.fr2, text='Nome: ', font=self.font, width=8).pack(side=LEFT)
        self.nome_filme = Entry(self.fr2)
        self.nome_filme.pack(side=RIGHT)

        self.fr3 = Frame(tk) # Frame 3
        self.fr3.pack(padx=18)
        Label(self.fr3, text='Data: ', font=self.font, width=8).pack(side=LEFT)
        self.data_filme = Entry(self.fr3)
        self.data_filme.pack(side=RIGHT)


        self.fr4 = Frame(tk) # Frame 4
        self.fr4.pack()
        Label(self.fr4, text='Horário: ', font=self.font, width=8).pack(side=LEFT)
        self.hora_filme = Entry(self.fr4)
        self.hora_filme.pack(side=RIGHT)

        self.fr5 = Frame(tk) # Frame 5
        self.fr5.pack()
        Label(self.fr5, text='Sala: ', font=self.font, width=8).pack(side=LEFT)
        self.sala = Entry(self.fr5)
        self.sala.pack(side=RIGHT)
        
        self.fr6 = Frame(tk) # Frame 6
        self.fr6.pack()
        self.btnCadastrar = Button(self.fr6, text='Cadastrar', padx=10, command=self.cadastrar)
        self.btnCadastrar.pack(pady=10)

        self.fr7 = Frame(tk) # Frame 7
        self.fr7.pack(pady=5)
        Label(self.fr7, text= 'Calcular Valor de Entrada', font=('Times New Roman', 14)).pack()

        self.fr8 = Frame(tk) # Frame 8
        self.fr8.pack()
        Label(self.fr8, text='Idade:', font=self.font).pack(side=LEFT)
        self.idade = Entry(self.fr8,width=5)
        self.idade.pack(side=RIGHT)

        self.fr9 = Frame(tk) # Frame 9
        self.fr9.pack(padx=15)
        Label(self.fr9, text= 'Carteirinha: ', font=self.font).pack(side=LEFT)
        self.id_carteirinha = Entry(self.fr9)
        self.id_carteirinha.pack(side=LEFT)

        self.fr10 = Frame(tk) # Frame 10
        self.fr10.pack()
        self.btnCalcularDesconto = Button(self.fr10,text='Calcular Valor', width=12, command=self.desconto)
        self.btnCalcularDesconto.pack(pady=5)

        self.fr11 = Frame(tk) # Frame 11
        self.fr11.pack()
        self.lbValorIngresso = Label(self.fr11, text=' ', font=self.font, pady=15)
        self.lbValorIngresso.pack()
    
    def cadastrar(self):
        self.sessao = EntradaDeCinema(self.nome_filme.get(),self.data_filme.get(),self.hora_filme.get(),self.sala.get())
    def desconto(self):
        self.sessao.calculaDesconto(int(self.idade.get()),str(self.id_carteirinha.get()))
        self.lbValorIngresso['text'] = f'Valor = R${float(self.sessao.valor):.2f}'

root = Tk()
Main_Winddow(root)
root.title('Entrada de Cinema')
root.mainloop()

# Questão 4
from tkinter import *

class Main_Windown:
    def __init__(self, tk):
        self.font = ('Arial', 11)

        self.fr1 = Frame(tk)
        self.fr1.pack(padx=20)

        self.lbText = Label(self.fr1, text='Carro Novo R$', font=self.font).pack(side=LEFT)
        self.txtCarroNovo = Entry(self.fr1, width=12)
        self.txtCarroNovo.pack()

        self.fr2 = Frame(tk)
        self.fr2.pack()

        Label(self.fr2, text= 'Carro Usado R$', font=self.font).pack(side=LEFT)
        self.txtCarroUsado = Entry(self.fr2, width=12)
        self.txtCarroUsado.pack()

        self.fr3 = Frame(tk)
        self.fr3.pack()

        Label(self.fr3, text='Margem de Lucro (%):', font=self.font).pack(side=LEFT)
        self.txtLucro = Entry(self.fr3, width=8)
        self.txtLucro.pack()

        self.fr4 = Frame(tk)
        self.fr4.pack(pady=8)
        self.btnCalcular = Button(self.fr4, text='Calcular', width=10, activeforeground='blue', command=self.Calcular)
        self.btnCalcular.pack(padx=5, side=LEFT)
        self.btnLimpar = Button(self.fr4, text='Limpar', width=10, activeforeground='red', command=self.Limpar)
        self.btnLimpar.pack(padx=5)

        self.fr5 = Frame(tk)
        self.fr5.pack(pady=2)
        self.lbStatus = Label(self.fr5, text=' ', font=('Times New Roman', 12, 'bold'))
        self.lbStatus.pack()

    def Limpar(self):
        self.txtCarroNovo.delete(0,END)
        self.txtCarroUsado.delete(0,END)
        self.txtLucro.delete(0,END)

    def Calcular(self):
        lucro = float(str(self.txtLucro.get()).strip('%')) / 100
        valor_a_pagar = 0
        if len(self.txtCarroUsado.get()) == 0:
            valor_a_pagar = float(self.txtCarroNovo.get()) + (float(self.txtCarroNovo.get())*lucro)
        else: 
            valor_a_pagar = (float(self.txtCarroNovo.get()) + (float(self.txtCarroNovo.get())*lucro)) - float(self.txtCarroUsado.get())
        self.lbStatus['text'] = f'Valor a pagar = R${valor_a_pagar:.2f}'

root = Tk()
Main_Windown(root)
root.title('Cálculo de Lucro')
root.mainloop()