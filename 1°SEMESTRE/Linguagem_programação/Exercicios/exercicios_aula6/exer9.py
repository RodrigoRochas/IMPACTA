cont = 0
media_classe = 0

while cont < 5:
    nota1 = float(input('Digite a primeira nota :'))

    while not (nota1 >= 0 and nota1 <= 10):
        print('Digite uma nota valida')
        nota1 = float(input(f'Digite a primeira nota : '))
    
    nota2 = float(input('Digite a segunda nota :'))
    while not (nota2 >= 0 and nota2 <= 10):
        print('Digite uma nota valida')
        nota2 = float(input(f'Digite a segunda nota'))

    media = (nota1 + nota2) / 2
    print(f'A media é : {media:.1f}')
    media_classe += 1
    cont += 1
    cont += 1

print(f'A media da classe é : {media_classe/cont:.2f}')