'''
    NOME: Davi dos Santos Mattos    DRE: 119133049
'''

# Questão 1
from tkinter import *

class Main_Window:
    def __init__(self,tk):
        self.fr1 = Frame(tk)
        self.fr1.pack()
        self.fr2 = Frame(tk)
        self.fr2.pack()

        self.lbText = Label(self.fr1, text='Clique para ficar azul.', width=30, height=3)
        self.lbText.pack()

        self.btnMudarCor = Button(self.fr2, text='Clique', bg='#800', fg='#fff')
        self.btnMudarCor.bind('<Button-3>', self.muda_cor)
        self.btnMudarCor.pack()

    def muda_cor(self, event):
        if self.btnMudarCor['bg'] == 'blue':
            self.btnMudarCor['bg'] = '#800'
            self.lbText['text'] = 'Clique para ficar azul'
        else:
            self.btnMudarCor['bg'] = 'blue'
            self.lbText['text'] = 'Clique para ficar grená'

root = Tk()
Main_Window(root)
root.title('Mudar cor')
root.mainloop()

# Questão 2
from tkinter import *

class Main_Window:
    def __init__(self,tk):
        self.fr1 = Frame(tk)
        self.fr1.pack()
        self.fr2 = Frame(tk)
        self.fr2.pack()
        self.fr3 = Frame(tk)
        self.fr3.pack()

        self.lbText = Label(self.fr1, text='Clique para ficar azul.', width=30, height=3)
        self.lbText.pack()

        self.btnMudarCor = Button(self.fr2, text='Clique', bg='#800', fg='#fff')
        self.btnMudarCor.bind('<Button-3>', self.muda_cor)
        self.btnMudarCor.pack(pady=5)

        self.inText = Entry(self.fr3)
        self.inText.pack()
        self.inText.bind(('<Up>','<Up>','<Down>','<Down>','<Left>','<Right>','<Left>','<Right>'),self.konamiCode)

    def muda_cor(self, event):
        if self.btnMudarCor['bg'] == 'blue':
            self.btnMudarCor['bg'] = '#800'
            self.lbText['text'] = 'Clique para ficar azul'
        else:
            self.btnMudarCor['bg'] = 'blue'
            self.lbText['text'] = 'Clique para ficar grená'
    
    def konamiCode(self, event):
        txt = 'KONAMI'
        for letra in txt: print(letra)
        print('\n')

root = Tk()
Main_Window(root)
root.title('Mudar cor')
root.mainloop()

# Questão 3
from tkinter import *
import random

class Main_Window:
    def __init__(self,tk):

        self.cor = ['red','green','blue','yellow','pink','black','white']
        self.pontos = 0

        self.fr1 = Frame(tk)
        self.fr1.pack()
        self.fr2 = Frame(tk)
        self.fr2.pack(pady=20)
        self.fr3 = Frame(tk)
        self.fr3.pack(padx=5, side=LEFT)

        self.btnStart = Button(self.fr1, text='Clique para iniciar', width=15, command=self.start)
        self.btnStart.pack(pady=10,padx=10)
        self.btnStart.bind('<Button-3>', self.reinicia)
        self.orig_color = self.btnStart.cget("background")

        self.btn1Red = Button(self.fr2,padx=6, bg='red', command=lambda color='red':self.pontuacao(color))
        self.btn1Red.pack(side=LEFT,padx=5)
        
        self.btn2Green = Button(self.fr2,padx=6,bg = 'green', command=lambda color='green':self.pontuacao(color))
        self.btn2Green.pack(side=LEFT,padx=5)
        
        self.btn3Blue = Button(self.fr2,padx=6, bg = 'blue', command=lambda color='blue':self.pontuacao(color))
        self.btn3Blue.pack(side=LEFT,padx=5)
        
        self.btn4Yellow = Button(self.fr2,padx=6,bg = 'yellow', command=lambda color='yellow':self.pontuacao(color))
        self.btn4Yellow.pack(side=LEFT,padx=5)
        
        self.btn5Pink = Button(self.fr2,padx=6,bg = 'pink', command=lambda color='pink':self.pontuacao(color))
        self.btn5Pink.pack(side=LEFT,padx=5)
        
        self.btn6Black = Button(self.fr2,padx=6,bg = 'black', command=lambda color='black':self.pontuacao(color))
        self.btn6Black.pack(side=LEFT,padx=5)
        
        self.btn7White = Button(self.fr2,padx=6,bg = 'white', command=lambda color='white':self.pontuacao(color))
        self.btn7White.pack(side=LEFT,padx=5)

        self.lbPontos = Label(self.fr3,text=f'   Pontos:    {self.pontos:}')
        self.lbPontos.pack(side=LEFT)


    def start(self):
        self.btnStart['bg'] = self.cor[random.randint(0,6)]
        if self.btnStart['bg'] =='black':
            self.btnStart['fg'] = 'white'
            self.btnStart['text'] = self.cor[random.randint(0,6)]
        else: 
            self.btnStart['fg'] = 'black'
            self.btnStart['text'] = self.cor[random.randint(0,6)]

    def pontuacao(self, cor):
        if self.btnStart['text'] == cor:
            self.pontos = self.pontos + 1
            self.lbPontos['text'] = f'   Pontos:    {self.pontos:}'
            self.start()
        else:
            self.pontos = self.pontos - 1
            self.lbPontos['text'] = f'   Pontos:    {self.pontos:}'
            self.start()

    def reinicia(self,event):
        self.btnStart['text'] = 'Clique para iniciar'
        self.btnStart['bg'] = self.orig_color
        self.pontos = 0
        self.lbPontos['text'] = f'   Pontos:    {self.pontos:}'

root = Tk()
root.geometry('250x150')
Main_Window(root)
root.title('Colors')
root.mainloop()

# Questão 4
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
