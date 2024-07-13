import json
import requests
from tkinter import *
from tkinter import messagebox

def generate():

    clear()
    city_name=searchbox.get()

    try:
        # enter your respective api key in below key variable before running the program...
        key=''
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}'

        server_info=requests.get(url)
        data=server_info.json()

        p=data['main']['pressure']
        pressure_entry.insert(0,str(p)+' hPa')

        w=data['wind']['speed']
        Wind_entry.insert(0,str(w)+' m/s')

        h=data['main']['humidity']
        humidity_entry.insert(0,str(h)+' %')

        d=data['weather'][0]['description']
        description_entry1.insert(0,d)
        description_entry2.insert(0,d)

        t=data['main']['temp']-273
        T=round(t)
        temperature_entry.insert(0,str(T)+'°C')
        
    except Exception as e:
        messagebox.showwarning('warning','Enter valid city')

    
def clear():

    pressure_entry.delete(0,END)
    Wind_entry.delete(0,END)
    humidity_entry.delete(0,END)
    description_entry1.delete(0,END)
    temperature_entry.delete(0,END)
    description_entry2.delete(0,END)

w=Tk()
w.title("weather app")
w.geometry('630x600')

bg1=PhotoImage(file='sky.png')
Label(w,image=bg1).place(x=10,y=10)

searchbox=Entry(w,width=10,justify=CENTER,bg='white',fg='black',font=("elephant",34))
searchbox.place(x=130,y=20)

searchbar=PhotoImage(file='copy of search_icon.png')
Button(w,image=searchbar,padx=2,pady=6,bg='white',command=generate).place(x=475,y=20)

logo=PhotoImage(file='weather_logo.png')
Label(w,image=logo).place(x=170,y=150)

bg2=PhotoImage(file='grass2.png')
Label(w,image=bg2).pack(side=BOTTOM)

Label(w,text=' Pressure ',font=('elephant',20),bg='#C5FF95',fg='white').place(x=10,y=400)
Label(w,text=' Wind ',font=('elephant',20),bg='#C5FF95',fg='white').place(x=170,y=400)
Label(w,text=' Humidity ',font=('elephant',20),bg='#C5FF95',fg='white').place(x=290,y=400)
Label(w,text=' Description ',font=('elephant',20),bg='#C5FF95',fg='white').place(x=450,y=400)

pressure_entry=Entry(w,width=7,bg='#C5FF95',font=('forte',18))
pressure_entry.place(x=30,y=500)

Wind_entry=Entry(w,width=7,bg='#C5FF95',font=('forte',18))
Wind_entry.place(x=170,y=500)

humidity_entry=Entry(w,width=7,bg='#C5FF95',font=('forte',18))
humidity_entry.place(x=310,y=500)

description_entry1=Entry(w,width=13,bg='#C5FF95',font=('forte',18))
description_entry1.place(x=450,y=500)

temperature_entry=Entry(w,width=4,font=('forte',55))
temperature_entry.place(x=375,y=150)

description_entry2=Entry(w,width=12,font=('cooper black',25))
description_entry2.place(x=375,y=240)

w.mainloop()