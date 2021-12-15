arquivo = open('numeros.txt', 'w')

for i in range(10):
    n = int(input('Informe um número inteiro:'))
    arquivo.write(str(n) + '\n')

arquivo.close()
