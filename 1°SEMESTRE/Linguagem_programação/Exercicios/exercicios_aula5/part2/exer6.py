produto = float(input('Digite o valor do produto : '))

lucro45 = produto - ((45 / 100) * produto)
lucro30 = produto - ((30 / 100) * produto)

if produto <= 20:
    print(f'Lucro com 45% = R$ {lucro45:.2f}')
elif produto > 20:
    print(f'Lucro com 30% = R$ {lucro30:.2f}')