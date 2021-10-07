ano = list()
mes = dict()

for c in range(1,3):
    mes['ano'] = int(input(('Digite o ano : ')))
    mes['mes'] = str(input(('Digite o mes : ')))
    mes['quantidade'] = int(input('Digite a quantidade : '))

    ano.append(mes.copy())

for mes in ano:
    print(mes)

for k, v in mes.items():
    print(f'{k} = {v}')


