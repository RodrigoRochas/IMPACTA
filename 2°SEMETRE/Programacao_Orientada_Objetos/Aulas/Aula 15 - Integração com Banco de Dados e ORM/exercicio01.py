# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)

connection.execute("""CREATE TABLE IF NOT EXISTS PACIENTE (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CPF VARCHAR(255),
                        IDADE INTEGER)""")

connection.execute("""CREATE TABLE IF NOT EXISTS MEDICO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CRM VARCHAR(255),
                        ESPECIALIZACAO VARCHAR(255))""")

connection.execute("""CREATE TABLE IF NOT EXISTS EXAME (
                        ID INTEGER PRIMARY KEY,
                        ID_MEDICO INTEGER,
                        ID_PACIENTE INTEGER,
                        DESCRICAO VARCHAR(255),
                        RESULTADO VARCHAR(255))""")


class Paciente(Base):
    __tablename__ = 'PACIENTE'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    cpf = Column('CPF', String(255))
    idade = Column('IDADE', Integer)

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Medico(Base):
    __tablename__ = 'MEDICO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    crm = Column('CRM', String(255))
    especializacao = Column('ESPECIALIZACAO', String(255))

    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao


class Exame(Base):
    __tablename__ = 'EXAME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    id_medico = Column('ID_MEDICO', Integer)
    id_paciente = Column('ID_PACIENTE', Integer)
    descricao = Column('DESCRICAO', String(255))
    resultado = Column('RESULTADO', String(255))

    def __init__(self, id_medico, id_paciente, descricao, resultado):
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        self.descricao = descricao
        self.resultado = resultado


# Criar objetos médico e pacientes
medico1 = Medico('Dr. Rodolfo', '3454343', 'Cardiologista')
paciente1 = Paciente('Maria', '034343434343', 25)
paciente2 = Paciente('João', '06877847457', 30)

# Inserir médico e pacientes no Banco de Dados
session.add(medico1)
session.add(paciente1)
session.add(paciente2)
session.commit()

# criar objetos exames
exame1 = Exame(medico1.id, paciente1.id, "PCR COVID-19", "Negativo")
exame2 = Exame(medico1.id, paciente2.id, "Eletrocardiograma", 'Normal')

# insere os exames no Banco de Dados
session.add(exame1)
session.add(exame2)
session.commit()

# Realiza consultas
lista_medicos = session.query(Medico)
lista_pacientes = session.query(Paciente)
lista_exames = session.query(Exame)

# Exibe os resultados
print('-' * 30)
for m in lista_medicos:
    print(m.id, m.nome, m.crm, m.especializacao)

print('-' * 30)
for p in lista_pacientes:
    print(p.id, p.nome, p.cpf, p.idade)

print('-' * 30)
for e in lista_exames:
    print(e.id, e.id_medico, e.id_paciente, e.descricao, e.resultado)

# exemplod de relação entre tabelas (JOIN)
# SELECT * FROM EXAME, MEDICO, PACIENTE WHERE EXAME.ID_PACIENTE = PACIENTE.ID
# AND EXAME.ID_MEDICO = MEDICO.ID
print('-' * 30)
resultado = session.query(Exame, Medico, Paciente).filter(
    Exame.id_medico == Medico.id, Exame.id_paciente == Paciente.id)
for obj in resultado:
    print(obj.Medico.nome, obj.Paciente.nome, obj.Exame.descricao,
          obj.Exame.resultado)

# fecha conexão
connection.close()
