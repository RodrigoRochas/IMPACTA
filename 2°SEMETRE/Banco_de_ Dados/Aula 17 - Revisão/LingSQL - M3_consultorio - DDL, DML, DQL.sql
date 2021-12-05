/*
use master
go

drop database M3_consultorio;
GO
*/

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- AC1 - DDL - Criação da base
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

CREATE DATABASE M3_consultorio;
GO
USE M3_consultorio;
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
, CONSTRAINT FK_ConsultaPaciente FOREIGN KEY ( Id_paciente ) REFERENCES paciente( ID )
, CONSTRAINT FK_ConsultaSala FOREIGN KEY ( NumeroSala ) REFERENCES Sala( Numero )
)
GO

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- AC2 - DML - Carga da base
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

INSERT INTO Paciente( Nome, Telefone )
VALUES	( 'Almir dos Santos', '99923232' )
	,	( 'Adamastor Silva', '32324414' )
GO
INSERT INTO Medico( CRM, Nome, Especialidade )
VALUES	( '<não cadastrado>', 'Creusa', 'Dentista' )
	,	( '<não cadastrado>', 'Juvenal', 'Psicólogo' )
GO
--salas só existem para garantir integridade referencial em consulta
--poderiam ser substituidas por um check constraint, porém, este dá mais trabalho para manutenção ( incluir, retirar salas )
INSERT INTO Sala( Numero ) 
VALUES	( 9 )
	,	( 12 )
GO
INSERT INTO Consulta ( ID_Paciente, ID_Medico, NumeroSala, DataHora, Duracao )
VALUES (	(SELECT id FROM paciente WHERE nome = 'Almir dos Santos')
		,	(SELECT id FROM medico WHERE nome = 'Creusa')
		,	9 --não faz sentido buscar a sala 9 via select
		,	'20171021 15:00'
		, 30
	), (	(SELECT id FROM paciente WHERE nome = 'Almir dos Santos')
		,	(SELECT id FROM medico WHERE nome = 'Juvenal')
		,	9 --não faz sentido buscar a sala 9 via select
		,	'20171023 15:00'
		, 15
	), (	(SELECT id FROM paciente WHERE nome = 'Adamastor Silva')
		,	(SELECT id FROM medico WHERE nome = 'Creusa')
		,	12 --não faz sentido buscar a sala 9 via select
		,	'20171026 15:00'
		, 60
	)

--Conferências:
select * from Paciente
select * from Medico
select * from Sala
select * from Consulta

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- AC3 + AC4 - DQL
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

/*AC3:*/
-- Lista com o nome e telefone dos pacientes cadastrados
SELECT nome, telefone FROM Paciente

-- Lista com o numero da sala e a data/hora das consultas realizadas pelo médico ‘Juvenal’ ordenadas por dataHora
SELECT	consulta.NumeroSala, consulta.DataHora
FROM	medico
		INNER JOIN consulta ON medico.ID = consulta.ID
WHERE	medico.nome = 'Juvenal'
ORDER BY consulta.DataHora 

-- Lista com os nomes dos médicos cuja especialidade = ‘Dentista’
SELECT	nome
FROM	medico
WHERE	especialidade = 'Dentista'

-- Lista o nome dos pacientes que foram atendidos entre ‘01/01/2017 e ‘31/12/2017’
SELECT	DISTINCT paciente.nome --para não duplicar os nomes
FROM	paciente
		INNER JOIN Consulta ON paciente.id = consulta.ID_Paciente
WHERE	DataHora BETWEEN '20170101' AND '20171231'

-- Lista com o Nome do Médico e Paciente, das consultas cuja duração foi igual ou superior à 60 minutos.
SELECT	DISTINCT --para não duplicar os nomes 
		paciente.nome as [Nome do Paciente]
		, medico.nome as [Nome do Medico]
FROM	paciente
		INNER JOIN Consulta ON paciente.id = consulta.ID_Paciente
		INNER JOIN Medico ON consulta.ID_Medico = medico.ID
WHERE	duracao >= 60

/*AC4:*/
-- Lista com o ranking dos top 10 médicos que mais atenderam na sala 9.
SELECT	TOP 10 medico.nome, count(*) as TotalConsultas
FROM	medico
		INNER JOIN consulta ON medico.ID = consulta.ID
WHERE	consulta.numeroSala =9
GROUP BY medico.nome
ORDER BY TotalConsultas DESC

-- Lista com o Numero de médicos por especialidade
SELECT	Especialidade, COUNT(*) as NumeroMedicos
FROM	Medico
GROUP BY Especialidade

-- Lista com o nome e telefone dos pacientes que não se consultaram nenhuma vez neste ano ( usar função de data ).
	-- Lista de pacientes menos os que se consultaram este ano
	SELECT	Paciente.nome
	FROM	Paciente
	WHERE	Paciente.nome NOT IN 
		(	SELECT	Paciente.nome				
			FROM	paciente
					INNER JOIN Consulta ON paciente.id = consulta.ID_Paciente
			WHERE	YEAR(DataHora) = YEAR(GETDATE()) --ano atual
		)

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- DQL - Replicando o select original ( Extra / Avançado )
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

--Replicando select original ( básico )
SELECT	Paciente.nome as Paciente
		, Paciente.Telefone as Contato
		, consulta.DataHora as [Consulta(data/hora)]
		, Consulta.Duracao
		, medico.nome as [Médico]
		, medico.Especialidade
		, consulta.NumeroSala as sala
FROM	paciente
		INNER JOIN Consulta ON paciente.id = consulta.ID_Paciente
		INNER JOIN Medico ON consulta.ID_Medico = medico.ID

select getdate() --2020-10-26 22:03:12.353
select convert(varchar,getdate() ) --Out 26 2020 10:03PM
select convert(varchar,getdate(),103 ) --26/10/2020

--Replicando select original ( básico )
--Arrumando a data
SELECT	Paciente.nome as Paciente
		, Paciente.Telefone as Contato
		, convert(varchar,consulta.DataHora,103) 
			+ ' ' + RIGHT('00'+convert(varchar,datepart(hour,consulta.DataHora)),2)
			+ ':' + RIGHT('00'+convert(varchar,datepart(minute,consulta.DataHora)),2)
		as [Consulta(data/hora)]
		, Consulta.Duracao
		, medico.nome as [Médico]
		, medico.Especialidade
		, consulta.NumeroSala as sala
FROM	paciente
		INNER JOIN Consulta ON paciente.id = consulta.ID_Paciente
		INNER JOIN Medico ON consulta.ID_Medico = medico.ID


