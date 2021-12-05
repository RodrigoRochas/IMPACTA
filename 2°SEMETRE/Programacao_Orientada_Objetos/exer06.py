def soma_divisores(n):
    a = 1
    soma = 0
    while a <= n:
        if n % a == 0:
            soma += a
        a += 1

    return soma


print(soma_divisores(10))