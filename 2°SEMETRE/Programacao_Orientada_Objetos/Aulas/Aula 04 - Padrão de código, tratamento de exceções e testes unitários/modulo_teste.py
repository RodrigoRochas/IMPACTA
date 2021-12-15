from modulo import soma, fatorial


try:
    resultado = soma(10, 20)
    assert resultado > 0, 'O resultado não é positivo'
    assert resultado % 2 == 0, 'O resultado não par'
    assert resultado == 30, 'O resultado não é 30'
    print('Soma CORRETA')
except AssertionError as msg:
    print('Soma ERRADA:', msg)

try:
    resultado = soma(-10, -10)
    assert resultado == -20
    print('Soma CORRETA')
except AssertionError:
    print('Soma ERRADA')

try:
    resultado = soma(0, 0)
    assert resultado == 0
    print('Soma CORRETA')
except AssertionError:
    print('Soma ERRADA')

try:
    resultado = fatorial(5)
    assert resultado == 120
    print('Fatorial CORRETO')
except AssertionError:
    print('Fatorial ERRADO')
