numA = int(input('Digite o primeiro numero : '))
numB= int(input('Digite o segundo numero : '))

conta = str(input('Digite a operacação que deseja fazer : '))

print('Operações disponiveis : ')
print('Soma (+)')
print('Subtração (-)')
print('Divisão ( / )')
print('Multiplicação (*)')
print('Porcentagem (%)')

soma = numA + numB
subtracao = numA - numB
divisao = numA / numB
multiplicacao = numA * numB
porcentagem = (numA / 100) * numB


if conta == '+':
    print(f'{numA} + {numB} = {soma}')

elif conta == '-' :
     print(f'{numA} - {numB} = {subtracao}')

elif conta == '/' :
     print(f'{numA} / {numB} = {divisao}')

elif conta == '*' :
     print(f'{numA} * {numB} = {multiplicacao}')

elif conta == '%' :
     print(f'{numA}% de {numB} = {porcentagem}')

else: 
    print('Digite um sinal válido')

