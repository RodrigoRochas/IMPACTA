use esfiraria;
GO
create table TBLcliente (
	id_cliente int identity not null,
	nome varchar(50) not null,
	endereco varchar(50) not null,


	constraint pkCliente primary key(id_cliente)
);

insert into TBLcliente (nome, endereco) values ('jose', 'Av.Tres, numero 1')
insert into TBLcliente (nome, endereco) values ('maria', 'Av impar, apto 122')
select * from TBLcliente;


create table TBLtelefone(
	id_cliente int not null,
	id_telefone int not null,


	constraint fkTelefoneCliente foreign key (id_cliente) references TBLcliente(id_cliente)
);

exec sp_rename 'TBLtelefone.[id_telefone]', 'numero', 'column';

insert into TBLtelefone (id_cliente, numero) values (1,120)
insert into TBLtelefone (id_cliente, numero) values (2,122)
select * from TBLtelefone;

GO

create table TBLpedido (
	id_pedido int identity not null,
	id_cliente int not null,
	DataHora datetime not null,

	constraint pkPedido primary key(id_pedido),
	constraint fkPedidoCliente foreign key(id_cliente) references TBLcliente(id_cliente)
);
--	YYYY-MM-DD hh:mm:ss[.nnn]
insert into TBLpedido (id_cliente, DataHora) values (2, '20170827 10:30:00 PM');
select * from TBLpedido;



create table TBLproduto (
	id_produto int identity not null,
	nome varchar(50) not null,


	constraint pkProduto primary key(id_produto),
);

insert into TBLproduto (nome) values ('brocolis')
select * from TBLproduto;




create table TBLitempedido (
	id_item_pedido int identity not null,
	id_produto int not null,
	id_pedido int not null,
	quantidade int not null,

	constraint pkItemPedido primary key(id_item_pedido),
	constraint fkItemPedidoProduto foreign key(id_produto) references TBLproduto(id_produto),
	constraint fkItemPedidoPedido foreign key(id_pedido) references TBLpedido(id_pedido)
);

insert into TBLitempedido (id_produto, id_pedido, quantidade) 
	values (1, 4, 3);

insert into TBLitempedido (id_produto, id_pedido, quantidade) 
	values (2, 4, 2);

insert into TBLitempedido (id_produto, id_pedido, quantidade)
	values (1, 5, 7) , (3, 5, 4);



select * from TBLcliente;
select * from TBLtelefone;
select * from TBLpedido;
select * from TBLproduto;
select * from TBLitempedido;
