arquivo = open('numeros.txt', 'r')

soma = 0
for linha in arquivo:
    soma += int(linha)
    print(int(linha))

print("Somatorio: ", soma)

arquivo.close()
