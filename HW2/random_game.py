n=int(input("Введите число от1 до 4:"))
import random
m=random.randint(1,4)
if m==n:
    print("pobeda")
else:
    if m>n:
        print("Результат больше введенного числа")
    else:
        print("Результат меньше введенного числа")
