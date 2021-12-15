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

connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
           ID INTEGER PRIMARY KEY,
           NOME varchar(255) NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
           ID INTEGER PRIMARY KEY,
           TITULO VARCHAR(255) NOT NULL,
           PAGINAS INT NOT NULL,
           AUTOR_ID INT NOT NULL)""")


class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)

    def __init__(self, nome):
        self.nome = nome


class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255), nullable=False)
    paginas = Column('PAGINAS', Integer, nullable=False)
    autor_id = Column('AUTOR_ID', Integer, nullable=False)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id


autor1 = Autor('Paulo Vieira')
autor2 = Autor('Maria da Silva')
session.add(autor1)
session.add(autor2)
session.commit()

livro1 = Livro('Titulo do livro 1', 300, autor1.id)
livro2 = Livro('Titulo do livro 2', 120, autor2.id)
session.add(livro1)
session.add(livro2)
session.commit()

print('-'*30)
resultado = session.query(Autor)
for obj in resultado:
    print(obj.id, obj.nome)

print('-'*30)
resultado = session.query(Livro)
for obj in resultado:
    print(obj.id, obj.titulo, obj.paginas, obj.autor_id)

connection.close()
