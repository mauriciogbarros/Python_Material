from Tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        rightframe = Frame()
        rightframe.pack(side=RIGHT)
        
        diam = 380; larg = 400; alt = 500
        centroX = larg/2; centroY = alt/2
        canvas = Canvas(bg="black",width=larg,height=alt)
        canvas.create_oval(centroX - diam/2,centroY - diam/2,centroX + diam/2,centroY + diam/2,fill="dark green",outline="yellow",width=10)
        canvas.pack(fill=BOTH, expand=True)
        
        self.lb1 = Label(text="Fichas:",background="white")
        self.lb1.pack(side=LEFT,fill="x",expand=True)
        
        
        self.btn1 = Button(rightframe,text="Aposta")#command=self.########)
        self.btn1.pack(side=BOTTOM,expand=True,fill="x")
        self.btn2 = Button(rightframe,text="Para")#command=self.########)
        self.btn2.pack(side=BOTTOM,expand=True,fill="x")
        self.btn3 = Button(rightframe,text="Manda")#command=self.########)
        self.btn3.pack(side=BOTTOM,expand=True,fill="x")
        

        self.pack()


app = Application()
app.master.title("Blackjack")
mainloop()