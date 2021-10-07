create database Livraria;
GO
use Livraria;

GO

create table TBLcliente (
	id_cliente int not null,
	nome varchar(50) not null,
	telefone int not null,

	constraint PKcliente primary key(id_cliente)
);

GO

create table TBLlivro (
	nome_livro varchar(250) not null,
	id_copia int not null,
	istatus varchar(20) not null,

	constraint PKlivro primary key (nome_livro, id_copia)

);

GO

create table TBLemprestimo (
	id_emprestimo int not null identity,
	id_cliente int not null,
	nome_livro varchar(250) not null,
	id_copia int not null,

	dataEmprestimo datetime not null,
	dataDevolucaoProposta datetime null,
	dataDevolucaoEfetiva datetime null,
	multa decimal(6,2),

	constraint PKempretimo primary key (id_emprestimo),

	constraint FKemprestimoLivro foreign key (nome_livro, id_copia) references TBLlivro(nome_livro, id_copia),
	constraint FKemprestimoCliente foreign key (id_cliente) references TBLcliente(id_cliente)

);
