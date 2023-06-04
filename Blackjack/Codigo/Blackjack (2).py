# -*- coding: utf-8 -*-
"""
Created on Sun Dec 07 10:08:09 2014

@author: Mauricio, Alexandre
"""

from Tkinter import *
import numpy as np

stack=0
cards=[]
points=[]
hand_player=0
hand_dealer=0
n_player=0
n_dealer=0

top=Tk()
top.resizable(0,0)

#Banco de Imagens
#   c = paus, s=espadas, h=copas, d=ouros
#   1 = ás, j = valete, q = rainha, k = rei
piFundo=PhotoImage(file="Mesa_Blackjack_f.gif")
#Paus (Clubs)
pi_c1=PhotoImage(file="c1.gif")
cards.append(pi_c1)
points.append(11)
pi_c2=PhotoImage(file="c2.gif")
cards.append(pi_c2)
points.append(2)
pi_c3=PhotoImage(file="c3.gif")
cards.append(pi_c3)
points.append(3)
pi_c4=PhotoImage(file="c4.gif")
cards.append(pi_c4)
points.append(4)
pi_c5=PhotoImage(file="c5.gif")
cards.append(pi_c5)
points.append(5)
pi_c6=PhotoImage(file="c6.gif")
cards.append(pi_c6)
points.append(6)
pi_c7=PhotoImage(file="c7.gif")
cards.append(pi_c7)
points.append(7)
pi_c8=PhotoImage(file="c8.gif")
cards.append(pi_c8)
points.append(8)
pi_c9=PhotoImage(file="c9.gif")
cards.append(pi_c9)
points.append(9)
pi_c10=PhotoImage(file="c10.gif")
cards.append(pi_c10)
points.append(10)
pi_cj=PhotoImage(file="cj.gif")
cards.append(pi_cj)
points.append(10)
pi_cq=PhotoImage(file="cq.gif")
cards.append(pi_cq)
points.append(10)
pi_ck=PhotoImage(file="ck.gif")
cards.append(pi_ck)
points.append(10)
#Ouros (Diamonds)
pi_d1=PhotoImage(file="d1.gif")
cards.append(pi_d1)
points.append(11)
pi_d2=PhotoImage(file="d2.gif")
cards.append(pi_d2)
points.append(2)
pi_d3=PhotoImage(file="d3.gif")
cards.append(pi_d3)
points.append(3)
pi_d4=PhotoImage(file="d4.gif")
cards.append(pi_d4)
points.append(4)
pi_d5=PhotoImage(file="d5.gif")
cards.append(pi_d5)
points.append(5)
pi_d6=PhotoImage(file="d6.gif")
cards.append(pi_d6)
points.append(6)
pi_d7=PhotoImage(file="d7.gif")
cards.append(pi_d7)
points.append(7)
pi_d8=PhotoImage(file="d8.gif")
cards.append(pi_d8)
points.append(8)
pi_d9=PhotoImage(file="d9.gif")
cards.append(pi_d9)
points.append(9)
pi_d10=PhotoImage(file="d10.gif")
cards.append(pi_d10)
points.append(10)
pi_dj=PhotoImage(file="dj.gif")
cards.append(pi_dj)
points.append(10)
pi_dq=PhotoImage(file="dq.gif")
cards.append(pi_dq)
points.append(10)
pi_dk=PhotoImage(file="dk.gif")
cards.append(pi_dk)
points.append(10)
#Copas (Hearts)
pi_h1=PhotoImage(file="h1.gif")
cards.append(pi_h1)
points.append(11)
pi_h2=PhotoImage(file="h2.gif")
cards.append(pi_h2)
points.append(2)
pi_h3=PhotoImage(file="h3.gif")
cards.append(pi_h3)
points.append(3)
pi_h4=PhotoImage(file="h4.gif")
cards.append(pi_h4)
points.append(4)
pi_h5=PhotoImage(file="h5.gif")
cards.append(pi_h5)
points.append(5)
pi_h6=PhotoImage(file="h6.gif")
cards.append(pi_h6)
points.append(6)
pi_h7=PhotoImage(file="h7.gif")
cards.append(pi_h7)
points.append(7)
pi_h8=PhotoImage(file="h8.gif")
cards.append(pi_h8)
points.append(8)
pi_h9=PhotoImage(file="h9.gif")
cards.append(pi_h9)
points.append(9)
pi_h10=PhotoImage(file="h10.gif")
cards.append(pi_h10)
points.append(10)
pi_hj=PhotoImage(file="hj.gif")
cards.append(pi_hj)
points.append(10)
pi_hq=PhotoImage(file="hq.gif")
cards.append(pi_hq)
points.append(10)
pi_hk=PhotoImage(file="hk.gif")
cards.append(pi_hk)
points.append(10)
#Espadas (Spades)
pi_s1=PhotoImage(file="s1.gif")
cards.append(pi_s1)
points.append(11)
pi_s2=PhotoImage(file="s2.gif")
cards.append(pi_s2)
points.append(2)
pi_s3=PhotoImage(file="s3.gif")
cards.append(pi_s3)
points.append(3)
pi_s4=PhotoImage(file="s4.gif")
cards.append(pi_s4)
points.append(4)
pi_s5=PhotoImage(file="s5.gif")
cards.append(pi_s5)
points.append(5)
pi_s6=PhotoImage(file="s6.gif")
cards.append(pi_s6)
points.append(6)
pi_s7=PhotoImage(file="s7.gif")
cards.append(pi_s7)
points.append(7)
pi_s8=PhotoImage(file="s8.gif")
cards.append(pi_s8)
points.append(8)
pi_s9=PhotoImage(file="s9.gif")
cards.append(pi_s9)
points.append(9)
pi_s10=PhotoImage(file="s10.gif")
cards.append(pi_s10)
points.append(10)
pi_sj=PhotoImage(file="sj.gif")
cards.append(pi_sj)
points.append(10)
pi_sq=PhotoImage(file="sq.gif")
cards.append(pi_sq)
points.append(10)
pi_sk=PhotoImage(file="sk.gif")
cards.append(pi_sk)
points.append(10)
#Outras
pi_back=PhotoImage(file="b1fv.gif")
pi_back_pile=PhotoImage(file="b1pr.gif")

