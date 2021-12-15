# Valida um número inteiro e positivo

while True:
    try:
        n = int(input('Informe um numero inteiro e positivo: '))
        if n < 0:
            raise TypeError
        print(n*2)
    except ValueError:
        print('O numero não é inteiro')
    except TypeError:
        print('O numero não é positivo')
    else:
        break       # sai do loop
