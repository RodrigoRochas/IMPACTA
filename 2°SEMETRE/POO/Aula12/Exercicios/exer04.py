arquivo = open('IPS.txt', 'r')
ips_validos = open('IP_VALIDO.txt', 'w')
ips_invalidos = open('IP_INVALIDO.txt', 'w')

arquivo.file

for linha in arquivo:
    n_desmenbrado = linha.split('.')
    
    n1 = int(n_desmenbrado[0])
    n2 = int(n_desmenbrado[1])
    n3 = int(n_desmenbrado[2])
    n4 = int(n_desmenbrado[3])
    
    if  n1 >= 1 and n1 <= 255 and \
        n2 >= 0 and n2 <= 255 and \
        n3 >= 0 and n3 <= 255 and \
        n4 >= 0 and n4 <= 255:
        ips_validos.write(linha)
    else:
        ips_invalidos.write(linha)   
        

arquivo.close()
ips_validos.close()
ips_invalidos.close() 
    
    
    