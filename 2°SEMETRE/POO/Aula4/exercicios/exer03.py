def buscar(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print('Indice inexistente')


lista = []

for c in range(0,5):
    nome = str(input('Digite um nome : '))

    lista.append(nome)

print(lista)
print(buscar(lista, 8))


