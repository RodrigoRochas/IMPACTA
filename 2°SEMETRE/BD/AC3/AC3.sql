use AC3;
GO
create table TBLfornecedor (
    Id_Fornecedor int not null identity(1,1),
    nome varchar(50) not null,

    constraint PK_FORNECEDOR primary key (Id_Fornecedor)

);
GO
create table TBLcompra (
    Nota_Fiscal varchar(15) not null,
    DiasEntrega tinyint not null,
    Valor money not null,
    Dataa DATETIME2,

    constraint PK_COMPRA primary key (Nota_Fiscal)
);
GO
CREATE TABLE TBLproduto(
    Id_Produto int not null IDENTITY(1,1),
    nome VARCHAR(50) not null,
    Id_Fornecedor int not null,

    CONSTRAINT PK_PRODUTO PRIMARY KEY (Id_Produto),
    CONSTRAINT FK_PRODUTO_FORNECEDOR FOREIGN KEY(Id_Fornecedor) REFERENCES TBLfornecedor(Id_Fornecedor)

);
GO
CREATE TABLE TBLItemCompra (
    Id_Produto INT NOT NULL,
    Id_Fornecedor INT NOT NULL,
    Nota_Fiscal VARCHAR(15) NOT NULL,
    QTDE INT NOT NULL,

    CONSTRAINT PK_ITEM_COMPRA PRIMARY KEY(Id_Produto, Id_Fornecedor, Nota_Fiscal),
    CONSTRAINT FK_ITEMCOMPRA_PRDUTO FOREIGN KEY(Id_Produto) REFERENCES TBLproduto(Id_Produto),
    CONSTRAINT FK_ITEMCOMPRA_FORNECEDOR FOREIGN KEY(Id_Fornecedor) REFERENCES TBLfornecedor(Id_Fornecedor),
    CONSTRAINT FK_ITEMCOMPRA_COMPRA FOREIGN KEY(Nota_Fiscal) REFERENCES TBLcompra(Nota_Fiscal)

);
GO
SELECT * FROM TBLcompra;
SELECT * FROM TBLfornecedor;
SELECT * FROM TBLproduto;
SELECT * FROM TBLItemCompra;
