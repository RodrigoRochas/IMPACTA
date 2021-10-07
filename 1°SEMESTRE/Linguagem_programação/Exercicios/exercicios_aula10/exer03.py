def calcula_media(nota1, nota2, nota3):
    soma = nota1 + nota2 + nota3
    media = soma / 3
    return media


def validar_nota(nota):
    while not(nota >=0 and nota <= 10 ):
        print('Error')
        nota = float(input('Digite novamente : '))

    return nota

nota1 = float(input('Digite a 1° nota : '))
nota1 = validar_nota(nota1)

nota2 = float(input('Digite a 2° nota : '))
nota2 = validar_nota(nota2)

nota3 = float(input('Digite a 3° nota : '))
nota3 = validar_nota(nota3)


print(f'{calcula_media(nota1, nota2, nota3)}')