from tkinter import *
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
            self.label2['fg'] = 'red'

raiz = Tk()
tv = StringVar(raiz)
Janela(raiz)
raiz.mainloop()