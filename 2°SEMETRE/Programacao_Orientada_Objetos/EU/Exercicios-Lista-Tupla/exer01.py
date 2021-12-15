c = n = 1

lista = []
lista_par = []
listaMedia = []

while c in range(11):
    n = int(input(f'Digite o {c}° numero :'))

    if n % 2 == 0:
        lista_par.append(n)
    lista.append(n)

    c += 1

soma = sum(lista)

media = soma / c

for item in lista:
    if item <= media:
        listaMedia.append(item)

print(f'{lista}')
print(f'O maior numero da lista é {max(lista)}')
print(f'O menor numero da lista é {min(lista)}')
print(f'A quantidade de numeros pares da lista é {lista_par} = {len(lista_par)}')
print(f'A media da lista é {media}')
print(f'Valores abaixo da media {listaMedia}')