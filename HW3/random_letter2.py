import random
s=['самовар','весна', 'лето']
m=random.choice(s)
a=random.choice(m)
b=m.index(a)
lst=list(m)
lst[b]='?'
print(''.join(lst))
k=input("Введите букву:")
while  k!=a:
  k=input("lose,  Введите букву:")
else:
    print("win")
