horas_extras = float(input('Digite o numero de horas extras : '))
horas_faltas = float(input('Digite o numero de horas de faltas : '))

H = horas_extras - (2/3 *(horas_faltas))

H_minuto = H * 60

if H_minuto >= 2400:
    print('Prêmio R$ 500,00')
elif H_minuto > 1800:
    print('Prêmio R$ 400,00')
elif H_minuto >= 1200:
    print('Prêmio R$ 300,00')
elif H_minuto >= 600:
    print('Prêmio R$ 200,00')
else:
    print('Prêmio R$ 100,00')