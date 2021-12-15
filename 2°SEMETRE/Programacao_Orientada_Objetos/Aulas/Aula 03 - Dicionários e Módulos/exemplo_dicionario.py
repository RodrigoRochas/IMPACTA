# EXEMPLO 1:
# Criar dicionario para armazenar um cadastro de pessoas (CPF e NOME)
cadastro = {123456: 'Paulo', 
            567890: 'Maria', 
            456789: 'Fernando'}

# Imprimir dicionário
print(cadastro)

# Imprimir item do dicionário (acesso pela chave)
print(cadastro[123456])

# Adicionar item no dicionario
cadastro[999999] = 'Joaquim'
cadastro[777777] = 'Pedro'
print(cadastro)

# Alterar item do dicionário
cadastro[123456] = 'Paulo Vieira'
print(cadastro)

# Excluir item do dicionário (função pop)
cadastro.pop(123456)
print(cadastro)

# Verificar se chave existe no dicionário
if 999998 in cadastro:
    print('O CPF está cadastrado')
else:
    print('O CPF não está cadastrado')

# Percorrer o dicionario com estrutura de repetição
for a in cadastro:
    print(a)

for a in cadastro.values():
    print(a)

for a in cadastro:
    print(a, cadastro[a])

# preencher dicionário com dados informados pelo usuário
'''
cadastro = {}
for i in range(5):
    cpf = int(input('CPF: '))
    nome = input('Nome: ')
    cadastro[cpf] = nome
print(cadastro)
'''


# EXEMPLO 2:
# Dicionario para armazenar o RA de um aluno e uma lista com 5 notas
alunos = {123456: [10, 9, 8, 7, 6], 
          456789: [8, 9, 5, 7, 4.5], 
          343434: [7.5, 8, 4, 9, 10]}
print(alunos)

# Exibir lista de notas de um aluno
print(alunos[123456])

# Inserir uma nova nota para um aluno
alunos[123456].append(10)
print(alunos)

# Alterar a nota de um aluno
alunos[123456][0] = 8.0
print(alunos)
