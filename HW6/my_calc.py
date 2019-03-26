a = input('Первое число:')
b = input('Второе число:')
c = input('Введите операцию:')

def calc(a,b,c):
    
    try:
        a=int(a)
        b=int(b)
       
        if c == '+':
            return a+b
        if c == '-':
            return a-b
        if c == '*':
            return a*b
        if c == '/':
            return a/b
    except ValueError:
        print('Это не число')
    except ZeroDivisionError:
        print('Деление на ноль')
        
print(calc(a,b,c))    
