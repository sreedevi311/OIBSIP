def start():
    Label(w,text='Select  Your  Choice :',font=('Arial',17),bg='#1FAB89',fg='white').grid(row=2,columnspan=5,padx=10,pady=20)
    Button(w,text='ROCK',font=('Arial Bold',10),bg='#1FAB89',fg='white',padx=34,pady=15,command=lambda: display('ROCK')).grid(row=3,column=1,padx=40,pady=20)
    Button(w,text='PAPER',font=('Arial Bold',10),bg='#1FAB89',fg='white',padx=34,pady=15,command=lambda: display('PAPER')).grid(row=3,column=2,padx=40,pady=20)
    Button(w,text='SCISSOR',font=('Arial Bold',10),bg='#1FAB89',fg='white',padx=28,pady=15,command=lambda: display('SCISSOR')).grid(row=3,column=3,padx=40,pady=20)


from random import * 
us=cs=0 
#us-user score,cs-computer score
uc=cc=''
#uc-user choice,cc-computer choice
l=[]

def display(type):
    global us,cs,l,uc,cc
    uc=type
    Label(w,text='Your  Choice :',font=('Arial',17),bg='#1FAB89',fg='white').grid(row=4,column=0,columnspan=2,padx=10,pady=20)
    db1=Entry(w,width=35)
    db1.grid(row=4,column=2,columnspan=3,padx=20,pady=20)
    db1.insert(0,uc)

    Label(w,text='Computer  Choice :',font=('Arial',17),bg='#1FAB89',fg='white').grid(row=6,column=0,columnspan=2,padx=10,pady=20)
    db2=Entry(w,width=35)
    db2.grid(row=6,column=2,columnspan=3,padx=20,pady=20)
    l=['ROCK','PAPER','SCISSOR'] 
    cc=choice(l)
    db2.insert(0,cc)
    
    if uc==cc: 
        messagebox.showinfo('','***LEVEL TIE*** \n\n Click OK To Know Scores')
        us+=0
        cs+=0
    else:
        if (uc=='ROCK' and cc=='SCISSOR') or (uc=='SCISSOR' and cc=='PAPER') or (uc=='PAPER' and cc=='ROCK'): 
            messagebox.showinfo('','***HURRAY ! YOU WON*** \n\n Click OK  To Know Scores')
            us+=1
        else:
            messagebox.showinfo('','***OOPS ! YOU LOST*** \n\n Click OK To Know Scores')
            cs+=1
    
    Label(w,text='Your  Score :',font=('Arial',17),bg='#1FAB89',fg='white').grid(row=8,column=0,columnspan=2,padx=10,pady=20)
    db3=Entry(w,width=35)
    db3.grid(row=8,column=2,columnspan=3,padx=20,pady=20)
    db3.insert(0,us)

    Label(w,text='Computer  Score :',font=('Arial',17),bg='#1FAB89',fg='white').grid(row=9,column=0,columnspan=2,padx=10,pady=20)
    db4=Entry(w,width=35)
    db4.grid(row=9,column=2,columnspan=3,padx=20,pady=20)
    db4.insert(0,cs)

    Button(w,text='END GAME',font=('Arial Bold',10),bg='#1FAB89',fg='white',padx=30,pady=13,command=end).grid(row=10,columnspan=6,padx=10,pady=10)


def end():
    w.destroy()
    


from tkinter import *
from tkinter import messagebox
w=Tk()
w.title("Rock Paper Scissor Game")
w.geometry('600x900')
w.config(bg='#9DF3C4')
Label(w,text='* Welcome  to  Rock  Paper  Scissor  Game *',font=('Arial',15),bg='#1FAB89',fg='white').grid(row=0,columnspan=6,padx=60,pady=20)
Button(w,text='START',font=('Arial Bold',10),bg='#1FAB89',fg='white',padx=30,pady=13,command=start).grid(row=1,columnspan=6,padx=40,pady=20)
w.mainloop()