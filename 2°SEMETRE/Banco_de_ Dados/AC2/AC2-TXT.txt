create database AC2;
GO
use AC2;
GO
create table TBLCompra(
	nota_fiscal varchar(15) not null,
	dias_entrega tinyint not null,
	valor float not null,
	dataa date not null,

	constraint PK_COMPRA primary key (nota_fiscal)
);
GO
select * from TBLCompra;


create table TBLfornecedor(
	id_fornecedor int not null identity(1,1),
	nome varchar(50) not null,

	constraint PK_FORNECEDOR primary key(id_fornecedor)
);
GO
select * from TBLfornecedor;


create table TBLproduto(
	id_produto int not null identity(1,1),
	nome varchar(50) not null,
	id_fornecedor int not null,

	constraint PK_PRODUTO primary key (id_produto),
	constraint FK_PRODUTO_FORNECEDOR foreign key (id_fornecedor) references TBLfornecedor(id_fornecedor)
);
GO
select * from TBLproduto;

create table TBLItemCompra(
	id_produto int not null,
	id_fornecedor int not null,
	nota_fiscal varchar(15) not null,
	qtde int not null,

	constraint PK_PRODUTO_FORNECEDOR_NF primary key (id_produto, id_fornecedor, nota_fiscal),
	constraint FK_ITEMCOMPRA_PRODUTO foreign key (id_produto) references TBLproduto(id_produto),
	constraint FK_ITEMCOMPRA_FORNECEDOR foreign key (id_fornecedor) references TBLfornecedor(id_fornecedor),
	constraint FK_ITEMCOMPRA_NF foreign key (nota_fiscal) references TBLCompra (nota_fiscal),

);
GO
select * from TBLItemCompra;



		--INSERT NA TABELA DE FORNECEDOR
insert into TBLfornecedor (nome) values ('Ambev')
insert into TBLfornecedor (nome) values ('P&G')
insert into TBLfornecedor (nome) values ('Dist.PPG')
select * from TBLfornecedor;

GO

	--INSERT COM SELECT NA TABELA DE PRODUTO
insert into TBLproduto (nome, id_fornecedor) 
	values (
	'Skol', 
	(select id_fornecedor from TBLfornecedor where nome like 'Amb%')
);
GO 
insert into TBLproduto (nome, id_fornecedor) 
	values (
	'Fralda Pamapers',
	(select id_fornecedor from TBLfornecedor where nome like 'P%')
);
GO
select * from TBLproduto;



					--INSERT TABELA COMPRA
insert into TBLCompra (nota_fiscal, dias_entrega, valor, dataa)
	values ('#112434', 3, 8.243, '20171021');
GO
insert into TBLCompra (nota_fiscal, dias_entrega, valor, dataa)
	values ('#324235', 10, 1.230, '20171021');
GO
insert into TBLCompra (nota_fiscal, dias_entrega, valor, dataa)
	values ('#455464', 2, 500, '20171026');
GO
select * from TBLCompra;


					--INSERT TABELA ITEM COMPRA
insert into TBLItemCompra (id_produto, id_fornecedor, nota_fiscal, qtde) 
	values (
	(select id_produto from TBLproduto where nome = 'Skol' and id_fornecedor = 1),
	(select id_fornecedor from TBLfornecedor where nome like 'Amb%'),
	(select nota_fiscal from TBLCompra where valor = 8.243),
	300
);
GO
insert into TBLItemCompra (id_produto, id_fornecedor, nota_fiscal, qtde)
	values (
	(select id_produto from TBLproduto where nome like 'Frald%' and id_fornecedor = 2),
	(select id_fornecedor from TBLfornecedor where nome like 'P%'),
	(select nota_fiscal from TBLCompra where valor = 1.23),
	25
);
GO
insert into TBLItemCompra (id_produto, id_fornecedor, nota_fiscal, qtde)
	values (
	(select id_produto from TBLproduto where nome like 'Fralda%'),
	(select id_fornecedor from TBLfornecedor where nome like 'Dist%'),
	(select nota_fiscal from TBLCompra where valor = 500),
	10
);
GO
select * from TBLItemCompra;



			--DELETE DE PRODUTOS ALCOOLICOS
delete from TBLproduto where nome like 'Skol';
delete from TBLCompra where dias_entrega = 3;
delete from TBLItemCompra where qtde = 300;
GO

			--UPDATE DATA NA TABELA COMPRA
update TBLCompra set dataa = '20171028' where dataa = '20171026';
GO

select * from TBLproduto;
select * from TBLCompra;
select * from TBLfornecedor;
select * from TBLItemCompra;


