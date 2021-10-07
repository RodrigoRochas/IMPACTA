lista1 = []
lista2 = []

cont1 = 1
print('************************ 1° LISTA **************')
while cont1 <= 5:
    n = int(input(f'Digite o {cont1}° numero : '))
    lista1.append(n)
    cont1 += 1

print('********************** 2° LISTA *********************')

cont = 1
while cont <= 5:
    n = int(input(f'Digite o {cont}° numero : '))
    lista2.append(n)
    cont += 1

tupla1 = tuple(lista1)
tupla2 = tuple(lista2)

tupla3 = tupla1 + tupla2

print(tupla1)
print(tupla2)

print(tupla3)
