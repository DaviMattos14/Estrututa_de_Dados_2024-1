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