def _new():
    global stack
    stack=1000
    lblStack["text"]="$"+str(stack)+".00"
    _file.entryconfig("Save", state=NORMAL)
    place_btnDeal()
    place_lblBet()
    
def _open(): pass

def _save(): pass

def hit():
    global n_player
    global hand_player
    print hand_player
    n_player=n_player+1
    z=np.random.uniform(0,51)
    hand_player=hand_player+points[int(z)]
    
    if n_player==3:
        lblCard3_player["image"]=cards[int(z)]
        lblCard3_player.pack(side=LEFT)
        
    elif n_player==4:
        lblCard4_player["image"]=cards[int(z)]
        lblCard4_player.pack(side=LEFT)
        
    elif n_player==5:
        lblCard5_player["image"]=cards[int(z)]
        lblCard5_player.pack(side=LEFT)
        
    elif n_player==6:
        lblCard6_player["image"]=cards[int(z)]
        lblCard6_player.pack(side=LEFT)
        
    elif n_player==7:
        lblCard7_player["image"]=cards[int(z)]
        lblCard7_player.pack(side=LEFT)
        
    elif n_player==8:
        lblCard8_player["image"]=cards[int(z)]
        lblCard8_player.pack(side=LEFT)
        
    elif n_player==9:
        lblCard9_player["image"]=cards[int(z)]
        lblCard9_player.pack(side=LEFT)
        
    elif n_player==10:
        lblCard10_player["image"]=cards[int(z)]
        lblCard10_player.pack(side=LEFT)

    print n_player
    print hand_player
    if hand_player>21:
        btnHit["state"]=DISABLED
    
