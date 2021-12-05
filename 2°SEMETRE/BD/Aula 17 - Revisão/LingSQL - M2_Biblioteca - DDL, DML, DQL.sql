/*
use master
go

DROP DATABASE M2_Biblioteca;
GO
*/
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- AC1 - DDL - Criação da base
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

CREATE DATABASE M2_Biblioteca;
GO
USE M2_Biblioteca;
GO
--Licença acadêmica para sugerir uma chave composta...
--Poderia ser chave artificial = ID
CREATE TABLE Livro (
Nome VARCHAR(255) NOT NULL
, Copia TINYINT NOT NULL --Não é auto incremental
, Status VARCHAR(30) NULL
, CONSTRAINT PK_Livro PRIMARY KEY ( Nome, Copia )
)
GO
CREATE TABLE Cliente (
ID INT NOT NULL IDENTITY(1,1)
, Nome VARCHAR(50) NOT NULL
, Telefone INT NULL --poderia ou deveria ser VARCHAR
, CONSTRAINT PK_Cliente PRIMARY KEY ( ID )
)
GO

CREATE TABLE Emprestimo (
ID INT NOT NULL IDENTITY(1,1)
, Livro VARCHAR(255) NOT NULL
, Copia TINYINT NOT NULL
, ID_Cliente INT NOT NULL
, DataEmprestimo DATETIME NOT NULL
, DataDevolucaoProposta DATETIME NULL
, DataDevolucaoEfetiva DATETIME NULL
, Multa Decimal(6,2)
, CONSTRAINT PK_Emprestimo PRIMARY KEY ( ID )
, CONSTRAINT FK_EmprestimoLivro FOREIGN KEY ( Livro, Copia ) REFERENCES Livro ( Nome, Copia )
, CONSTRAINT FK_EmprestimoCliente FOREIGN KEY ( ID_cliente ) REFERENCES Cliente ( ID )
)
GO

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- AC2 - DML - Carga da base
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

INSERT INTO LIVRO ( nome, copia, [status] )
VALUES	('A arte da Guerra', 1, 'Atrasado')	
	,	('A arte da Guerra', 2, 'Livre')	
	,	('O Pequeno Principe', 1, 'Emprestado')	
GO
INSERT INTO CLIENTE (/*ID, */ nome, telefone )
VALUES	(/*1, */'José da Silva', '991235344')
	,	(/*2, */'Igor Pereira', '33120123')
GO
INSERT INTO Emprestimo ( Livro, Copia, ID_Cliente, DataEmprestimo, DataDevolucaoProposta, DataDevolucaoEfetiva, Multa )
VALUES ( 'A arte da Guerra'
		, 1
		, (SELECT id FROM Cliente where nome = 'José da Silva')
		, '20170810' --DataEmprestimo
		, '20170910' --DataDevolucaoProposta
		, NULL		 --DataDevolucaoEfetiva
		, 11.00		 --Ainda não devolveu, por isso a Multa Número sempre com '.' 
		)
	,	( 'O Pequeno Principe'
		, 1
		, (SELECT id FROM Cliente where nome = 'Igor Pereira')
		, '20170915' --DataEmprestimo
		, '20171015' --DataDevolucaoProposta
		, '20171015' --DataDevolucaoEfetiva
		, NULL		 --Já devolveu, por isso sem Multa
		)

--Conferências:
select * from Livro
select * from Cliente
select * from Emprestimo

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- AC3 + AC4 - DQL
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
/*AC3:*/
-- Lista com o nome dos livros disponíveis ( sem duplicidades ).
	SELECT	DISTINCT Nome 
	FROM	Livro 
-- Lista com o nome e o número da cópia, de cada livro+copia com status = ‘livre’
	SELECT	Nome, copia
	FROM	Livro 
	where	[status] = 'Livre'
-- Lista com o nome do cliente, o livro+copia dos livros emprestados cuja data de devolução proposta já expirou. ( ou seja, estou procurando quais livros estão atrasados, para poder atualizar seus status para atrasado e calcular sua multa ).
	--Sem conferir o status na tabela livro
		SELECT	Cliente.nome, Emprestimo.livro, Emprestimo.Copia
				--supondo R$1,00 de multa por dia de atraso
				, datediff(day,DataDevolucaoProposta,getdate()) as NovaMulta
		FROM	Cliente 
				INNER JOIN Emprestimo ON Cliente.ID = Emprestimo.ID_Cliente
		WHERE	DataDevolucaoEfetiva IS NULL --ainda não devolveu
				AND DataDevolucaoProposta <= getdate() -- está atrasado
	--Conferindo Status na tabela Livro
		SELECT	Cliente.nome, Emprestimo.livro, Emprestimo.Copia, Livro.[status] 
		FROM	Cliente 
				INNER JOIN Emprestimo ON Cliente.ID = Emprestimo.ID_Cliente
				INNER JOIN Livro ON Emprestimo.livro = livro.nome AND Emprestimo.copia = Livro.copia
		WHERE	DataDevolucaoEfetiva IS NULL --ainda não devolveu
				AND DataDevolucaoProposta <= getdate() -- está atrasado

