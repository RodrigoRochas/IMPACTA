salario_bruto = float(input('Digite seu salario : '))
preco_prestacao = float(input('Digite o quanto quer pagar mensalmente : '))
valor_prestacao = ((30 / 100) * salario_bruto) 

if valor_prestacao < preco_prestacao: 
    print('Emprestimo Negado')

else:
    print('Emprestimo Concedido')
