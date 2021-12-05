create database autorelacionamento
go
use autorelacionamento
go

CREATE TABLE PESSOA (
	id	INT NOT NULL --identity(1,1)
	, nome NVARCHAR(50)
	, data_nascimento DATETIME
	, idade	TINYINT
	, CONSTRAINT PK_pessoa PRIMARY KEY (ID)
)
go
CREATE TABLE DEPENDENCIA (
	id_pessoa1 INT NOT NULL
	, id_pessoa2 INT NOT NULL
	, parentesco VARCHAR(50) NOT NULL
	, CONSTRAINT PK_dependencia 
		PRIMARY KEY ( id_pessoa1, id_pessoa2, parentesco )
	, CONSTRAINT FK_dependencia_p1
		FOREIGN KEY(id_pessoa1) REFERENCES Pessoa(id)
	, CONSTRAINT FK_dependencia_p2
		FOREIGN KEY(id_pessoa2) REFERENCES Pessoa(id)
)
GO

insert into pessoa(id, nome, data_nascimento, idade) 
VALUES ( 1, 'Pedro', '19320331', 78 )
	, ( 2, 'Joana', '19340331', 76 )
	, ( 3, 'Maria', '19680331', 42)
	, ( 4, 'Felipe', '19950221', 15 )

insert into DEPENDENCIA (id_pessoa1, id_pessoa2, parentesco)
values ( 3, 1, 'Filha' )
,	(3, 2, 'Filha' )
,	(1, 2, 'Conjuge' )
,	(4, 3, 'Filho' )

select * from pessoa
select * from DEPENDENCIA

--quem tem dependencia ou relacionamento com quem...
select  p1.nome as [primeira pessoa]
	, dependencia.parentesco
	, p2.nome as [segunda pessoa]
from 	pessoa as p1
	INNER JOIN dependencia
		on p1.id = dependencia.id_pessoa1
	INNER JOIN pessoa as p2
		on dependencia.id_pessoa2 = p2.id




