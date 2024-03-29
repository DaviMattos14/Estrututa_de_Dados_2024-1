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