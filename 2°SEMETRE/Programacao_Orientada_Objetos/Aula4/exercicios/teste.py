from exer05 import converte_para_celsius, converte_para_fahrenheit

try:
    resultado = converte_para_fahrenheit(0)
    assert resultado == 32.0
    print('COORETO')

except AssertionError:
    print('ERROR 404')


try:
    resultado = converte_para_fahrenheit(27)
    assert resultado == 80.6
    print('COORETO')

except AssertionError:
    print('ERROR 404')