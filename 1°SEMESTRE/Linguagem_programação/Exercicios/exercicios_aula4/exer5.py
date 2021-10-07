nome = str(input('Digite seu nome : '))
salario = float(input('Digite o salario : '))
anos_trabalhados = int(input('Digite anos trabalhados : '))

bonus_maior = ((20 / 100) * salario) + salario
#salario_atualG = salario + bonus_maior

bonus_menor = ((10 / 100) * salario) + salario
#salario_atualP = salario + bonus_menor

if anos_trabalhados >= 5 :
    print(f'{nome} vc tem {anos_trabalhados} anos de XSoftware. Portanto sua remuneração será de R$ {bonus_maior:.2f} == 20%')

else: 
    print(f'{nome} vc tem {anos_trabalhados} anos de XSoftware. Portanto sua remuneração será de R$ {bonus_menor:.2f} == 10%')