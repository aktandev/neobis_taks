def calculator(x,y,op):

    if op == '+' and type(x) == int and type(y) == int:
        return x + y
    elif op == '-':
        return  x - y
    elif op == '/':
        return  x / y
    elif op == '*':
        return  x * y
    else :
        return 'unknown value'

print(calculator(6, '+', '&'))