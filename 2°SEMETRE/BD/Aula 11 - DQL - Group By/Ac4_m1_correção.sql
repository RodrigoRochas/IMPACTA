/*
use master
go

1

DROP DATABASE M1_Vendas_Pedidos;
GO
*/
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=--
--=X=-- DDL - Cria��o da base
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=--
CREATE DATABASE AC4_M1_Vendas_Pedidos;
GO
USE AC4_M1_Vendas_Pedidos;
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
, CONSTRAINT FK_TelefoneCliente FOREIGN KEY ( ID_cliente ) REFERENCES Cliente ( ID
)
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
, CONSTRAINT FK_PedidoCliente FOREIGN KEY ( ID_cliente ) REFERENCES Cliente ( ID )
)
GO
CREATE TABLE ItemPedido (
NumeroPedido INT NOT NULL
, ID_produto INT NOT NULL
, Qtde INT NOT NULL
, CONSTRAINT PK_ItemPedido PRIMARY KEY (NumeroPedido, ID_produto)
, CONSTRAINT FK_ItemPedidoPedido FOREIGN KEY ( NumeroPedido) REFERENCES Pedido (
Numero )
, CONSTRAINT FK_ItemPedidoProduto FOREIGN KEY ( ID_produto) REFERENCES Produto ( ID
)
)
GO
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=--
--=X=-- DML - Carga da base
--=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=-- --=X=--

