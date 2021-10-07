cont_idade = 0
cont_alt = 0
acm_alt = 0
cont_peso = 0

for cont in range(1,5):
    print(f'\n==== DADOS DA PESSOA {cont} ====')
    idade = int(input('Digite a idade: '))
    alt = float(input('Digite a altura: '))
    peso = float(input('Digite o peso: '))

    if idade > 50:
        cont_idade += 1

    if idade >= 10 and idade <= 20:
        acm_alt += alt
        cont_alt += 1
    
    if peso < 40:
        cont_peso += 1

if cont_alt > 0:
    media = acm_alt / cont_alt
else:
    media = 0
 
perc = (cont_peso*100)/cont
print(f'Total pessoas idade > 50 anos: {cont_idade}')
print(f'Média das alturas (idade entre 10 e 20): {media}')
print(f'{perc}% pessoas peso < 40 quilos')