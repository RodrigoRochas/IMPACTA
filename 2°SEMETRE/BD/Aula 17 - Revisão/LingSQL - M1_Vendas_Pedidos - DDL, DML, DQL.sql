/*
use master
go

DROP DATABASE M1_Vendas_Pedidos;
GO
*/

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- AC1 - DDL - Cria��o da base
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

CREATE DATABASE M1_Vendas_Pedidos;
GO
USE M1_Vendas_Pedidos;
GO

CREATE TABLE Cliente (
ID INT NOT NULL IDENTITY(1,1)
, Nome VARCHAR(50) NOT NULL
, Endereco VARCHAR(255) NULL
, CONSTRAINT PK_Cliente PRIMARY KEY ( ID )
)
GO
CREATE TABLE Telefone (
Id_cliente INT NOT NULL --n�o pode ser autoincremental
, Numero INT NOT NULL --poderia ou deveria ser VARCHAR
, CONSTRAINT PK_Telefone PRIMARY KEY ( Id_cliente, Numero )
, CONSTRAINT FK_TelefoneCliente FOREIGN KEY ( ID_cliente ) 
	REFERENCES Cliente ( ID )
)
GO
CREATE TABLE Produto (
ID INT NOT NULL IDENTITY(1,1)
, Nome VARCHAR(50) NOT NULL
, CONSTRAINT PK_Produto PRIMARY KEY ( ID )
)
GO
CREATE TABLE Pedido (
Numero INT NOT NULL IDENTITY(1,1)
, DataHora DATETIME NOT NULL
, Id_cliente INT NOT NULL
, CONSTRAINT PK_Pedido PRIMARY KEY (Numero )
, CONSTRAINT FK_PedidoCliente FOREIGN KEY ( ID_cliente ) 
	REFERENCES Cliente ( ID )
)
GO
CREATE TABLE ItemPedido (
NumeroPedido INT NOT NULL
, ID_produto INT NOT NULL
, Qtde INT NOT NULL
, CONSTRAINT PK_ItemPedido 
	PRIMARY KEY (NumeroPedido, ID_produto)
, CONSTRAINT FK_ItemPedidoPedido FOREIGN KEY ( NumeroPedido) 
	REFERENCES Pedido ( Numero )
, CONSTRAINT FK_ItemPedidoProduto FOREIGN KEY ( ID_produto) 
	REFERENCES Produto ( ID )
)
GO

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- AC2 - DML - Carga da base
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

INSERT INTO Cliente ( Nome, Endereco ) 
values	( 'Jos�', 'Av. Tr�s, Numero 1')
	,	( 'Maria', 'Av. Impar, nr 33, apto 12')
GO
INSERT INTO Telefone ( id_cliente, Numero )
VALUES	( (select ID from cliente where nome = 'Jos�'), '93783259' )
	,	( (select ID from cliente where nome = 'Jos�'), '87453452' )
	--Maria n�o tem Telefone Cadastrado
GO
INSERT INTO Produto (Nome )
VALUES	( 'Calabresa' )
	,	( 'Frango' )
	,	( 'Br�colis' )
	,	( 'Carne' ) --item extra para os relat�rios

--N�mero do pedido ficou como auto incremental para simplificar
--Jos� com 2 pedidos, maria com 1
-- SET DATEFORMAT DMY
INSERT INTO Pedido ( datahora, id_cliente )
VALUES	( '20/08/2017 23:11', (select ID from cliente where nome = 'Jos�') ) 
	,	( '27/08/2017 22:30', (select ID from cliente where nome = 'Jos�') ) 
	,	( '21/09/2017 19:59', (select ID from cliente where nome = 'Maria') ) 
GO
--Busca em Pedido foi feit pela datahora pois os IDs podem mudar
--Neste caso DataHora � o mais pr�ximo que tenho de um outro campo �nico.
INSERT INTO ItemPedido ( NumeroPedido, ID_produto, Qtde )
VALUES	(	(select Numero from Pedido where datahora = '20/08/2017 23:11')
		  ,	(select id from produto where nome = 'Calabresa')
		  , 3
		)
	, 	(	(select Numero from Pedido where datahora = '27/08/2017 22:30')
		  ,	(select id from produto where nome = 'Frango')
		  , 2
		)
	, 	(	(select Numero from Pedido where datahora = '21/09/2017 19:59')
		  ,	(select id from produto where nome = 'Calabresa')
		  , 7
		)
	, 	(	(select Numero from Pedido where datahora = '21/09/2017 19:59')
		  ,	(select id from produto where nome = 'Br�colis')
		  , 4
		)
--2 pedidos com 1 item cada para o Jos�
--1 pedido com 2 itens para a Maria
GO

