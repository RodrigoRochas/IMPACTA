def funcao_1():
    print('Início da função')
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        for i in range(15):
            print(lista[i])
    except IndexError:
        print('Indice inexistente')
    print('Fim da função')


print('Início do programa')
funcao_1()
print('Fim do programa')