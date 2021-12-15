
def buscar(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print('Indice inexistente')


lista = []
for i in range(5):
    nome = input('Nome: ')
    lista.append(nome)
print(lista)

print(buscar(lista, 8))
