numeroUm = float(input('Digite o primeiro numero : '))
numeroDois = float(input('Digite o segundo numero : '))

if numeroUm == numeroDois :
    print(f'Digite numeros diferentes')

elif numeroUm > numeroDois :
    print(f'[{numeroDois} - {numeroUm}]')
else:
    print(f'[{numeroUm} - {numeroDois}]')
