lin = int(input(f'Digite o número da linha da torre: '))
while not (lin >= 1 and lin <=8):
    lin = int(input(f'Digite NOVAMENTE o número da linha da torre: '))

col = int(input(f'Digite o número da coluna da torre: '))
while not (col >= 1 and col <=8):
    col = int(input(f'Digite NOVAMENTE o número da coluna da torre: '))

print('     1 2 3 4 5 6 7 8')

for linha in range(1,9):
    print(f'{linha} |', end = ' ')
    for coluna in range(1,9):
       
         
        if lin == linha or col == coluna:
            print(f' x', end = '')
        else:
            print(f' -', end = '')
    print()