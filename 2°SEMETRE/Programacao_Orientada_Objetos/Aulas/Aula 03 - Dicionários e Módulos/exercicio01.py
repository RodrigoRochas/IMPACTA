'''
Preencha um dicionário com as informações de 5 produtos.
Utilize o nome do produto como chave e o preço como valor. 
Solicite os dados ao usuário.
Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00
'''

produtos = {}
for i in range(5):
    nome = input('Nome do produto: ')
    preco = float(input('PReço do produtos: '))
    produtos[nome] = preco
print(produtos)

for a in produtos:
    if produtos[a] > 50:
        print(a)