def stand():
    global n_dealer
    global hand_player
    global hand_dealer
    
    n_dealer=2
    z=np.random.uniform(0,51)
    hand_dealer=hand_dealer+points[int(z)]
    lblCard2_dealer["image"]=cards[int(z)]
    lblCard2_dealer.pack(side=LEFT)

    while hand_dealer<17:
        n_dealer=n_dealer+1
        z=np.random.uniform(0,51)
        hand_dealer=hand_dealer+points[int(z)]    
        if n_dealer==3:
            lblCard3_dealer["image"]=cards[int(z)]
            lblCard3_dealer.pack(side=LEFT)
                
        elif n_dealer==4:
            lblCard4_dealer["image"]=cards[int(z)]
            lblCard4_dealer.pack(side=LEFT)
                
        elif n_dealer==5:
            lblCard5_dealer["image"]=cards[int(z)]
            lblCard5_dealer.pack(side=LEFT)
                
        elif n_dealer==6:
            lblCard6_dealer["image"]=cards[int(z)]
            lblCard6_dealer.pack(side=LEFT)
                
        elif n_dealer==7:
            lblCard7_dealer["image"]=cards[int(z)]
            lblCard7_dealer.pack(side=LEFT)
                
        elif n_dealer==8:
            lblCard8_dealer["image"]=cards[int(z)]
            lblCard8_dealer.pack(side=LEFT)
                
        elif n_dealer==9:
            lblCard9_dealer["image"]=cards[int(z)]
            lblCard9_dealer.pack(side=LEFT)
                
        elif n_dealer==10:
            lblCard10_dealer["image"]=cards[int(z)]
            lblCard10_dealer.pack(side=LEFT)
            
    print hand_dealer
    btnHit["state"]=DISABLED
    btnStand["state"]=DISABLED
    if hand_player>hand_dealer: pass
    if hand_player<hand_dealer: pass
    if hand_player==hand_dealer: pass
    

def dbl_down(): pass

def _exit():
    top.destroy()

def bet_amount():
    lblBet["text"]="$"+str(rdbtn_value.get())+".00"
    btnDeal["state"]=NORMAL

def deal():
    global hand_player
    global hand_dealer
    global stack
    global n_player
    global n_dealer
    stack=stack-rdbtn_value.get()
    lblStack["text"]="$"+str(stack)+".00"
    btnDeal.place_forget()
    rdbtn_1["state"]=DISABLED
    rdbtn_5["state"]=DISABLED
    rdbtn_10["state"]=DISABLED
    rdbtn_25["state"]=DISABLED
    rdbtn_100["state"]=DISABLED
    place_btnHit()
    place_btnStand()
    place_btnDblDown()
    place_chbtnInsurance()
    z=np.random.uniform(0,51)
    lblCard1_player["image"]=cards[int(z)]
    hand_player=points[int(z)]
    z=np.random.uniform(0,51)
    lblCard2_player["image"]=cards[int(z)]
    hand_player=hand_player+points[int(z)]
    z=np.random.uniform(0,51)
    lblCard1_dealer["image"]=cards[int(z)]
    hand_dealer=points[int(z)]

    n_player=2
    n_dealer=1
    if hand_player == 21:
        stack=stack + 2.5*rdbtn_value.get()
    elif hand_player < 21: pass
    
#Posicionamento de widgets
def place_btnDeal():
    btnDeal.place(x=280, y=405)

def place_lblBet():
    lblBet.place(x=275, y=300)

def place_btnHit():
    btnHit.place(x=245, y=365)

def place_btnStand():
    btnStand.place(x=308, y=365)

def place_btnDblDown():
    btnDblDown.place(x=245, y=415)

def place_chbtnInsurance():
    chbtnInsurance.place(x=245, y=390)

mnMenu=Menu(top)
top.configure(menu=mnMenu)
_file=Menu(mnMenu, tearoff=0)
_file.add_command(label="New Game", command=_new, underline=0)
_file.add_separator()
_file.add_command(labe="Open", command=_open, underline=0)
_file.add_command(label="Save", command=_save, underline=0)
_file.add_separator()
_file.add_command(label="eXit", command=_exit, underline=1)
mnMenu.add_cascade(label="File", menu=_file)
_file.entryconfig("Open", state=DISABLED)
_file.entryconfig("Save", state=DISABLED)

