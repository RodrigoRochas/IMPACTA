def calcula_IMC(altura, peso):
    IMC = peso / (altura ** 2)
    return IMC

def classificar(IMC):
    if IMC < 25:
        print('Normal')
    elif IMC < 30:
        print('Sobrepeso')
    elif IMC < 35:
        print('Obesidade grau 1')
    elif IMC < 40:
        print('Obesidade grau 2')
    else:
        print('Obesidade grau 3')




altura = float(input('Digite sua altura : '))
peso = float(input('Digite seu peso : '))

teste = calcula_IMC(altura, peso)
nada = classificar(teste)

print(f'{teste}')
print(f'{nada}')


