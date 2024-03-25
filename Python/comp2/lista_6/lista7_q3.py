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