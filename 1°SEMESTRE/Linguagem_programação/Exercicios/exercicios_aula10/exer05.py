# def inverter(num):
#     lista_str = list(str(num))
#     tam = len(lista_str)
#     reverso = ''
#     for i in range(tam):
#         reverso += lista_str[tam-1 - i]
#                             # 3-1 = 2 - 0 = 2
#                             # 3-1 = 2 - 1 = 1
#                             # 3-1 = 2 - 2 = 0
#     return int(reverso)

# num = int(input('Digite um número: '))
# numero_reverso = inverter(num)
# print(f'{num} => {numero_reverso}')




# def converter_mes(mes):
#     meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
#              'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
#     return meses[mes - 1]


# data = input('Digite uma data (dd/mm/aaaa):')
# data_separada = data.split('/')
# mes_extenso = converter_mes(int(data_separada[1]))
# print(f'Você nasceu em {data_separada[0]} de {mes_extenso} de {data_separada[2]}')



















# # # nomes = [''] * 5
# # # produtos = [0] * 5

# # # for i in range(len(nomes)):
# # #     nomes[i] = str(input('Digite o produto : '))
# # #     produtos[i] = float(input('Digite o qtde : '))


# # # busca = float(input('Digite a busca'))

# # # lista_nomes = []
# # # for i in range(len(produtos)):
# # #     if produtos[i] == busca:
# # #         lista_nomes.append(nomes[i])

# # # for i in range(len(lista_nomes)):
# # #     print(lista_nomes[i])

# # nomes = ['']*5
# # estoques = [0]*5

# # for i in range(len(nomes)):
# #     nomes[i] = input()
# #     estoques[i] = int(input())

# # maior_estoque = estoques[0]
# # nome_maior = ''
# # menor_estoque = estoques[0]
# # nome_menor = ''

# # for i in range(len(estoques)):
# #     if estoques[i] > maior_estoque:
# #         maior_estoque = estoques[i]
# #         nome_maior = nomes[i]

# #     if estoques[i] < menor_estoque:
# #         menor_estoque = estoques[i]
# #         nome_menor = nomes[i]


# # print(nome_menor)
# # print(nome_maior)
