def calculate():

    global in_meters

    Label(w,text="Your BMI is : ",font=('Arial Bold',12),padx=17,pady=21).grid(row=5,padx=20,pady=20)

    result_entry=Entry(w,width=6,font=('Arial Bold',18),justify=CENTER)
    result_entry.grid(row=5,column=3)

    feet=cb1.get()
    inches=cb2.get()
    weight=weight_entry.get()

    try:
        try:
            if int(feet) in range(0,10) and int(inches) in range(0,12):
                total_inches=(int(feet)*12)+int(inches)
                in_meters=(0.0254*total_inches)

        except ValueError:
            messagebox.showerror('Error','Enter valid Height..!')

        bmi=float(weight)/(in_meters*in_meters)
        result_entry.insert(0,round(bmi,2))

        if bmi < 18.5:
            messagebox.showwarning('warning','oops! you are underweight')

        elif bmi > 18.5 and bmi < 25:
            messagebox.showinfo('result','perfect! you weight is normal')

        elif bmi > 25:
            messagebox.showwarning('warning','oops! you are obese')

        else:
            pass

    except ValueError:
        messagebox.showerror('Error','Enter valid Weight..!')
    
    in_meters=0  


from tkinter import *
from tkinter import ttk,messagebox

w=Tk()
w.title("BMI calculator")
w.geometry("550x600")
w.config(bg='#71C9CE')
Label(w,text="*** BMI CALCULATOR ***",font=('Arial Bold',14),padx=20,pady=20).grid(row=0,column=0,columnspan=8,padx=50,pady=50)

#height section

Label(w,text="Enter your height : ",font=('Arial Bold',12),padx=17,pady=21).grid(row=1,padx=20,pady=20)

n=StringVar()
cb1=ttk.Combobox(w,textvariable=n,width=8)
cb1['values']=(0,1,2,3,4,5,6,7,8,9)
cb1.grid(row=1,column=1,columnspan=2)
cb1.current()

Label(w,text='feet',font=('Arial Bold',8),padx=12,pady=1).grid(row=1,column=3)

n=StringVar()
cb2=ttk.Combobox(w,textvariable=n,width=7)
cb2['values']=(0,1,2,3,4,5,6,7,8,9,10,11)
cb2.grid(row=1,column=4,columnspan=2)
cb2.current()

Label(w,text='inches',font=('Arial Bold',8),padx=4,pady=1).grid(row=1,column=6,padx=20)

#weight section

Label(w,text="Enter your weight : ",font=('Arial Bold',12),padx=17,pady=21).grid(row=2,padx=20,pady=20)

weight_entry=Entry(w,width=5,font=('Arial Bold',20),justify=CENTER)
weight_entry.grid(row=2,column=3)

Label(w,text='Kg',font=('Arial Bold',8),padx=4,pady=1).grid(row=2,column=4,padx=20)

#calculate section

Button(w,text="Calculate",font=('Arial Bold',13),padx=30,pady=13,command=calculate).grid(row=4,column=1,columnspan=5,padx=20,pady=20)

w.mainloop()