from random import * 
from string import *
s=[]
p=''
def Easy() :
    global s
    a=cb.get()
    X=list(digits)+list(digits) 
    s=sample(X,int(a)) 

def Moderate():
    global s
    a=cb.get()
    Y=list(ascii_letters) 
    s=sample(Y,int(a) )

def Hard():
    global s
    a=cb.get() 
    Z=list(punctuation) 
    s=sample(Z,int(a))

def generate():
    clear()
    global s,p
    a=cb.get()
    if a=='':
       db.insert(0,"Enter some number..!")
    elif a not in cb['values'] : 
        db.insert(0,"Enter valid number")
    else:
        pass
    p=''.join(map(str,s)) 
    db.insert(0,p)
    
def clear():
    db.delete(0,END)

from tkinter import *
from tkinter import ttk
root=Tk()
root.title("password generator")
root.geometry("700x600")
root.config(bg='#71C9CE')
Label(root,text="*** PASSWORD GENERATOR ***",font=('Arial Bold',14),padx=20,pady=20).grid(row=0,column=0,columnspan=8,padx=50,pady=50)
Label(root,text="Specify your password length : ",font=('Arial Bold',12),padx=17,pady=21).grid(row=1,padx=20,pady=20)
n=StringVar()
cb=ttk.Combobox(root,textvariable=n,width=35)
cb['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
cb.grid(row=1,column=1,columnspan=5)
cb.current()
Label(root,text="Select password complexity : ",font=('Arial Bold',12),padx=20,pady=20).grid(row=2,padx=20,pady=20)
r1=Radiobutton(root,text="Easy",value=0,command=Easy,padx=15,pady=10).grid(row=2,column=1,padx=20,pady=20)
r2=Radiobutton(root,text="Moderate",value=1,command=Moderate,padx=10,pady=10).grid(row=2,column=2,padx=20,pady=20)
r3=Radiobutton(root,text="Hard",value=2,command=Hard,padx=13,pady=10).grid(row=2,column=3,padx=20,pady=20)
Button(root,text="Generate password",font=('Arial Bold',10),padx=15,pady=15,command=generate).grid(row=4,column=1,columnspan=5,padx=20,pady=20)
Label(root,text="Your new password is : ",font=('arial Bold',12),padx=37,pady=18).grid(row=5,padx=20,pady=20)
db=Entry(root,width=37)
db.grid(row=5,column=1,columnspan=5,padx=10,pady=10)
root.mainloop()