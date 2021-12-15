alunos = {}
for i in range(5):
    try:
        ra = int(input('RA: '))
        if len(str(ra)) != 7:
            raise ValueError
        if ra in alunos:
            raise TypeError
        nome = input('Nome: ')
        alunos[ra] = nome
    except ValueError:
        print('O RA nao tem 7 dígitos')
    except TypeError:
        print('O RA ja está cadastrado')

print(alunos)