--Confer�ncias:
	select * from cliente
	select * from telefone
	select * from produto
	select * from Pedido
	select * from ItemPedido

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- AC3 + AC4 - DQL
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
/*AC3:*/
--Lista com Nome dos produtos dispon�veis
SELECT nome FROM produto

-- Lista com o Numero dos Pedidos realizados entre �01/01/2017� e �31/01/2017�
SELECT numero FROM Pedido WHERE datahora BETWEEN '20170101' AND '20170131 23:59:59.997'

-- Lista com Numero do Pedido, Nome do Produto e quantidade vendida.
SELECT	pedido.Numero, produto.nome, ItemPedido.qtde
FROM	Pedido 
		INNER JOIN ItemPedido ON pedido.Numero = ItemPedido.NumeroPedido
		INNER JOIN Produto ON ItemPedido.ID_produto = produto.ID

-- Lista com Nome e Endere�o do Cliente e, se existirem, seus respectivos telefones.
SELECT cliente.nome, cliente.Endereco, Telefone.numero
FROM	Cliente
		--tem que ser left pois existem clientes sem telefone
		LEFT JOIN Telefone on cliente.id = telefone.Id_cliente

-- Lista com o nome dos clientes que j� compraram, em uma compra, uma quantidade de produtos superior � 10.
	--para 1 item de produto com qtde>=10
		SELECT cliente.nome
		FROM	Cliente
				INNER JOIN Pedido on Cliente.id = Pedido.Id_cliente
				INNER JOIN ItemPedido on pedido.Numero = ItemPedido.NumeroPedido
		WHERE	Itempedido.qtde >= 10

	--(avan�ada) para uma qtde de produtos somados acima de 10
		SELECT cliente.nome/*, Pedido.Numero*/
		FROM	Cliente
				INNER JOIN Pedido on Cliente.id = Pedido.Id_cliente
				INNER JOIN ItemPedido on pedido.Numero = ItemPedido.NumeroPedido
		GROUP BY cliente.nome/*, Pedido.Numero*/ 
		HAVING SUM( Itempedido.qtde ) >= 10

/*AC4:*/
-- Lista com o total de Pedidos realizados por dia, m�s e ano deste ano ( usar fun��o para coletar data e hora padr�o ).
	--Separando dia de mes de ano
		SELECT	DAY(datahora) as dia
				, MONTH(datahora) as mes
				, YEAR(datahora) as ano
				, count(*) as TotalPedidos
		FROM	Pedido
		--WHERE	YEAR(datahora) = YEAR(GETDATE())--s� pedidos deste ano
		WHERE	YEAR(datahora) = 2017 /*para testes*/
		GROUP BY DAY(datahora)
				, MONTH(datahora)
				, YEAR(datahora)
	--usando apenas 1 campo para a data
		SELECT	convert(varchar,datahora,103) as dia
				, count(*) as TotalPedidos
		FROM	Pedido
		--WHERE	YEAR(datahora) = YEAR(GETDATE())--s� pedidos deste ano
		WHERE	YEAR(datahora) = 2017 /*para testes*/
		GROUP BY convert(varchar,datahora,103)

-- Lista com um ranking dos 10 melhores clientes pela quantidade de produtos comprados.
	SELECT	top 10 cliente.nome, SUM(itemPedido.qtde) as qtdeComprada, count(distinct pedido.numero) as nrPedidos
	FROM	Cliente
			INNER JOIN Pedido on Cliente.id = Pedido.Id_cliente
			INNER JOIN ItemPedido on pedido.Numero = ItemPedido.NumeroPedido
	GROUP BY cliente.nome
	ORDER BY qtdeComprada /*apelido*/ desc --> maior primeiro
	--ORDER BY SUM(itemPedido.qtde) --formula/coluna
	--ORDER BY 2 --posi��o

-- Lista com o nome dos produtos n�o vendidos ainda neste m�s autal ( usar fun��o para coletar data e hora padr�o ).
	--Lista total de produtos menos a lista de produtos vendidos no m�s atual
	SELECT	nome 
	FROM	produto
	WHERE	nome NOT IN (
		SELECT	Produto.nome
		FROM	Pedido 
				INNER JOIN ItemPedido on pedido.Numero = ItemPedido.NumeroPedido
				INNER JOIN Produto on ItemPedido.ID_produto = produto.ID		
		--WHERE	YEAR(datahora) = YEAR(GETDATE()) --s� pedidos deste ano
			--AND MONTH(datahora) = MONTH(GETDATE()) --s� pedidos deste ano+m�s
		WHERE	YEAR(datahora) = 2017 /*para testes*/
				AND MONTH(datahora) = 9 /*para testes*/
	)

--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 
--=X=-- DQL - Replicando o select original ( Extra / Avan�ado )
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- 

