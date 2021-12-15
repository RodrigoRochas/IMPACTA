# O formato de um endereço IP é num1.num.num.num, onde
# num1 vai de 1 a 255 e num vai de 0 a 255.

ips = open('ips.txt', 'r')

validos = open('ips validos.txt', 'w')
invalidos = open('ips invalidos.txt', 'w')

for n in ips:               # percorre arquivo de ips
    lista = n.split('.')    # separa os numeros do ip pelo caracter '.'

    n1 = int(lista[0])
    n2 = int(lista[1])
    n3 = int(lista[2])
    n4 = int(lista[3])

    # valida os números do ip e salva nos arquivos de saída
    if n1 >= 1 and n1 <= 255 and \
       n2 >= 0 and n2 <= 255 and \
       n3 >= 0 and n3 <= 255 and \
       n4 >= 0 and n4 <= 255:
        validos.write(n)
    else:
        invalidos.write(n)

ips.close()
validos.close()
invalidos.close()
