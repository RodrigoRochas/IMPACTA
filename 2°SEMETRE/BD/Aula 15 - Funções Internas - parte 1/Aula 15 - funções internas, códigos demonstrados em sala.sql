
select * from medico
-- terceira letra do nome do médico
select	SUBSTRING(nome,3,1) as [terceiro digito]
		, left(nome,1) as [primeira letra]
		, right(nome,1) as [ultima letra]
		, upper(nome) as [maiusculo]
		, lower(nome) as [minusculo]
		, len(nome) as [tamanho do nome]
		, nome 
from medico

-- como devolver só a inicial(primeira letra) em maiúsculo
-- e todas as demais em minúsculo ???
select	UPPER( LEFT(nome,1) ) 
+  LOWER( SUBSTRING(nome,2,49 ) )
from	Medico

select	UPPER( LEFT(nome,1) ) 
+  LOWER(RIGHT(nome, LEN(nome)-1 ) )
from	Medico


select '['+ trim('   texto    ')+']'
select '['+ rtrim(ltrim('   texto    '))+']'

-- alinhe os nomes 50 chars à direita
select '['+RIGHT(space(50) + nome,50)+']' from medico

select '['+RIGHT(replicate('0',10) + cast(id as varchar(50)),10)+']' from medico
[0000000001]
[0000000002]

select replace( 
			replace( '[texto]', '[', '{' )
			, ']'
			, '}')
{texto}

select nome, replace(nome,'a','bbc') from medico

select *
		, case duracao
			when 30 then 'Regular'
			when 15 then 'Curta'
			when 60 then 'Longa'
			else 'não definido'
			end
	, case     
			when duracao = 30 then 'Regular'
			when duracao = 15 then 'Curta'
			when duracao = 60 then 'Longa'
			else 'não definido'
			end
from consulta
 

-- pivoteamento dos dados..
-- soma condicionada...
número de consultas:
	curtas, regulares e longas 
	por médico...
SELECT medico.nome as [nome do médico]
		, count(*) as [total de consultas]
	, sum(case when duracao = 15 then 1 else 0 end) as [total consultas curtas]
	, sum(case when duracao = 30 then 1 else 0 end) as [total consultas Regulares]
	, sum(case when duracao = 60 then 1 else 0 end) as [total consultas Longas]
FROM medico
	inner join consulta
	on medico.id = consulta.id_medico
GROUP BY medico.nome

SELECT medico.nome as [nome do médico]
		, count(*) as [total de consultas]
	, sum( IIF( duracao = 15, 1, 0) ) as [total consultas curtas]
	, sum( IIF( duracao = 30, 1, 0) ) as [total consultas Regulares]
	, sum( IIF( duracao = 60, 1, 0) ) as [total consultas Longas]
FROM medico
	inner join consulta
	on medico.id = consulta.id_medico
GROUP BY medico.nome

declare @email varchar(50) = 'mauro@gmail.com'
select	SUBSTRING(@email, 1, charindex('@',@email)-1 ) as [nome]
, SUBSTRING(@email, charindex('@',@email)+1, 9999 ) as [dominio]

select nome as [nome completo]
	, SUBSTRING(nome, 1, charindex(' ',nome)-1 ) as [primeiro nome]
	, SUBSTRING(nome, charindex(' ',nome)+1, 9999 ) as [sobrenome]
from paciente

substring(texto, posicao, qtde chars )
select substring('hoje é quarta-feira', 10, 2 )
ar



select datediff(day,'2001-06-30',getdate()) --7438


select datediff(day,'2001-06-30','2001-07-01') --1
select datediff(month,'2001-06-30'
					 ,'2001-07-01') --1 ????
select datediff(year ,'2001-12-31'
					 ,'2002-01-01') --1 ????

-- então como calcular a data de aniversário ???
select datediff(day,'1960-11-11',getdate()) / 365.25
60.996577


select dateadd(year,-1,'1960-11-11')
select getdate()+10, dateadd(day,10,getdate())
2021-11-20 22:17:22.500	2021-11-20 22:17:22.500


-- qual o primeiro dia do mês atual ???
declare @data datetime = getdate()
select  @data - day(@data) + 1
		--,  convert(varchar(50), year(@data) )
		--	+ convert(varchar(50), month(@data) )
		--	+ '01'
-- qual o último dia do mês atual ???
declare @data datetime = '20211101'
select  dateadd(month,1,@data) - day(@data)


select datepart(year,'20210103'), year('20210103')

select datename(month,'20210103') Janeiro
select datename(weekday,'20210103') Domingo


