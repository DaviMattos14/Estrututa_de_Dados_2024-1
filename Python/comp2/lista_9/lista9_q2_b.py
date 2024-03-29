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