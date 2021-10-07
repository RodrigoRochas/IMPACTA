lista = []
cont = 0
cont_sem_obesidade = 0

while cont < 4:
    altura = float(input(f'Digite a altura da {cont + 1}° pessoa : '))
    peso = float(input(f'Digite a peso da {cont + 1}° pessoa : '))

    imc = peso / (altura ** 2)
    if imc >= 18.5 and imc < 25:
        cont_sem_obesidade += 1

    lista.append(imc)
    print('\n')
    cont += 1

    
    
