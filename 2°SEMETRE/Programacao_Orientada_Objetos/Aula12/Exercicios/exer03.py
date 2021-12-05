pares = open('pares.txt', 'r')
impares = open('impares.txt', 'r')
numeros = open('numeros_juntos', 'w')

lista = list()

for linhaPar in pares:
    lista.append(int(linhaPar))
    
for linhaImpar in impares:
    lista.append(int(linhaImpar))
    
lista.sort()

for n in lista:
    numeros.write(str(n) + '\n')
    
print(f'Lista = {lista}')
print(f'Numeros : {numeros}')

pares.close()
impares.close()
numeros.close()
    