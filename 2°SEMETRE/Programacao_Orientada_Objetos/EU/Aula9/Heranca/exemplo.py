class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir_dados(self):
        print(f'NOME : {self.nome}')
        print(f'EMAIL : {self.email}')
        print(f'TELEFONE : {self.telefone}')


class Aluno(Pessoa):                        # CLASSE ALUNO HERDA DA CLASSE PESSOA
    def __init__(self, nome, email, telefone, ra, turma):
        super().__init__(nome, email, telefone)
        self.ra = ra
        self.turma = turma

    def exibir_dados(self):
        super().exibir_dados()
        print(f'RA : {self.ra}')
        print(f'TURMA : {self.turma}')


aluno = Aluno('Rodrigo', 'rodrigo-rochas@live.com', '11974688166', 2101648, 'DS2C')
aluno.exibir_dados()