INSERT INTO Cliente ( Nome, Endereco )
values ( 'Jos�', 'Av. Tr�s, Numero 1')
, ( 'Maria', 'Av. Impar, nr 33, apto 12')
GO
INSERT INTO Telefone ( id_cliente, Numero )
VALUES ( (select ID from cliente where nome = 'Jos�'), '93783259' )
, ( (select ID from cliente where nome = 'Jos�'), '87453452' )
--Maria n�o tem Telefone Cadastrado
GO
INSERT INTO Produto (Nome )
VALUES ( 'Calabresa' )
, ( 'Frango' )
, ( 'Br�colis' )
, ( 'Carne' ) --item extra para os relat�rios
--N�mero do pedido ficou como auto incremental para simplificar
--Jos� com 2 pedidos, maria com 1
-- SET DATEFORMAT DMY
INSERT INTO Pedido ( datahora, id_cliente )
VALUES ( '20/08/2017 23:11', (select ID from cliente where nome = 'Jos�') )
, ( '27/08/2017 22:30', (select ID from cliente where nome = 'Jos�') )
, ( '21/09/2017 19:59', (select ID from cliente where nome = 'Maria') )
GO
--Busca em Pedido foi feit pela datahora pois os IDs podem mudar
--Neste caso DataHora � o mais pr�ximo que tenho de um outro campo �nico.
INSERT INTO ItemPedido ( NumeroPedido, ID_produto, Qtde )
VALUES ( (select Numero from Pedido where datahora = '20/08/2017 23:11')

, (select id from produto where nome = 'Calabresa')
, 3
)
, ( (select Numero from Pedido where datahora = '27/08/2017 22:30')
, (select id from produto where nome = 'Frango')
, 2
)
, ( (select Numero from Pedido where datahora = '21/09/2017 19:59')
, (select id from produto where nome = 'Calabresa')
, 7
)
, ( (select Numero from Pedido where datahora = '21/09/2017 19:59')
, (select id from produto where nome = 'Br�colis')
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


Da AC3 -
- Lista com Nome dos produtos dispon�veis
select nome from produto

- Lista com o Numero dos Pedidos realizados entre �01/01/2017� e �31/01/2017�
select Numero from pedido
where datahora between
'20170801' AND '20170831'


- Lista com Numero do Pedido, Nome do Produto e quantidade vendida.
SELECT pedido.numero as [Numero do Pedido]
, produto.nome as [Nome do Produto]
, itemPedido.qtde as [quantidade vendida]
FROM Pedido
INNER JOIN ItemPedido
ON pedido.numero = itempedido.NumeroPedido
INNER JOIN produto
ON ItemPedido.ID_produto = produto.ID

- Lista com Nome e Endere�o do Cliente e, se existirem, seus respectivos telefones.
SELECT cliente.nome as [nome do cliente]
, cliente.endereco as [endereco]
, telefone.numero [telefone]
FROM cliente
LEFT join telefone
ON cliente.id = telefone.id_cliente

- Lista com o nome dos clientes que j� compraram, em uma compra, uma quantidade de produtos superior � 10.
select DISTINCT cliente.nome as [nome do cliente]
FROM cliente
INNER JOIN PEDIDO
on cliente.id = pedido.id_cliente
INNER JOIN itempedido
on pedido.numero = itempedido.numeroPedido
where itempedido.qtde > 10

/*Mais exemplos de group by*/

--Confer�ncias:
select * from cliente
select * from telefone
select * from produto
select * from Pedido
select * from ItemPedido

-- quantidade de pedidos realizados por cliente
select	id_cliente, count(Numero) as qtde, min(datahora) as  dataPrimeiraCompra
from	Pedido
group by id_cliente --> no resultado final, terei uma linha para cada id_cliente �nico encontrado.

id_cliente	qtde	dataPrimeiraCompra
1			2		2017-08-20 23:11:00.000
2			1		2017-09-21 19:59:00.000

-- pessoas com telefone ou n�o...
SELECT cliente.nome as [nome do cliente]
, cliente.endereco as [endereco]
, telefone.numero [telefone]
FROM cliente
LEFT join telefone
ON cliente.id = telefone.id_cliente

-- pessoas e o n�mero de telefones cadastrados.
Jos�	2
Maria	0
SELECT	cliente.nome
		, count(telefone.numero) as contagemTelefones
		--, count(*) as contagemGenerica
FROM	cliente
		LEFT join telefone
		ON cliente.id = telefone.id_cliente
GROUP BY cliente.nome

-- soma das qtdes por numero do pedido
select	numeroPedido, sum(qtde) as totalEsfihas, count(*) as totalItens
from	ItemPedido
group by numeroPedido



select *, year(datahora) as ano, month(datahora) as mes, day(datahora) as dia 
, datepart(year,datahora) as ano, datepart(month,datahora) as mes, datepart(day,datahora) as dia
, datepart(weekday,datahora) as diaSemana, datename(weekday,datahora) as diaSemana
from Pedido

-- n�mero de vendas por dia da semana
select top 1 datename(weekday,datahora) as diaSemana, count(*) as vendas
from pedido
group by datename(weekday,datahora) 
order by vendas desc


ciclo de vida
coletado -> tratado -> organizado -> registrado/armazenado -> usado -> transferido -> descartado.




Na AC4 - Execute as seguintes consultas no banco de dados criado:
- Lista com o total de Pedidos realizados por dia, m�s e ano deste ano ( usar fun��o para coletar data e hora padr�o ).

SELECT	year(datahora) as ano, month(datahora) as mes, day(datahora) as dia 
		, count(*) as [total de pedidos]
FROM	Pedido
WHERE	year(datahora) = year(getdate()) -- pedidos feitos neste ano. pedidos feitos no ano atual
GROUP BY year(datahora),  month(datahora), day(datahora)

- Lista com um ranking dos 10 melhores clientes pela quantidade de produtos comprados.

SELECT	top 10
			cliente.nome
			, sum(qtde) as [total produtos]
FROM	cliente
		inner join pedido on cliente.id = pedido.Id_cliente
		inner join itemPedido on pedido.Numero = ItemPedido.NumeroPedido
group by cliente.nome
order by [total produtos] DESC


- Lista com o nome dos produtos n�o vendidos ainda neste m�s autal ( usar fun��o para coletar data e hora padr�o )

-- Resolu��o na pr�xima aula
