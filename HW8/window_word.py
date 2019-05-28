from tkinter import *
from random import *

root = Tk()
root.title('tk')
root.geometry('300x220')
frame = Frame(root)
frame.pack()

words = {'dog': 'собака',
         'cat': 'кошка',
         'night': 'ночь',
         'fish': 'рыба',
         'sun': 'солнце'}

def randomChoice():
    global tr
    word, tr = choice(list(words.items()))
    label2.config(text = word)

def enterFunc():
    if tr == ent.get():
        label4.config(text = 'Угадали')
    else:
        label4.config(text = 'Неверно')
def ex():
    exit()
    
label1 = Label(frame,text = 'Случайное слово:',font='13')
label1.grid()

label2 = Label(frame,font=('13'))
label2.grid()

label3 = Label(frame, text = 'Перевод:',font='13')
label3.grid()

ent = Entry(frame,width = 30)
ent.grid()

label4 = Label(frame, text = '',font='13')
label4.grid()

but1 = Button(frame, text = 'Готово!',width = 14, height = 1,command = enterFunc)
but1.grid()

but2 = Button(frame, text = 'Выход',width = 14, height = 1, command=ex)
but2.grid()

randomChoice()

root.mainloop()
