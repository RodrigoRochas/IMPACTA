from exercicio05 import converte_para_celsius, converte_para_fahrenheit

try:
    resultado = converte_para_fahrenheit(0)
    assert resultado == 32.0
    print('CORRETA')
except AssertionError:
    print('ERRO')

try:
    resultado = converte_para_fahrenheit(27)
    assert resultado == 80.6
    print('CORRETA')
except AssertionError:
    print('ERRO')

try:
    resultado = converte_para_celsius(32)
    assert resultado == 0
    print('CORRETA')
except AssertionError:
    print('ERRO')

try:
    resultado = converte_para_celsius(41)
    assert resultado == 5.0
    print('CORRETA')
except AssertionError:
    print('ERRO')
