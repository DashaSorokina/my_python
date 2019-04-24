import tkinter
import math
from tkinter import *

def valume(r):
    try:
        return 1/3 *math.pi*(r**3)
    except ValueError:
        print("Ошибка ввода")

def click():
    global t
    t=valume(int(entry.get()))
    label2.config(text=str(t))
    

def to_txt(v):
    with open("out.txt","w") as o:
        o.write(str(v))

def to_html(v):
    with open("out.html","w") as o:
        o.write(str(v))
        
def f():
    if var.get()=="txt":
        return to_txt(t)
    elif var.get()=="HTML":
        return to_html(t)
   
window=tkinter.Tk()
window.geometry('410x250')

label=tkinter.Label(window, text = "Программа для вычисления объема сферы",font=("Arial Bold", 15)).grid(row=0, column=0, columnspan=2)

radius=tkinter.Label(window, text = "Введите радиус:")
radius.grid(row=1, column=0)

entry = tkinter.Entry(window)
entry.grid(row=1, column=1)

radius=tkinter.Label(window, text = "Результат вычислений:")
radius.grid(row=2, column=0)

label2=tkinter.Label(window, text = "")
label2.grid(row=2, column=1)

button=tkinter.Button(window, text='Вычислить', command=click).grid(row=3, column=0, columnspan=2)

var = StringVar(window)
option = OptionMenu(window,var,"txt", "HTML")
option.grid(row=4, column=1)

button_save=tkinter.Button(window, text='Сохранить', command=f).grid(row=4, column=0)


window.mainloop()
