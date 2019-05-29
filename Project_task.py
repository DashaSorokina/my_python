import tkinter
import json

def from_json(): #экспортируем список из json файла
    data=[]
    try:
        with open('file.json','r') as file: #открываем файл для чтения
            text=file.read() #читаем файл
            if (text!=''):
                parseJson=json.loads(text) #преобразование в словарь
                data=parseJson['tasks'] #список словарей
            file.close()
    except IOError: #если нет файла
        create_delete_datafile()
    return data

def create_delete_datafile():
    file = open('file.json','w')
    file.close()
    show() 
               
def write_json(): #записываем в json файл новую задачу
    data=from_json()
    item={
        'task':str(task_w.get()),
        'category':str(category_w.get()),
        'time':str(time_w.get())
    }
    data.append(item)
    with open('file.json','w') as file:
        text={
            'tasks' : data
        }
        json.dump(text,file) #преобразование словаря в текстовый вид в json формате в переменную file
        file.close()
    show()

def show():
    s = ''
    for i in from_json():
        s+='Задача:{0} Категория:{1} Время:{2}\n'.format(i['task'],i['category'],i['time'])
    tasks_list.config(text=s)

window=tkinter.Tk()
window.geometry('400x300')

label=tkinter.Label(window, text="Менеджер   задач",font=("Arial Bold", 15))
label.place(x=0,y=0)

task=tkinter.Label(window, text="Задача:")
task.place(x=10,y=60)
category=tkinter.Label(window, text="Категория:")
category.place(x=10,y=90)
time=tkinter.Label(window, text="Время:")
time.place(x=10,y=120)

task_w = tkinter.Entry(window)
task_w.place(x=100,y=60)
category_w = tkinter.Entry(window)
category_w.place(x=100,y=90)
time_w = tkinter.Entry(window)
time_w.place(x=100,y=120)

tasks_list = tkinter.Label(window,bg='white')
tasks_list.place(x=300,y=60)

button_add=tkinter.Button(window, text='Добавить',command=write_json)
button_add.place(x=10,y=150)
button_show=tkinter.Button(window, text='Список задач',command=show)
button_show.place(x=10,y=180)
button_clean=tkinter.Button(window, text='Очистить весь список',command=create_delete_datafile)
button_clean.place(x=10,y=210)
button_ex=tkinter.Button(window, text='Выход',command=window.destroy)
button_ex.place(x=10,y=240)

window.mainloop()
