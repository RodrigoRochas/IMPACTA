class Aluno:
    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma

        self.notas = []

    def inserir_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        return media


aluno1 = Aluno(123, 'Rodrigo', 'ADS')
aluno2 = Aluno(456, 'Felipe', 'ADS')
aluno3 = Aluno(789, 'Noelma', 'ADS')

aluno1.inserir_nota(10)
aluno1.inserir_nota(8)

aluno2.inserir_nota(5)
aluno2.inserir_nota(4)

aluno3.inserir_nota(1)
aluno3.inserir_nota(8)

lista = [aluno1, aluno2, aluno3]

for aluno in lista:
    print(aluno.nome, aluno.calcular_media())