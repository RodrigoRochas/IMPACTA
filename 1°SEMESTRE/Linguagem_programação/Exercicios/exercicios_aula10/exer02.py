segundo = int(input('Digite em segundos : '))

def converter(segundo):
    horas = segundo // 3600
    resto_horas = segundo % 3600

    minutos = resto_horas // 60
    segundos = resto_horas % 60

    print(f'{horas:02d} : {minutos:02d} : {segundos:02d} ')

converter(segundo)