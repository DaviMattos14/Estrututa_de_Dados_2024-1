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