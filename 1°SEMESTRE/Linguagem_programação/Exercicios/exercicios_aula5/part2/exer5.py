n1 = int(input('Digite o numero : '))

if n1 % 10 == 0 and n1 % 5 == 0 and n1 % 2 == 0:
    print('por 10 e por 5 e por 2')
elif n1 % 5 == 0:
    print('por 5')
elif n1 % 2 == 0:
    print('por 2')
else:
    print('por nenhum dos numero')