frQuadro=Frame(top, width=602, height=700)
frQuadro.pack()

# Mesa e cartas
lblFundo=Label(frQuadro, image=piFundo)
lblFundo.pack()

lblStack=Label(frQuadro,bg="white",font=("Verdana","14","bold"))
lblStack.place(x=255,y=445)
lblStack["text"]="$"+str(stack)+".00"
frCards_player=Frame(frQuadro)
frCards_dealer=Frame(frQuadro)
frCards_player.place(x=260, y=195)
frCards_dealer.place(x=260, y=20)
lblCard1_player=Label(frCards_player, image=pi_back, bd=0)
lblCard2_player=Label(frCards_player, image=pi_back_pile, bd=0)
lblCard3_player=Label(frCards_player, bd=0)
lblCard4_player=Label(frCards_player, bd=0)
lblCard5_player=Label(frCards_player, bd=0)
lblCard6_player=Label(frCards_player, bd=0)
lblCard7_player=Label(frCards_player, bd=0)
lblCard8_player=Label(frCards_player, bd=0)
lblCard9_player=Label(frCards_player, bd=0)
lblCard10_player=Label(frCards_player, bd=0)
lblCard1_player.pack(side=LEFT)
lblCard2_player.pack(side=LEFT)
lblCard1_dealer=Label(frCards_dealer, image=pi_back, bd=0)
lblCard2_dealer=Label(frCards_dealer, image=pi_back_pile, bd=0)
lblCard3_dealer=Label(frCards_dealer, bd=0)
lblCard4_dealer=Label(frCards_dealer, bd=0)
lblCard5_dealer=Label(frCards_dealer, bd=0)
lblCard6_dealer=Label(frCards_dealer, bd=0)
lblCard7_dealer=Label(frCards_dealer, bd=0)
lblCard8_dealer=Label(frCards_dealer, bd=0)
lblCard9_dealer=Label(frCards_dealer, bd=0)
lblCard10_dealer=Label(frCards_dealer, bd=0)
lblCard1_dealer.pack(side=LEFT)
lblCard2_dealer.pack(side=LEFT)

lblBet=Label(frQuadro, text=" ", font=("12"), borderwidth=3)
lblBet["background"]="#%02x%02x%02x"%(0,128,0)

rdbtn_value=IntVar(value=0)
rdbtn_1=Radiobutton(top, value=1, variable=rdbtn_value, bg="white", command=bet_amount)
rdbtn_5=Radiobutton(top, value=5, variable=rdbtn_value, bg="white", command=bet_amount)
rdbtn_10=Radiobutton(top, value=10, variable=rdbtn_value, bg="white", command=bet_amount)
rdbtn_25=Radiobutton(top, value=25, variable=rdbtn_value, bg="white", command=bet_amount)
rdbtn_100=Radiobutton(top, value=100, variable=rdbtn_value, bg="white", command=bet_amount)
rdbtn_1.place(x=15, y=445)
rdbtn_5.place(x=55, y=445)
rdbtn_10.place(x=95, y=445)
rdbtn_25.place(x=135, y=445)
rdbtn_100.place(x=175, y=445)

btnDeal=Button(frQuadro, text="DEAL!", command=deal, state=DISABLED)

btnHit=Button(frQuadro, text="Hit", command=hit, width=7)
btnStand=Button(frQuadro, text="Stand", command=stand, width=7)
btnDblDown=Button(frQuadro, text="Double Down", command=dbl_down, width=16, state=DISABLED)

chbtn_value=IntVar()
chbtnInsurance=Checkbutton(frQuadro, text="Insurance", variable=chbtn_value, state=DISABLED)
chbtnInsurance["background"]="#%02x%02x%02x"%(0,85,0)

top.title("Welcome to Blackjack")
mainloop()
