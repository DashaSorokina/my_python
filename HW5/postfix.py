def calc(expr):
    '''
    >>> calc("1 2 + 4 * 3 +")
    '15'
    >>> calc("1 2 3 * + 2 -")
    '5'
    '''

    stack=[]
    for i in expr:
        if i.isdigit():
            stack.append(int(i))
        elif i == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b)+int(a))
        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b)-int(a))
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b)*int(a))
        elif i=='/':
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b)/int(a))
            

    return str(stack[0])


print(calc("1 2 + 4 * 3 +"))

import doctest
doctest.testmod()
