

s=[]
n=int(input("Введите число:"))
while n!=3:
    print("Простой todo")
    print("1. Добавить задачу.")
    print("2. Вывести список задач.")
    print("3. Выход.")
    n=int(input("Введите число:"))
    d={}
    if n==1:
        task=input("Сфрмулируйте задачу")
        d["task"]=task
        category = input("Добавьте категорию к задаче: ")
        d["category"] = category
        time = input("Добавьте время к задаче: ")
        d["time"] = time
        s.append(d)
    if n==2:
        for i in s:
            print("Задача:", i["task"], " Категория:", i["category"], " Дата:", i['time'])
