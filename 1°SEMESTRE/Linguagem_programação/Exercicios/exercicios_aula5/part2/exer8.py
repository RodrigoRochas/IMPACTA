mesada = float(input('Digite sua mesada : '))

pergunta = str(input('Deseja comprar algum produto (s/n) : '))

if pergunta == 's':
    produto = float(input('Qual o valor do produto ? '))
    print(f'Sua mesada passara a ser R$ {mesada - produto}')
else:
    print(f'Sua mesada é R$ {mesada}')

























# resp = 's'
# acm_num = 0
# cont = 0

# while resp == 's':
#     num = int(input('Digite um numero : '))
#     acm_num += num

#     cont += 1
#     resp = input('Deseja continuar (s/n)').lower()

# print(f'O LOOP executou {cont} vezes')
# print(f'A soma é {acm_num}')
