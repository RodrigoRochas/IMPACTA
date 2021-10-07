lado1 = float(input('Digite o primeiro lado : '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Traingulo')
    if lado1 == lado2 and lado2 == lado3:
        print('Equilátero')
    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print('Escaleno')

    else:
        print('Isosceles')
else:
    print('Não é triangulo')

