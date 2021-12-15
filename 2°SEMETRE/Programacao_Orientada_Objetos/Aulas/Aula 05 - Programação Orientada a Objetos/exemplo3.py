'''
Criar uma classe Aluno
- Atributos: ra, nome, email, lista de notas.
- Métodos: inserir_nota, calcular_media
'''


class Aluno:
    def __init__(self, ra, nome, email):
        self.ra = ra
        self.nome = nome
        self.email = email
        self.lista_notas = []

    def inserir_nota(self, nota):
        self.lista_notas.append(nota)

    def calcular_media(self):
        media = sum(self.lista_notas) / len(self.lista_notas)
        return media


aluno1 = Aluno(12345, "João", "joao@email.com")
aluno2 = Aluno(56789, "Maria", "maria@email.com")

aluno1.inserir_nota(9)
aluno1.inserir_nota(8)

aluno2.inserir_nota(7)
aluno2.inserir_nota(6.5)
aluno2.inserir_nota(8)

print("Média do aluno", aluno1.nome, ":", aluno1.calcular_media())
print("Média do aluno", aluno2.nome, ":", aluno2.calcular_media())
