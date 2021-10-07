salario_minimo = 1100
consumo_quilowatt_casa = float(input('Digite seu consumo em quilowatts'))
um_quilowatt = salario_minimo / 500
valor_pago_reais = um_quilowatt * consumo_quilowatt_casa
desconto = (15 / 100) * valor_pago_reais
valor_reais = valor_pago_reais - desconto


print('Um quilowatt custa', um_quilowatt, 'R$')
print('Voce pagara', valor_pago_reais, 'R$, por', consumo_quilowatt_casa, 'quilowatts')
print('Voce pagara' , valor_reais, 'R$', 'com desconto de 15%')
