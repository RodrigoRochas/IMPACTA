# LISTAS:
# Sequencias de elementos. Delimitada por colchetes [ ]
lista = [3,4,5,6]

# Listas heterogêneas: Pode conter diferentes tipos de dados 
lista1 = [1, 'asasas', 3.5, 3, 'abc']

# listas vazias
lista2 = []

# função print pode ser utilizada para exibir os itens contidos na lista
print(lista)
print(lista1)
print(lista2)

# Índice: especifica a posição de um item na lista
# Índice inicial é 0
lista = [20, 30, 40, 50]
print(lista[0])


# Índices negativos indicam posições referente ao final da lista
print(lista[-1])


# Listas são mutáveis: podem ser alteradas
lista = [2,3,4,5]
lista[0] = 100
print(lista)

# append: adiciona item ao final da lista
lista = [5,6,7,8]
lista.append(10)
lista.append(20)
print(lista)

# repetição for para percorrer a lista
lista = [10, 20, 30, 40, 50]
for a in lista:
    print(a)

# preencher lista com dados informados pelo usuário
'''
lista = []
for i in range(5):
    n = int(input('Numero: '))
    lista.append(n)
print(lista)
'''
# ---------------------------------------------------
# PRINCIPAIS FUNÇÕES

# len: Retorna o tamanho de uma lista
lista = [3,5,6,7,8,3,4,5]
print(len(lista))

# count: Contar quantas vezes um item aparece na lista
lista = [3,5,6,7,8,3,4,5]
print(lista.count(5))


# index: Retorna o índice da primeira ocorrência de um item
# Se o item não for encontrado retorna uma exceção
lista = [3,5,6,7,8,3,4,5, 10]
print(lista.index(5))

# in: verificar se determinado item existe em uma lista
if 10 in lista:
    print('O numero 10 existe')
    print(lista.index(10))
else:
    print('O numero 10 nao existe')


# insert: insere item em determinada posição
lista = [3,4,5,6,7]
lista.insert(0, 10)         # insert(indice, valor)
print(lista)

# pop: Remove o último item da lista
lista = [3,4,5,6,7]
lista.pop()
print(lista)

# pop: Remove um item pelo indice
lista = [3,4,5,6,7]
lista.pop(0)
print(lista)

# remove: Remove primeira ocorrencia de um item da lista
lista = [3,4,5,4,7,8,9,4]
lista.remove(4)
print(lista)

# remover todas as ocorrencia de um item da lista
while 4 in lista:
    lista.remove(4)
print(lista)

# sort: ordenação da lista
lista = [2,5,1,6,70,2]
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

# min: menor elemento
lista = [4,5,6,7,2,80,2]
print(min(lista))

# max: maior elemento
print(max(lista))

# sum: somatorio da lista
print(sum(lista))

# concatenação de listas
lista1 = [3,5,6,7]
lista2 = [30, 40, 50]
lista3 = lista1 + lista2 + lista1 + lista2
print(lista3)

# ----------------------------------------------
# TUPLAS

# Sequencias de elementos que não podem ser alteradas. 
# Delimitada por parenteses ( )
tupla = (3, 4, 5, 7)

# tuplas vazias
tupla = ()
print(tupla)


# tuplas de 1 elemento (tem uma virgula no final)
tupla = (10,)
print(tupla)

# acesso pelo índice
tupla = (4,5,6)
print(tupla[-1])


# estrutura for pode ser utilizada para percorrer a tupla
tupla = (3,4,5,6)
for a in tupla:
    print(a)

# concatenção de tuplas
tupla1 = (3,4,5)
tupla2 = (40,20)
tupla3 = tupla1 + tupla2
print(tupla3)

# converter listas em tuplas
lista = [3, 4, 5]
tupla = tuple(lista)
print(tupla)

# converter tuplas em listas 
tupla = (3,4,5)
lista = list(tupla)
print(lista)

# exemplo para ordenar a tupla usando conversao para lista
tupla = (4,3,1,20,3,8)
lista = list(tupla)
lista.sort()
tupla = tuple(lista)
print(tupla)
