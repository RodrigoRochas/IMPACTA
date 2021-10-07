cont_idade_peso = 0
cont_azul = 0
cont_atl = 0

for cont in range(1, 4):
    print(f'======= DADOS DA {cont}a PESSOA ========')
    idade = int(input('Digite a idade: '))
    peso = float(input('Digite o peso: '))
    alt = float(input('Digite a altura: '))

    olho = input('Digite a cor do olho (a,p,v,c): ').lower()
    while not (olho == 'a' or olho == 'p' or olho == 'v' or olho == 'c'):
        print('-->Cor do olho inválida!')
        olho = input('Digite a cor do olho (a,p,v,c): ')

    if alt > 1.68 and olho != 'v':
        cont_atl += 1

print(f'Total pessoas idade > 50 e peso < 60: {cont_idade_peso}')
print(f'{((cont_azul*100)/cont):.2f}% de pessoas olho azul')
print(f'Total pessoas alt > 1.68 e sem olho verde: {cont_atl}')