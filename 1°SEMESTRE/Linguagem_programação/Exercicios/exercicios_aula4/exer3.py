numeroUm = int(input('Digite o primeiro numero : '))
numeroDois = int(input('Digite o segundo numero : '))

if numeroUm == numeroDois :
    print('Numeros iguais')

elif numeroUm > numeroDois :
    print(f'{numeroUm} - {numeroDois} = {numeroUm - numeroDois}')

else:
    print(f'{numeroDois} - {numeroUm} = {numeroDois - numeroUm}')