'''
Escreva uma função que conta a quantidade de vogais em um texto e
armazena tal quantidade em um dicionário, onde a chave é a vogal
considerada e o valor é a quantidade de vezes que essa vogal aparece no texto. 
A função deve receber o texto como entrada, e retornar o dicionário.
'''

def conta_vogais(texto):
    dicionario = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for c in texto:
        if c == 'a':
            dicionario['a'] += 1
        if c == 'e':
            dicionario['e'] += 1
        if c == 'i':
            dicionario['i'] += 1
        if c == 'o':
            dicionario['o'] += 1
        if c == 'u':
            dicionario['u'] += 1
    return dicionario

texto = 'exemplo de texto'
dicionario = conta_vogais(texto)
print(dicionario)
