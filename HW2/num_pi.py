from math import pi
n=int(input("Введите число:"))
def funpi(n):
    return f'{pi:.{n}f}'
print(funpi(n))
