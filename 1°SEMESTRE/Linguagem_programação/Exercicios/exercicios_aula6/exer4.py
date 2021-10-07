lista = []
cont = 0

while cont < 10:
    num = int(input(f'Digite o {cont + 1}° numero : '))
    lista.append(num)
    lista.sort()
    cont += 1

print(f'{lista}')
print(f'{lista[0]}')
