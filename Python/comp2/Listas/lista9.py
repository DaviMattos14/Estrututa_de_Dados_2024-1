"""
    Nome: Davi dos Santos Mattos    DRE: 119133049
"""
from tkinter import *

# Questão 1
class Window:
    def __init__(self, tk):
        self.c1 = Canvas(tk, height=500, width=500)
        self.c1.pack(side=LEFT)

        x1 = 5.1
        x2 = 10.2
        x3 = 15.3
        while x1 < 250 or x2 < 250 or x3 < 250:    
            if x2 < 250 or x3 < 250 or x1 < 244.7:
                self.c1.create_line((x1,0),(x1,500), fill='#12fc19', width=5.3)
                self.c1.create_line((x2,0),(x2,500), fill='yellow', width=5.3)
                self.c1.create_line((x3,0),(x3,500), fill='blue', width=5.3)
            x1 += 15.3
            x2 += 15.3
            x3 += 15.3
        self.c1.create_line((250,0),(250,500), fill='#12fc19', width=3.5)
        
        yh1 = 0
        yh2 = 20
        for x in range(13):
            x1 =250 
            x2 =260
            x3 =270
            while x1 < 500:
                self.c1.create_polygon((x1,yh2),(x2,yh1),(x3,yh2), fill='red')
                x1 += 20
                x2 += 20
                x3 += 20
            yh1 += 20
            yh2 += 20
        self.c1.create_rectangle((250,260),(500,500), fill='black')

root = Tk()
Window(root)
root.title("Canvas")
root.geometry("500x500")
root,mainloop()

"""
    Questão 2
"""
# A)
class Janela:
    def __init__(self, tk):
        self.c1 = Canvas(tk, height=300, width=500)
        self.c1.pack()

        self.c1.create_rectangle((0,0),(500,100),fill="black")
        self.c1.create_rectangle((0,100),(500,200), fill='red')
        self.c1.create_rectangle((0,200),(500,300), fill='yellow')

root = Tk()
Janela(root)
root.geometry("500x300")
root.mainloop()

# B)
from tkinter import*

class Janela:
    def __init__(self, tk):
        self.c1 = Canvas(tk, height=300, width=600)
        self.c1.pack()

        self.c1.create_rectangle((0,0),(200,300), fill="green")
        self.c1.create_rectangle((200,0),(400,300), fill="white")
        self.c1.create_rectangle((400,0),(600,300), fill="red")

root = Tk()
Janela(root)
root.geometry("600x300")
root.mainloop()

"""
    Questão 3
"""
from tkinter import*

class Janela:
    def __init__(self, tk):
        self.c1 = Canvas(tk, height=600, width=1200)
        self.c1.pack()

        self.c1.create_rectangle((60,0),(1200,900), fill="white")

        #Finlãndia
        self.c1.create_rectangle((600,100),(1200,200), fill="blue")
        self.c1.create_rectangle((750,0),(850,300), fill="blue")
        self.c1.create_polygon((600,100),(750,100),(750,0),(850,0),(850,100),(1200,100),(1200,200),(850,200),(850,300),
        (750,300),(750,200),(600,200), fill="blue")

        #Chile
        self.c1.create_rectangle((0,300),(200,450), fill="blue")
        self.c1.create_rectangle((0,450),(600,600), fill="red")
        self.c1.create_polygon((55,360),(90,360),(100,330),(110,360),(140,360),(115,380),(125,410),(100,390),(75,410),(85,380), fill="white")
        
        # Trindade e Tobago
        self.c1.create_polygon((0,0),(450,300),(0,300),fill="red")
        self.c1.create_polygon((150,0),(600,0),(600,300),fill="red")
        self.c1.create_polygon((20,0),(130,0),(580,300),(470,300),fill="black")

        # Japão - Bônus
        self.c1.create_oval(810,390,960,510, fill='red')


root = Tk()
Janela(root)
root.geometry("1200x600")
root.mainloop()

"""
    Questão 4
"""

from tkinter import*
from tkinter import messagebox

class Poupanca:
    def __init__(self, anos, juros, depositoMensal):
        self.anos = anos
        self.juros = juros/100.0
        self.depositoMensal = depositoMensal

    def calculaTotal(self):
        num_pagamentos = self.anos * 12;
        print(num_pagamentos)
        total = 0
        for i in range(num_pagamentos):
            total += self.depositoMensal
            total *= (1 + self.juros)
        return total

class Janela:
    def __init__(self, tk):
        self.fr1 = Frame(tk)
        self.fr1.pack()
        self.fr2 = Frame(tk)
        self.fr2.pack()
        self.fr3 = Frame(tk)
        self.fr3.pack()
        self.fr4 = Frame(tk)
        self.fr4.pack()
        
        self.font = ('Times New Roman', 12, 'bold')
        self.lbAnos = Label(self.fr1, text='Anos: ', font=self.font, width=15)
        self.lbAnos.pack(side=LEFT)
        self.lbJuros = Label(self.fr2, text='Juros (%): ', font=self.font, width=15)
        self.lbJuros.pack(side=LEFT)
        self.lbDeposito = Label(self.fr3, text='Depósito Mensal (R$): ', font=self.font)
        self.lbDeposito.pack(side=LEFT)

        self.entAnos = Entry(self.fr1)
        self.entAnos.pack(side=RIGHT)

        self.entJuros = Entry(self.fr2)
        self.entJuros.pack(side=RIGHT)

        self.entDeposito = Entry(self.fr3)
        self.entDeposito.pack(side=RIGHT)

        self.btnOK = Button(self.fr4, text='OK', font=('Arial', 12, 'bold'), command=lambda:[self.CriarPoupanca(),self.Mensagem()]).pack(pady=5)

    def CriarPoupanca(self):
        self.poupanca = Poupanca(int(self.entAnos.get()),float(self.entJuros.get()),float(self.entDeposito.get()))
        self.total_acumulado = round(self.poupanca.calculaTotal(), 2)
    
    def Mensagem(self):
        #tkMessageBox.showinfo('Total Acumulado', self.total_acumulado)
        messagebox.showinfo('Total Acumulado', self.total_acumulado)
        

root = Tk()
Janela(root)
root.mainloop()
