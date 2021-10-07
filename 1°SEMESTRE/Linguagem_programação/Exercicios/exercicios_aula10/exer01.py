num = int(input('Digite um numero : '))

def verificar(num):
    if num > 0:
        return True
    elif num < 0:
        return False
    else:
        return 'Neutro'

print(verificar(num))

