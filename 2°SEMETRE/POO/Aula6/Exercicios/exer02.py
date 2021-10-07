class Funcionario :
    def __init__(self, nome, sobrenome, salario_mensal) : 
        self.nome = nome
        self.sobrenome = sobrenome
        if salario_mensal > 0:
            self.salario_mensal = salario_mensal
        else:
            self.salario_mensal = 0


    def aumentar_salario(self):
        aumento = self.salario_mensal * 10 / 100
        self.salario_mensal += aumento

    def salario_anual(self):
        return self.salario_mensal * 12


funcionario1 = Funcionario('Rodrigo', 'Rocha', 2000)
funcionario2 = Funcionario('Noelma', 'Santos', 2500)

print(funcionario1.nome, funcionario1.salario_anual())
print(funcionario2.nome, funcionario2.salario_anual())


funcionario1.aumentar_salario()
funcionario2.aumentar_salario()

print(funcionario1.nome, funcionario1.salario_anual())
print(funcionario1.nome, funcionario2.salario_anual())