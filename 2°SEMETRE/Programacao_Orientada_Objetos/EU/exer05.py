def calcula(salario):
    if salario >= 2000:
        salario = salario + (salario * 7 / 100)

    else:
        salario = salario + (salario * 15 / 100)

    return salario



print(calcula(3000))