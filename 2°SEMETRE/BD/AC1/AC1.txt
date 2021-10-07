use Mercado;
GO
create table TBLcompra (
	nota_fiscal int not null identity,
	DiasEntrega date not null,
	valor decimal(8,2) not null,
	Dataa datetime not null,

	constraint PKcompra primary key (nota_fiscal)
);
GO
create table TBLfornecedor (
	id_fornecedor int not null identity,
	nome varchar(200) not null,

	constraint PKfornecedor primary key (id_fornecedor)
);
GO
create table TBLproduto (
	id_produto int not null identity,
	nome varchar(200) not null,
	id_fornecedor int not null,

	constraint PKproduto primary key (id_produto),
	constraint FK_produto_fornecedor foreign key (id_fornecedor) 
		references TBLfornecedor (id_fornecedor)

);
GO

create table TBLItemCompra (
	id_produto int not null,
	id_fornecedor int not null,
	nota_fiscal int not null,
	quantidade int not null,

	constraint PKs_produto_fornecedor_notaFiscal 
		primary key(id_produto, id_fornecedor, nota_fiscal),

	constraint FK_ItemCompra_produto foreign key (id_produto)
		references TBLproduto (id_produto),

	constraint FK_ItemCompra_fornecedor foreign key (id_fornecedor)
		references TBLfornecedor (id_fornecedor),

	constraint FK_ItemCompra_compra foreign key (nota_fiscal)
		references TBLcompra (nota_fiscal),

);

select * from TBLcompra;
select * from TBLfornecedor;
select * from TBLproduto;
select * from TBLItemCompra;