print("Простой todo")
print("1. Добавить задачу.")
print("2. Вывести список задач.")
print("3. Выход.")

n=int(input("Введите число:"))
s=[]
while n!=3:
    if n==1:
        s1=input("Сформулируйте задачу:")
        s2=input("Добавьте категорию:")
        s3=input("Время:")
        s4="Задача: "+s1+" Категория: "+s2+" Дата: "+s3
        s.append(s4)
    if n==2:
        for i in s:
             print(i)
    print("Простой todo")
    print("1. Добавить задачу.")
    print("2. Вывести список задач.")
    print("3. Выход.")
    n=int(input("Введите число:"))
    
        
