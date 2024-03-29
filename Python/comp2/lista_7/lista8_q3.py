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
