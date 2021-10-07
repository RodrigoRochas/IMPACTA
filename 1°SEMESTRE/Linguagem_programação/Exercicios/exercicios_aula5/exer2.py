numA = int(input('Digite o primeiro numero : '))
numB = int(input('Digite o primeiro numero : '))
numC = int(input('Digite o primeiro numero : '))

if numA < numB and numA < numC:
    if numB < numC:
        print(f'[{numA}, {numB}, {numC}]')
    else:
        print(f'[{numA}, {numC}, {numB}]')

elif numB < numA and numB < numC:
    if numA < numC:
        print(f'[{numB}, {numA}, {numC}]')
    else:
        print(f'[{numB}, {numC}, {numA}]')
else:
    if numA < numB:
        print(f'[{numC}, {numA}, {numB}]')
    else:
        print(f'[{numC}, {numB}, {numA}]')



# lista = [numA, numB, numC]
# lista.sort(reverse=False)

# print(f'{lista}')