-- Lista com os nomes dos clientes que pegaram emprestados livros no mês atual de Abril de 2018.
	--Olhando o mês atual
		SELECT	DISTINCT Cliente.nome --para não vir o mesmo nome múltiplas vezes
		FROM	Cliente 
				INNER JOIN Emprestimo ON Cliente.ID = Emprestimo.ID_Cliente	
		WHERE 	YEAR(Emprestimo.DataEmprestimo) = YEAR(GETDATE())
				AND MONTH(Emprestimo.DataEmprestimo) = MONTH(GETDATE())
	--Olhando o abril de 2018
		SELECT	DISTINCT Cliente.nome --para não vir o mesmo nome múltiplas vezes
		FROM	Cliente 
				INNER JOIN Emprestimo ON Cliente.ID = Emprestimo.ID_Cliente	
		WHERE 	CONVERT(VARCHAR(6),Emprestimo.DataEmprestimo,112) = '201804' -- ou 201709 para testes
				
-- Lista de Clientes que preencheram o campo Telefone no seguinte formato 912345678
	SELECT	nome
	FROM	Cliente
	WHERE	telefone like '[9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]' --para celular
			--OR telefone like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]' --para telefone fixo

/*AC4:*/
-- Lista com o Ranking dos top 10 livros ( pelo nome ) mais emprestados.
	SELECT	TOP 10 livro.nome, count(*) as totalEmprestimos
	FROM	Emprestimo 
			INNER JOIN Livro ON Emprestimo.livro = livro.nome AND Emprestimo.copia = Livro.copia
	GROUP BY livro.nome
	ORDER BY totalEmprestimos DESC

-- Lista com o nome do cliente, o número de vezes em que ele já pagou uma multa, e o valor total das multas já pagas.
	SELECT	cliente.nome
			, count(multa) as totalMultas --só conta quando "multa IS NOT NULL"
			, SUM(multa) as quantiaMultas
	FROM	Emprestimo 
			--INNER JOIN Livro ON Emprestimo.livro = livro.nome AND Emprestimo.copia = Livro.copia
			INNER JOIN Cliente ON cliente.ID = Emprestimo.ID_Cliente
	GROUP BY cliente.nome

-- Lista dos Livros ( pelo nome ) que não foram emprestado nem uma única vez no ano passado ( usar função de data ).
	--Lista total de livros menos os que foram emprestados no ano passado
	--por Título: nome único do livro ( mais fácil )
		SELECT	DISTINCT livro.nome
		FROM	Livro
		WHERE	livro.nome NOT IN (
				SELECT	livro.nome
				FROM	Emprestimo 
						INNER JOIN Livro ON Emprestimo.livro = livro.nome AND Emprestimo.copia = Livro.copia
				WHERE 	YEAR(Emprestimo.DataEmprestimo) = YEAR(GETDATE())-1 --ano passado
				--WHERE 	YEAR(Emprestimo.DataEmprestimo) = YEAR(DATEADD(year,-1,GETDATE())) --ano passado
		)
	--Por exemplar [livro + cópia] ( mais difícil pois NOT IN só compara 1 valor )
		SELECT	livro.nome, livro.Copia
		FROM	Livro
				LEFT JOIN (
					SELECT	livro.nome, livro.Copia
					FROM	Emprestimo 
							INNER JOIN Livro ON Emprestimo.livro = livro.nome AND Emprestimo.copia = Livro.copia
					WHERE 	YEAR(Emprestimo.DataEmprestimo) = YEAR(GETDATE())-1 --ano passado
				) emprestadosAnoPassado
				ON livro.nome = emprestadosAnoPassado.nome
				AND livro.Copia = emprestadosAnoPassado.copia
		WHERE	emprestadosAnoPassado.nome IS NULL -- quero quem não foi emprestado

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- DQL - Replicando o select original ( Extra / Avançado )
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

--Replicando select original ( básico )
	SELECT	livro.nome as livro
			, livro.copia as copia
			, cliente.nome as EmprestadoPara
			, Emprestimo.DataEmprestimo as Emprestimo
			, Emprestimo.DataDevolucaoProposta as Devolucao
			, Emprestimo.Multa
			, livro.[Status]
	FROM	Livro --Livro é o dado principal, ele não pode sair/ser omitido
			LEFT JOIN Emprestimo ON Emprestimo.livro = livro.nome AND Emprestimo.copia = Livro.copia
			LEFT JOIN Cliente ON Cliente.ID = Emprestimo.ID_Cliente

--Replicando select original ( intermediario )
	--Tratando os NULOS e arrumando as datas
	--Ajustando o valor da multa para pt-br e acrescentando o R$
	SELECT	livro.nome as livro
			, livro.copia as copia
			, ISNULL(cliente.nome,'') as EmprestadoPara
			, ISNULL(CONVERT(varchar,emprestimo.DataEmprestimo,103),'') as Emprestimo
			, ISNULL(CONVERT(varchar,emprestimo.DataDevolucaoProposta,103),'') as Devolucao
			, ISNULL(
				'R$'+ REPLACE(CONVERT(varchar,Emprestimo.Multa),'.',',')
			,'') as Multa
			, livro.[Status]
	FROM	Livro --Livro é o dado principal, ele não pode sair/ser omitido
			LEFT JOIN Emprestimo ON Emprestimo.livro = livro.nome AND Emprestimo.copia = Livro.copia
			LEFT JOIN Cliente ON Cliente.ID = Emprestimo.ID_Cliente

/*	DICA: para valores acima de 1.000,00
	você tem que usar 3 replaces...
		Original: 1,000.00 
		de '.' para 'X' --> 1X000,00 
		de ',' para '.' --> 1X000.00 
		de 'X' para ',' --> 1,000.00

	MAS o SQL não usa os characteres de separador de milhar...
*/


