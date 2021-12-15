pares = open('pares.txt', 'r')
impares = open('impares.txt', 'r')

numeros = open('numeros ordenados.txt', 'w')

lista = []
for linha in pares:
    lista.append(int(linha))

for linha in impares:
    lista.append(int(linha))

lista.sort()

for n in lista:
    numeros.write(str(n) + '\n')

pares.close()
impares.close()
numeros.close()
