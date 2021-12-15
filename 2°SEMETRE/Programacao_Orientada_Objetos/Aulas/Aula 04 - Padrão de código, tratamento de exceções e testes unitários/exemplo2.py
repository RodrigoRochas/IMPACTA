# Realizar a divisão de dois números inteiros positivos
# Identificar e tratar os possíveis erros.
# Solicitar os dados novamente caso o usuário informar valores inválidos

while True:
    try:
        a = int(input('Primeiro numero:'))
        b = int(input('Segundo numero: '))
        c = a / b
        print('Resultado da divisão: ', c)
    except ValueError:
        print('O numero não é inteiro')
    except ZeroDivisionError:
        print('Ocorreu uma divisão por zero')
    except Exception:                           # erro genérico
        print('Erro inesperado!')
    else:                                       # executa se não houver exceção
        print('Operação realizada com sucesso')
        break                                   # interrompe o loop
