codigo_estado = int(input('Digite o código do Estado : '))
codigo_carga = int(input('Digite o código da carga : '))
tonelada = float(input('Digite o peso em toneladas da carga : '))

kg = tonelada * 1000

preco_carga1 = kg * 100
preco_carga2 = kg * 250
preco_carga3 = kg * 340


if codigo_carga >= 10 and codigo_carga <= 20:
    print(f'O preço da carga é: {preco_carga1} * 100')
elif codigo_carga > 20 and codigo_carga <= 30:
    print(f'O preço da carga é: {preco_carga2} * 250')
elif codigo_carga > 30 and codigo_carga <= 40:
    print(f'O preço da carga é: {preco_carga3} * 340')
else:
    print('Digite um código de carga válido')

if codigo_estado == 1:
    print(f'{pre}')