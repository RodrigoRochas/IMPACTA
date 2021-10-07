media_classe = 0
reprovados = 0
aprovados = 0
exames = 0

for cont in range(1,7):
    print(f'\n ======== DADOS DO {cont}° ALUNO ======')
    nota1 = float(input('Digite a primeira nota : '))
    nota2 = float(input('Digite a segunda nota : '))

    media = (nota1 + nota2) / 2
    print(f'Sua média é {media}')
    media_classe += media

    if media <= 3:
        print('REPROVADO :-( ')
        reprovados += 1
    elif media < 7:
        print('EXAME :-| ')
        exames += 1
    else:
        print('APROVADO :-) ')
        aprovados += 1

print(f'A media da classe é {(media_classe/cont):.1f}')
print(f'Total de APROVADOS é {aprovados}')
print(f'Total de REPROVADOS é {reprovados}')
print(f'Total de EXAMES é {exames}')
