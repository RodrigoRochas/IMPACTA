resp = 's'
total_venda = 0

menu =  'PRODUTO\t\tCÓDIGO\tPREÇO\n'
menu += '--------------------------------\n'
menu += 'Cachorro quente\t100\t1.20\n'
menu += 'Bauru Simples\t101\t1.30\n'
menu += 'Bauru com ovo\t102\t1.50\n'
menu += 'Hamburguer\t103\t1.20\n'
menu += 'Cheeseburguer\t104\t1.30\n'
menu += 'Refrigerante\t105\t1.00\n'
print(menu)

while resp == 's':
    codigo = int(input('\nDigite o código do produto (100-105): '))
    if codigo >= 100 and codigo <= 105:
        quantidade = int(input('Quantas unidades? '))
        if codigo == 100 or codigo == 103:
            preco = 1.2
        elif codigo == 101 or codigo == 104:
            preco = 1.3 
        elif codigo == 102:
            preco = 1.5
        elif codigo == 105:
            preco = 1.0

        total = preco * quantidade
        print(f'Valor a pagar: R$ {total:.2f}')
        total_venda += total
    else:
        print('-->Código inválido!\n')

    resp = input('Deseja comprar mais produtos? (s/n): ').lower()

print('------------------------------------')
print(f'TOTAL DA COMPRA: R$ {total_venda:.2f}')