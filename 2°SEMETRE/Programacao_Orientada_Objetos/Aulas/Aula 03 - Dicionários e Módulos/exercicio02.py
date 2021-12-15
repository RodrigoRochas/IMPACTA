'''
Preencha um dicionário com os dados de 5 alunos.
Utilize o ra do aluno como chave e uma lista de três notas como valor.
Solicite os dados ao usuário.
Percorra o dicionário e exiba a média de cada aluno.
'''

alunos = {}
for i in range(5):
    ra = int(input('RA: '))
    lista = []
    for a in range(3):
        nota = float(input('Nota: '))
        lista.append(nota)
    alunos[ra] = lista
print(alunos)

for ra in alunos:
    lista = alunos[ra]
    media = sum(lista) / len(lista)
    print(media)
