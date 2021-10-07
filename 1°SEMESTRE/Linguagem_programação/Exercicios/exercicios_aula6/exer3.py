import random

cont = 0
cont_par = 0
cont_impar = 0

while cont < 200:
    num = random.randint(1, 1000)
    print(num, end=' ')

    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
        cont += 1

print(f'\n\n Total de pares : {cont_par}')
print(f'\n\n Total de impares : {cont_impar}')
