nota1 = float(input('Digite a primeira nota : '))
nota2 = float(input('Digite a segunda nota : '))
nota3 = float(input('Digite a terceira nota : '))

media = (nota1 + nota2 + nota3) / 3
media_exame = 12 - media

if media >= 0 and media < 3 :
    print(f'Sua media é de {media:.2f}, e vc esta REPROVADO')

elif media >= 3 and media < 6:
    print(f'Sua media é de {media:.2f}, e vc esta de EXAME')
    print(f'Voce precisa tirar {media_exame:.2f} para passar de ano')

elif media >= 6 and media <= 10 :
    print(f'Sua media é de {media:.2f}, e vc esta de APROVADO')

elif media < 6:
    print(f'Voce precisa tirar {media_exame:.2f} para passar de ano')

else:
    print('Error')

