sexo = str(input('Digite seu sexo : (M ou F) ').upper())
altura = float(input('Digite sua altura : '))
peso_ideal_m = (72.7 * altura) - 58
peso_ideal_f = (62.1 * altura) - 44.7

if sexo == 'M':
    print(f'{sexo}, seu peso ideal é : {peso_ideal_m:.2f}')
else: 
     print(f'{sexo}, seu peso ideal é : {peso_ideal_f:.2f}')