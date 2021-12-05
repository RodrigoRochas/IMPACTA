/*
use master

go
drop database M3_consultorio;
GO
*/
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=--
--=X=-- DDL - Criação da base
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=--
CREATE DATABASE AC3_M3_consultorio;
GO
USE AC3_M3_consultorio;
GO
CREATE TABLE Paciente (
ID INT NOT NULL IDENTITY(1,1)
, Nome VARCHAR(50) NOT NULL
, Telefone INT NULL
, CONSTRAINT PK_Paciente PRIMARY KEY ( ID )
)
GO
CREATE TABLE Sala (
Numero INT NOT NULL
, CONSTRAINT PK_Sala PRIMARY KEY ( Numero )
)
GO
CREATE TABLE Medico (
ID INT NOT NULL IDENTITY(1,1)
, CRM VARCHAR(50) NOT NULL --acrescentado, mas não tenho valores....
, Nome VARCHAR(50) NOT NULL
, Especialidade VARCHAR(30) NULL
, CONSTRAINT PK_Medico PRIMARY KEY ( ID )
)
GO
CREATE TABLE Consulta (
ID INT NOT NULL IDENTITY(1,1)
, ID_Paciente INT NOT NULL
, ID_Medico INT NOT NULL
, NumeroSala INT NOT NULL
, DataHora DATETIME NOT NULL
, Duracao TINYINT NOT NULL
, CONSTRAINT PK_Consulta PRIMARY KEY ( ID )
, CONSTRAINT FK_ConsultaMedico FOREIGN KEY ( Id_medico ) REFERENCES Medico( ID )
, CONSTRAINT FK_ConsultaPaciente FOREIGN KEY ( Id_paciente ) REFERENCES paciente(
ID )
, CONSTRAINT FK_ConsultaSala FOREIGN KEY ( NumeroSala ) REFERENCES Sala( Numero )
)
GO
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=--
--=X=-- DML - Carga da base
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=--
INSERT INTO Paciente( Nome, Telefone )
VALUES ( 'Almir dos Santos', '99923232' )
, ( 'Adamastor Silva', '32324414' )
GO

INSERT INTO Medico( CRM, Nome, Especialidade )
VALUES ( '<não cadastrado>', 'Creusa', 'Dentista' )
, ( '<não cadastrado>', 'Juvenal', 'Psicólogo' )
GO
--salas só existem para garantir integridade referencial em consulta
--poderiam ser substituidas por um check constraint, porém, este dá mais trabalho
--para manutenção ( incluir, retirar salas )
INSERT INTO Sala( Numero )
VALUES ( 9 )
, ( 12 )
GO
INSERT INTO Consulta ( ID_Paciente, ID_Medico, NumeroSala, DataHora, Duracao )
VALUES ( (SELECT id FROM paciente WHERE nome = 'Almir dos Santos')
, (SELECT id FROM medico WHERE nome = 'Creusa')
, 9 --não faz sentido buscar a sala 9 via select
, '20171021 15:00'
, 30
), ( (SELECT id FROM paciente WHERE nome = 'Almir dos Santos')
, (SELECT id FROM medico WHERE nome = 'Juvenal')
, 9 --não faz sentido buscar a sala 9 via select
, '20171023 15:00'
, 15
), ( (SELECT id FROM paciente WHERE nome = 'Adamastor Silva')
, (SELECT id FROM medico WHERE nome = 'Creusa')
, 12 --não faz sentido buscar a sala 9 via select
, '20171026 15:00'
, 60
)
--Conferências:
select * from Sala
select * from Medico
select * from Consulta
select * from Paciente



Execute as seguintes consultas no banco de dados criado:
- Lista com o nome e telefone dos pacientes cadastrados

select nome, telefone FROM Paciente


- Lista com o numero da sala e a data/hora das consultas realizadas pelo médico ‘Juvenal’ ordenadas por dataHora

SELECT numerosala as [Numero da sala]
		, datahora as [data e hora da consulta]
FROM	consulta
		INNER JOIN medico ON medico.ID = consulta.ID_Medico
WHERE	medico.nome = 'Juvenal'		
ORDER BY datahora

- Lista com os nomes dos médicos cuja especialidade = ‘Dentista’
SELECT nome
FROM medico
WHERE Especialidade = 'Dentista'

- Lista o nome dos pacientes que foram atendidos entre ‘01/01/2017 e ‘31/12/2017’

select	paciente.nome
FROM	paciente
		INNER JOIN consulta ON consulta.ID_Paciente = paciente.id
WHERE	consulta.dataHora  between  '20170101 00:00:00.000' AND '20171231 23:59:59.997'

- Lista com o Nome do Médico e Paciente, das consultas cuja duração foi igual ou superior à 60 minutos.

Select	Medico.nome as [nome do medico]
		, Paciente.nome as [nome do paciente]
FROM	Medico
		INNER JOIN consulta
			ON medico.id = consulta.ID_Medico
		INNER JOIN Paciente
			ON paciente.ID = consulta.ID_Paciente
where	duracao >= 60


