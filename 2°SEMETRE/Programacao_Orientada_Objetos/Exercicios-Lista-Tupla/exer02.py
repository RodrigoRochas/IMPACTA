cont = 1
listaPar = []
listaImpar = []

while cont <= 10:
    n = int(input(f'Digite o {cont}° numero :'))

    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)


    cont += 1

print(f'Lista com numeros PARES {listaPar}')
print(f'Lista com numeros IMPARES {listaImpar}')