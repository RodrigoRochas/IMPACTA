# INSTALAR O MÓDULO SQLALCHEMY
# Executar no terminal o comando: pip install sqlalchemy

# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import false

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)

# SCRIPT PARA CRIAR UMA NOVA TABELA NO BANCO DE DADOS
connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        IDADE INT,
                        SALARIO FLOAT)
                    """)

class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


# -----------------------------------------------------------------------------
# INSERINDO DADOS NA TABELA


# Inserir um objeto
func = Funcionario('Zezinho', 20, 1700)
session.add(func)
session.commit()

# Inserir uma lista de objetos
func1 = Funcionario('Luizinho', 22, 1250)
func2 = Funcionario('Huguinho', 22, 2200)
lista = [func1, func2]
session.add_all(lista)
session.commit()

# Inserir objetos cadastrados pelo usuário
lista = []
while True:
    nome = input('Informe o nome (digite SAIR para finalizar): ')
    if nome == 'SAIR':
        break
    idade = int(input('Informe a idade: '))
    salario = float(input('Informe o salario: '))
    func = Funcionario(nome, idade, salario)
    lista.append(func)
session.add_all(lista)
session.commit()

# -----------------------------------------------------------------------------
# CONSULTANDO OS DADOS DA TABELA

# Consultar todos os dados
print('-'*30)
resultado = session.query(Funcionario)      # select * from funcionario
for func in resultado:
    print(func.id, func.nome, func.idade, func.salario)

# Consultar utilizando filtros (salario maior que 1500)
print('-'*30)
resultado = session.query(Funcionario).filter(Funcionario.salario > 1500)
for func in resultado:
    print(func.id, func.nome, func.idade, func.salario)

# Consultar utilizando filtros (salário maior que 1500 e idade igual a 22)
print('-'*30)
resultado = session.query(Funcionario).filter(Funcionario.salario > 1500, Funcionario.idade == 22)
for func in resultado:
    print(func.id, func.nome, func.idade, func.salario)

# Consultar utilizando filtros (salario maior que 1500)
print('-'*30)
resultado = session.query(Funcionario).filter(Funcionario.salario > 1500).order_by(Funcionario.nome)
for func in resultado:
    print(func.id, func.nome, func.idade, func.salario)

# consultar pela chave primaria
print('-'*30)
obj = session.query(Funcionario).get(6)
if obj is not None:
    print(obj.id, obj.nome, obj.idade, obj.salario)
else:
    print('ID inexistente')

# consulta utilizando TOP 1
print('-'*30)
obj = session.query(Funcionario).filter(Funcionario.nome == 'Paulo').first()
if obj is not None:
    print(obj.id, obj.nome, obj.idade, obj.salario)
else:
    print('Funcionario nao existe')

# consulta usando a função LIKE
print('-'*30)
lista = session.query(Funcionario).filter(Funcionario.nome.like('%inho%'))
for obj in lista:
    print(obj.id, obj.nome, obj.idade, obj.salario)

# -----------------------------------------------------------------------------
# ALTERANDO DADOS

# altera os dados de um objeto
obj = session.query(Funcionario).get(6)
if obj is not None:
    obj.idade = 41
    obj.nome = 'Fernando da Silva'
    session.commit()

# aumenta o salario de todos os funcionario em 10%
'''
lista = session.query(Funcionario)
for obj in lista:
    obj.salario += obj.salario * 0.10
session.commit()
'''
# -----------------------------------------------------------------------------
# EXCLUINDO DADOS

# exclui um objeto
obj = session.query(Funcionario).get(2)
if obj is not None:
    session.delete(obj)
    session.commit()

# -----------------------------------------------------------------------------
# CONSULTANDO TODOS OS DADOS
print('-'*30)
lista = session.query(Funcionario)
for obj in lista:
    print(obj.id, obj.nome, obj.idade, obj.salario)

# -----------------------------------------------------------------------------
# FECHANDO CONEXÃO COM BANCO DE DADOS
connection.close()
