from Tkinter import *
from threading import Timer

top = Tk()
fr = Frame(top, height=500, width=400)

im1 = PhotoImage(file="b1fv.gif")
im2 = PhotoImage(file="2.gif")
lb1=Label(fr,image=im1,height=96,width=72)
lb2=Label(fr,image=im2,height=96,width=0)

fr.pack()
lb1.place(x=0, y=0, anchor=NW)
lb2.place(x=0, y=0, anchor=NE)

def timeout():
    global t
    largura=int(lb1["width"].string)
    passo=1
    if largura<72:
        largura=largura+passo
        lb2.configure(width=int(largura))
    sys.stdout.flush()
    t=Timer(0.3, timeout)
    t.start()

t=Timer(0.3, timeout)
t.start()
mainloop()
    
