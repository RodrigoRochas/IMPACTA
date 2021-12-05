/*
use master
go

DROP DATABASE M4_compras_mercearia;
GO
*/

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- AC1 - DDL - Cria��o da base
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

CREATE DATABASE M4_compras_mercearia;
GO
USE M4_compras_mercearia;
GO

CREATE TABLE Fornecedor (
ID INT NOT NULL IDENTITY(1,1)
, Nome VARCHAR(50) NOT NULL
, CONSTRAINT PK_Fornecedor PRIMARY KEY ( ID )
)
GO
CREATE TABLE Produto (
ID INT NOT NULL IDENTITY(1,1)
, Nome VARCHAR(50) NOT NULL
, ID_FornecedorPadrao INT NOT NULL  --NULL se fornecedor for opcional
									--NOT NULL se fornecedor for obrigatorio
, CONSTRAINT PK_Produto PRIMARY KEY ( ID )
, CONSTRAINT FK_ProdutoFornecedorPadrao FOREIGN KEY ( Id_FornecedorPadrao ) REFERENCES
Fornecedor( ID )
)
GO
CREATE TABLE Compra (
NF VARCHAR(15) NOT NULL
, DiasEntrega TINYINT NOT NULL
, Valor FLOAT NOT NULL
, Data DATE NOT NULL
, CONSTRAINT PK_Compra PRIMARY KEY ( NF )
)
GO

--Neste modelo 1 compra pode ter N itens cada item pode vir de um fornecedor diferente
CREATE TABLE ItemCompra (
ID_Produto INT NOT NULL
, ID_Fornecedor INT NOT NULL
, NF_Compra VARCHAR(15) NOT NULL
, QTDE INT NOT NULL
, CONSTRAINT PK_ItemCompra PRIMARY KEY ( ID_Produto, ID_Fornecedor, NF_Compra )
, CONSTRAINT FK_ItemCompraProduto FOREIGN KEY ( ID_produto ) REFERENCES PRODUTO ( ID )
, CONSTRAINT FK_ItemCompraFornecedor FOREIGN KEY ( ID_fornecedor) REFERENCES Fornecedor ( ID )
, CONSTRAINT FK_ItemCompraCompra FOREIGN KEY ( NF_Compra ) REFERENCES Compra ( NF )
)
GO

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- AC2 - DML - Carga da base
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

INSERT INTO Fornecedor ( Nome )
VALUES	( 'Ambev' )
	,	( 'P&G' ) 	
	,	( 'Dist. PPG' )

--N�o foi definido quem � o fornecedor padr�o, ent�o, tive que estabelecer um
INSERT INTO Produto ( nome, ID_FornecedorPadrao )
VALUES ( 'Skol', (SELECT id from Fornecedor WHERE nome = 'Ambev') )
	,  ( 'Fralda Pampers', (SELECT id from Fornecedor WHERE nome = 'P&G') )

INSERT INTO Compra ( NF, DiasEntrega, Valor, [Data] )
VALUES ( '#112434', 3, '8243.00', '20171021' )
	,  ( '#324235', 10, '1123.00', '20171021' )
	,  ( '#455464', 2, '500.00', '20171026' )

--Neste modelo 1 compra pode ter N itens cada item pode vir de um fornecedor diferente
INSERT INTO ItemCompra ( ID_Produto, ID_Fornecedor, NF_Compra, QTDE )
VALUES (	(SELECT id FROM Produto WHERE nome = 'Skol')	
		,	(SELECT id FROM Fornecedor WHERE nome = 'Ambev')	
		,	'#112434'--Se j� sei o ID da Compra, basta utiliz�-lo, n�o preciso busc�-lo
		, 300
	),  (	(SELECT id FROM Produto WHERE nome = 'Fralda Pampers')	
		,	(SELECT id FROM Fornecedor WHERE nome = 'P&G')	
		,	'#324235'--Se j� sei o ID da Compra, basta utiliz�-lo, n�o preciso busc�-lo
		, 25
	),  (	(SELECT id FROM Produto WHERE nome = 'Fralda Pampers')	
		,	(SELECT id FROM Fornecedor WHERE nome = 'Dist. PPG')	
		,	'#455464'--Se j� sei o ID da Compra, basta utiliz�-lo, n�o preciso busc�-lo
		, 10
	)

--Confer�ncias:
select * from Fornecedor
select * from Produto
select * from Compra
select * from ItemCompra

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- AC3 + AC4 - DQL
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

/*AC3:*/
-- Lista com o nome dos produtos dispon�veis no cadastro.
SELECT nome FROM Produto

-- Lista com o n�mero da nota fiscal das compras cuja data seja superior � 01/01/2017 e Dias para entrega superior � 10.
SELECT	NF
FROM	Compra
WHERE	[Data] >= '20170101'
		AND DiasEntrega >= 10

