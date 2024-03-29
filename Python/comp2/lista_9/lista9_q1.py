from tkinter import *

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