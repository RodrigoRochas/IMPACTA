salario = float(input('Digite seu salario : '))

desconto_vinte = salario - ((20 / 100) * salario)
desconto_vinte_cinco = salario - ((25 / 100) * salario)
desconto_trinta = salario - ((30 / 100) * salario)

if salario <= 600 :
    print('Isento')

elif salario > 600 and salario <= 1200 :
    print(f'Desconto de 20%, portanto seu salario será : {desconto_vinte:.2f}')

elif salario > 12000 and salario <= 2000:
    print(f'Desconto de 25%, portanto seu salario será : {desconto_vinte_cinco:.2f}')

else:
    print(f'Desconto de 30%, portanto seu salario será : {desconto_trinta:.2f}')