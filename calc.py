#db-display box
def clear():
    db.delete(0,END)

#nb-number button
def nb(num):
    current_num=db.get()
    clear()
    db.insert(0,current_num+num)

f_num=operator=operation=''

def first_num(sign,calculation):
    global f_num,operator,operation
    operator=sign
    operation=calculation
    f_num=db.get()
    sign_list=['+','-','*','/','^']
    for i in sign_list:
        if i in f_num: f_num=f_num.replace(i,'')
    clear()
    db.insert(0,f_num+operator)

def second_num():
    global f_num,operator,operation
    result=s_num=0
    s_num=db.get().replace(str(f_num)+operator,'')
    clear()
    if operation =='add': 
        result=int(f_num)+int(s_num)
    elif operation =='sub': 
        result=int(f_num)-int(s_num)
    elif operation =='mul': 
        result=int(f_num)*int(s_num)
    elif operation =='div': 
        result=int(f_num)/int(s_num)
    elif operation =='pow': 
        result=int(f_num)**int(s_num)
    else: db.insert(0,text="Invalid input",font=('Arial',10))
    db.insert(0,result)
     

    
from tkinter import *
w=Tk()
w.title("calculator")
db=Entry(w,width=20,font=('Arial',25),bg='black',fg='white',justify=RIGHT)
db.grid(row=0,column=0,columnspan=4,padx=1,pady=1)
add_btn=Button(w,text="+",padx=30,pady=10,font=('arial',14),bg='black',fg='white',command=lambda:first_num('+','add')).grid(row=1,padx=1,pady=1)
sub_btn=Button(w,text="-",padx=33,pady=10,font=('arial',14),bg='black',fg='white',command=lambda:first_num('-','sub')).grid(row=1,column=1,padx=1,pady=1)
mul_btn=Button(w,text="*",padx=35,pady=10,font=('arial',14),bg='black',fg='white',command=lambda:first_num('*','mul')).grid(row=1,column=2,padx=1,pady=1)
div_btn=Button(w,text="/",padx=38,pady=10,font=('arial',14),bg='black',fg='white',command=lambda:first_num('/','div')).grid(row=1,column=3,padx=1,pady=1)

pow_btn=Button(w,text="^",padx=37,pady=10,font=('arial',14),bg='black',fg='white',command=lambda:first_num('^','pow')).grid(row=2,column=3,padx=1,pady=1)
b7=Button(w,text="7",padx=33,pady=10,font=('arial',14),bg='black',fg='white',command=lambda: nb('7')).grid(row=2,column=2,padx=1,pady=1)
b8=Button(w,text="8",padx=30,pady=10,font=('arial',14),bg='black',fg='white',command=lambda: nb('8')).grid(row=2,column=1,padx=1,pady=1)
b9=Button(w,text="9",padx=30,pady=10,font=('arial',14),bg='black',fg='white',command=lambda: nb('9')).grid(row=2,column=0,padx=1,pady=1)

b6=Button(w,text="6",padx=30,pady=10,font=('arial',14),bg='black',fg='white',command=lambda: nb('6')).grid(row=3,column=0,padx=1,pady=1)
b5=Button(w,text="5",padx=30,pady=10,font=('arial',14),bg='black',fg='white',command=lambda: nb('5')).grid(row=3,column=1,padx=1,pady=1)
b4=Button(w,text="4",padx=33,pady=10,font=('arial',14),bg='black',fg='white',command=lambda: nb('4')).grid(row=3,column=2,padx=1,pady=1)
eql=Button(w,text="=",padx=35,pady=72,font=('arial',14),bg='black',fg='white',command=second_num).grid(row=3,column=3,rowspan=3,padx=1,pady=1)

b3=Button(w,text="3",padx=33,pady=10,font=('arial',14),bg='black',fg='white',command=lambda: nb('3')).grid(row=4,column=2,padx=1,pady=1)
b2=Button(w,text="2",padx=30,pady=10,font=('arial',14),bg='black',fg='white',command=lambda: nb('2')).grid(row=4,column=1,padx=1,pady=1)
b1=Button(w,text="1",padx=30,pady=10,font=('arial',14),bg='black',fg='white',command=lambda: nb('1')).grid(row=4,column=0,padx=1,pady=1)

b0=Button(w,text="0",padx=30,pady=12,font=('arial',14),bg='black',fg='white',command=lambda: nb('0')).grid(row=5,column=0,padx=1,pady=1)
clr=Button(w,text="clear",padx=63,pady=12,font=('arial',14),bg='black',fg='white',command=clear).grid(row=5,column=1,columnspan=2,padx=1,pady=1)
w.mainloop()