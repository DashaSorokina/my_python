value=input("Введите атомный номер элемента:")
if value:
    n=int(value)
    if n==3:
        print("Li")
    elif n==17:
        print("Cl")
    elif n==25:
        print("Mn")
    elif  n==80:
        print("Hg")
    else:
        print("Нет такого")
    
else:
    print("Введите значение:")
