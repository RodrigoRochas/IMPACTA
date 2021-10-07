numA = int(input('Digite o primeiro numero : '))
numB = int(input('Digite o segundo numero : '))
numC = int(input('Digite o terceiro numero : '))

print(f'[{numA, numB, numC}]')

if numA == numB and numB == numC :
    print('Os numeros são iguais')

elif numA > numB and numA > numC :
    print(f'O maior numero é {numA}')

elif numB > numA and numB > numC :
    print(f'O maior numero é {numB}')
else:
    print(f'O maior numero é {numC}')