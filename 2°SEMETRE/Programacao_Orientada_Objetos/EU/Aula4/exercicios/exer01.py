while True:
    try:
        x = int(input('Digite um numero : '))
        y = int(input('Digite um numero : '))

        z = x / y
        print('O resultado da divisão é ', z)

    except ZeroDivisionError:
        print('Não é possivel dividir por 0')

    except ValueError:
        print('SOMENTE NUMEROS')

    except Exception:
        print('Erro inesperado, contate-nos urgentemente')

    else:
        print('FIM')
        break