/*
Jos�	telefone X2
		Pedidos	 X2
		Itens	 X1
linhas = 4

Telefone (N-1) Cliente (1-N) Pedido --N�o h� como relacionar normalmente
*/
--Replicando select original ( b�sico )
	SELECT	cliente.Nome
			, cliente.endereco
			, Telefone.numero
			, ItemPedido.Qtde
			, Pedido.numero
			, Produto.nome as NumeroPedido
			, Pedido.DataHora
	FROM	Cliente
			--tem que ser left pois existem clientes sem telefone
			LEFT JOIN Telefone on cliente.id = telefone.Id_cliente
			INNER JOIN Pedido on Cliente.id = Pedido.Id_cliente
			INNER JOIN ItemPedido on pedido.Numero = ItemPedido.NumeroPedido
			INNER JOIN Produto on ItemPedido.ID_produto = produto.ID

--Replicando o select original ( vers�o avan�ada )
--Ajustando os m�ltiplos telefones por pessoa
	SELECT	cliente.Nome
			, cliente.endereco
			, STRING_AGG( Telefone.numero, ', ') as Telefone
			, Pedido.numero
			, ItemPedido.Qtde
			, Produto.Nome as NumeroPedido
			, Pedido.DataHora
	FROM	Cliente
			--tem que ser left pois existem clientes sem telefone
			LEFT JOIN Telefone on cliente.id = telefone.Id_cliente
			INNER JOIN Pedido on Cliente.id = Pedido.Id_cliente
			INNER JOIN ItemPedido on pedido.Numero = ItemPedido.NumeroPedido
			INNER JOIN Produto on ItemPedido.ID_produto = produto.ID
	GROUP BY cliente.Nome
			, cliente.endereco
			, ItemPedido.Qtde
			, Produto.Nome
			, Pedido.numero
			, Pedido.DataHora

--Replicando o select original ( vers�o super avan�ada )
--Ajustando os m�ltiplos itens de um pedido
--N�o posso fazer 2 groups by ( para telefone e itens ) numa mesma query
	SELECT	cliente.Nome
			, cliente.endereco
			, ISNULL(Telefones.numeros,'-') as Numeros
			, Pedido.numero as NumeroPedido
			, STRING_AGG( convert(varchar,ItemPedido.qtde) + 'x ' + produto.nome, ' + ' ) as Itens_Pedido
			, Pedido.DataHora
	FROM	Cliente
			INNER JOIN Pedido on Cliente.id = Pedido.Id_cliente
			INNER JOIN ItemPedido on pedido.Numero = ItemPedido.NumeroPedido
			INNER JOIN Produto on ItemPedido.ID_produto = produto.ID	
			/*OUTER APPLY (
				SELECT	Telefone.Id_cliente,  STRING_AGG( Telefone.numero, ', ') as Numeros
				FROM	Telefone 
				WHERE	telefone.Id_cliente = cliente.id 
				GROUP BY telefone.Id_cliente
			) as Telefones*/

			LEFT JOIN (
				SELECT	Telefone.Id_cliente,  STRING_AGG( Telefone.numero, ', ') as Numeros
				FROM	Telefone 
				GROUP BY telefone.Id_cliente
			) as Telefones
			ON telefones.Id_cliente = cliente.id 
	GROUP BY cliente.Nome
			, telefones.numeros
			, cliente.endereco
			, Pedido.numero
			, Pedido.DataHora

--Replicando o select original ( vers�o mega avan�ada )
--Arrumando os n�meros do pedido para resetaram por cliente
	SELECT	cliente.Nome
			, cliente.endereco
			, ISNULL(Telefones.numeros,'-') as Numeros
			, ROW_NUMBER() OVER( Partition by cliente.id order by Pedido.numero) as NumeroPedido
			, STRING_AGG( convert(varchar,ItemPedido.qtde) + 'x ' + produto.nome, ', ' ) as Itens_Pedido
			, Pedido.DataHora
	FROM	Cliente
			INNER JOIN Pedido on Cliente.id = Pedido.Id_cliente
			INNER JOIN ItemPedido on pedido.Numero = ItemPedido.NumeroPedido
			INNER JOIN Produto on ItemPedido.ID_produto = produto.ID	
			--para cada...
			OUTER APPLY (
				SELECT	Telefone.Id_cliente,  STRING_AGG( Telefone.numero, ', ') as Numeros
				FROM	Telefone 
				WHERE	telefone.Id_cliente = cliente.id 
				GROUP BY telefone.Id_cliente
			) as Telefones
	GROUP BY cliente.id
			, cliente.Nome
			, telefones.numeros
			, cliente.endereco
			, Pedido.numero
			, Pedido.DataHora







