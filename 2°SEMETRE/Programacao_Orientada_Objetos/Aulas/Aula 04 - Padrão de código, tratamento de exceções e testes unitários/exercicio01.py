try:
    x = int(input('Primeiro valor:'))
    y = int(input('Segundo valor:'))
    z = x / y
    print('O resultado da divisão é:', z)
except ValueError:
    print('O numero não é inteiro')
except ZeroDivisionError:
    print('Ocorreu uma divisao por zero')

