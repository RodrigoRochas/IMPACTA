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
        print('O RA deve ter 7 digitos')
    except TypeError:
        print('O RA já está cadastrado')



   
print(alunos)
