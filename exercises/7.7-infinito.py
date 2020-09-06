
print('atençao, este codigo está em loop infinite')
print('precione ctrl + c para parar')
n = 1

while 1:
    n = n + n
    print(n)
    if len(str(n)) >= 1000: break # apagar isso para ser infinito
