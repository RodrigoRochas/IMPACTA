def intercala_numeros(lista1, lista2):
    lista3 = []

    for c in range(3):
        lista3.append(lista1[c])
        lista3.append(lista2[c])

    return lista3

lista1 = [2,3,4]
lista2 = [7,8,9]
print(intercala_numeros(lista1, lista2))