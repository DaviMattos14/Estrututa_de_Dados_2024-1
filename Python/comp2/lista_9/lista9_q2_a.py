from tkinter import *

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