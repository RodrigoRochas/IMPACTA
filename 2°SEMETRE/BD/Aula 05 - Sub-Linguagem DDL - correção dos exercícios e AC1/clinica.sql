use DBclinica;
GO
create table TBLsala (
	id_sala int not null identity,

	constraint PKsala primary key (id_sala)
);
GO
create table TBLpaciente (
	id_paciente int not null identity,
	nome varchar(50) not null,
	telefone int not null,

	constraint PKpaciente primary key (id_paciente)
);
GO
create table TBLmedico (
	id_medico int not null identity,
	crm int not null,
	nome varchar(50) not null,
	especialidade varchar(50) not null,

	constraint PKmedico primary key (id_medico)
);
GO
create table TBLconsulta (
	id_consulta int not null identity,
	id_paciente int not null,
	id_medico int not null,
	id_sala int not null,
	DataHora datetime not null,
	Hora time not null,

	constraint PKconsulta primary key (id_consulta),
	constraint FK_Consulta_Paciente foreign key (id_paciente) references TBLpaciente (id_paciente),
	constraint FK_Consulta_Medico foreign key (id_medico) references TBLmedico (id_medico),
	constraint FK_Consulta_Sala foreign key (id_sala) references TBLsala(id_sala),
);

select * from TBLconsulta;