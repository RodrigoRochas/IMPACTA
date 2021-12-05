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
, ID_FornecedorPadrao INT NOT NULL
, CONSTRAINT PK_Produto PRIMARY KEY ( ID )
, CONSTRAINT FK_ProdutoFornecedorPadrao FOREIGN KEY ( Id_FornecedorPadrao )
REFERENCES
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
CREATE TABLE ItemCompra (
ID_Produto INT NOT NULL
, ID_Fornecedor INT NOT NULL
, NF_Compra VARCHAR(15) NOT NULL
, QTDE INT NOT NULL
, CONSTRAINT PK_ItemCompra PRIMARY KEY ( ID_Produto, ID_Fornecedor, NF_Compra )
, CONSTRAINT FK_ItemCompraProduto FOREIGN KEY ( ID_produto ) REFERENCES PRODUTO (
ID )
, CONSTRAINT FK_ItemCompraFornecedor FOREIGN KEY ( ID_fornecedor) REFERENCES
Fornecedor ( ID )
, CONSTRAINT FK_ItemCompraCompra FOREIGN KEY ( NF_Compra ) REFERENCES Compra ( NF )
)
GO
INSERT INTO Fornecedor ( Nome )
VALUES ( 'Ambev' )
, ( 'P&G' )
, ( 'Dist. PPG' )

INSERT INTO Produto ( nome, ID_FornecedorPadrao )
VALUES ( 'Skol', (SELECT id from Fornecedor WHERE nome = 'Ambev') )
, ( 'Fralda Pampers', (SELECT id from Fornecedor WHERE nome = 'P&G') )

INSERT INTO Compra ( NF, DiasEntrega, Valor, [Data] )
VALUES ( '#112434', 3, '8243.00', '20171021' )
, ( '#324235', 10, '1123.00', '20171021' )
, ( '#455464', 2, '500.00', '20171026' )

INSERT INTO ItemCompra ( ID_Produto, ID_Fornecedor, NF_Compra, QTDE )
VALUES ( (SELECT id FROM Produto WHERE nome = 'Skol')
, (SELECT id FROM Fornecedor WHERE nome = 'Ambev')
, '#112434'
, 300
), ( (SELECT id FROM Produto WHERE nome = 'Fralda Pampers')
, (SELECT id FROM Fornecedor WHERE nome = 'P&G')
, '#324235'
, 25
), ( (SELECT id FROM Produto WHERE nome = 'Fralda Pampers')
, (SELECT id FROM Fornecedor WHERE nome = 'Dist. PPG')
, '#455464'
, 10
)

select * from Fornecedor
select * from Produto
select * from Compra
select * from ItemCompra

--EXERCICIO 1
select Nome from Produto

--EXERCICIO 2
select NF from Compra where [Data] > '20170101' and DiasEntrega > 10

--EXERCICIO 3
select Produto.Nome as [NomeProduto], Fornecedor.Nome as [NomeFornecedor], QTDE
from ItemCompra 
inner join Produto on ItemCompra.ID_Produto = Produto.ID 
inner join Fornecedor on Produto.ID_FornecedorPadrao = Fornecedor.ID

--EXERCICIO 4
select Produto.Nome as [NomeProduto], Fornecedor.Nome as [NomeFornecedor]
from Produto inner join Fornecedor on ID_FornecedorPadrao = Fornecedor.ID

--EXERCICIO 5
select NF, Produto.Nome as [NomeProduto], [Data], ItemCompra.QTDE as [QuantidadeCompra], Valor
from Compra inner join ItemCompra on Compra.NF = NF_Compra inner join Produto on ID_Produto = Produto.ID