-- Lista com o Nome do produto, o nome do fornecedor e a quantidade fornecida.
SELECT	produto.nome as [Nome do Produto]
		, fornecedor.nome as [Nome do Fornecedor]
		, ItemCompra.qtde as [Quantidade Fornecida]
FROM	Produto
		INNER JOIN ItemCompra ON produto.id = ItemCompra.ID_Produto
		INNER JOIN Fornecedor ON Fornecedor.id = ItemCompra.ID_Fornecedor

-- Lista com o nome dos produtos e seus respectivos fornecedores padr�o.
SELECT	produto.nome as [Nome do Produto]
		, fornecedor.nome as [Nome do Fornecedor Padr�o]
FROM	Produto
		INNER JOIN Fornecedor ON produto.ID_FornecedorPadrao = Fornecedor.id

-- Lista com o n�mero na nota fiscal, o nome do produto, a data, quantidade e valor cobrado.
SELECT	compra.NF as [Nota Fiscal]
		, produto.nome as [Nome do Produto]
		, compra.Data as [Data da Compra]
		, ItemCompra.QTDE as [Quantidade Vendida]
		, compra.Valor as [valor Cobrado]
FROM	Produto
		INNER JOIN ItemCompra ON produto.id = ItemCompra.ID_Produto
		INNER JOIN Fornecedor ON Fornecedor.id = ItemCompra.ID_Fornecedor
		INNER JOIN Compra ON ItemCompra.NF_Compra = compra.NF

/*AC4:*/
-- Lista com o n�mero da nota fiscal das [Compras] realizadas cujo prazo de entrega ainda n�o foi atingido ( usar fun��o de data ).
	--Adiciono os dias de entrega ao dia da compra para calcular o dia estimado
	-- Comparo o dia estimado com hoje e vejo se ele � uma data futura
	SELECT	NF as [N�mero da nota fiscal]
	FROM	Compra
	WHERE	dateadd(day,DiasEntrega,Data) > getdate() --produtos � receber....

-- Lista com um ranking dos TOP 10 produtos mais comprados ( pela quantidade )
SELECT	TOP 10 Produto.Nome, SUM(ItemCompra.QTDE) as [Total Comprado]
FROM	Produto
		INNER JOIN ItemCompra ON produto.id = ItemCompra.ID_Produto
GROUP BY Produto.nome
ORDER BY [Total Comprado] DESC

-- Lista com o nome dos produtos n�o vendidos nem uma �nica vez no m�s atual ( usar fun��o de data ).
	--Lista de Produtos total menos os vendidos no M�s atual
	SELECT	Produto.nome
	FROM	Produto
	WHERE	Produto.nome NOT IN (
		SELECT	Produto.nome
		FROM	Produto
				INNER JOIN ItemCompra ON produto.id = ItemCompra.ID_Produto
				INNER JOIN Compra ON ItemCompra.NF_Compra = compra.NF
		WHERE	YEAR([data]) = YEAR(getdate()) --Ano atual
				AND MONTH([data]) = MONTH(getdate()) --Ano+M�s atual
	)

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- DQL - Replicando o select original ( Extra / Avan�ado )
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

--Replicando select original ( b�sico )
SELECT	produto.nome as [Produto]
		, ItemCompra.QTDE as [QTDE]
		, compra.Data as [Data Compra]
		, compra.DiasEntrega as [Dias Entrega]
		, Fornecedor.nome as [Fornecedor]
		, compra.NF as [N�mero NF]
		, compra.Valor as [Valor]
FROM	Produto
		INNER JOIN ItemCompra ON produto.id = ItemCompra.ID_Produto
		INNER JOIN Fornecedor ON Fornecedor.id = ItemCompra.ID_Fornecedor
		INNER JOIN Compra ON ItemCompra.NF_Compra = compra.NF

--Ajustando Formato de Data e valor( incluindo R$, transformando ',' em '.' e deixando os .00 )
SELECT	produto.nome as [Produto]
		, ItemCompra.QTDE as [QTDE]
		, convert(varchar,compra.Data,103) as [Data Compra]
		, compra.DiasEntrega as [Dias Entrega]
		, Fornecedor.nome as [Fornecedor]
		, compra.NF as [N�mero NF]
		, 'R$'+ REPLACE(
					CONVERT(varchar,
							convert(numeric(10,2),compra.Valor)
					)
				,'.',',') as [Valor]
FROM	Produto
		INNER JOIN ItemCompra ON produto.id = ItemCompra.ID_Produto
		INNER JOIN Fornecedor ON Fornecedor.id = ItemCompra.ID_Fornecedor
		INNER JOIN Compra ON ItemCompra.NF_Compra = compra.NF
/*	DICA: para Valores acima de 1.000,00
	voc� tem que usar 3 replaces...
		de '.' para 'X'
		de ',' para '.'
		de 'X' para ','
*/ 

