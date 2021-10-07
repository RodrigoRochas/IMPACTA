def fatorial(n):
    a = 1
    multi = 1
    
    while a <= n:
        multi *= a
        a += 1

    return multi

print(fatorial(5))
