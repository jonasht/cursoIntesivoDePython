quadrados = []

for valor in range(1, 11):
    quadrado = valor**2
    quadrados.append(quadrado)
    
print(quadrados)

print('minimo: ', min(quadrados))
print('maximo: ', max(quadrados))
print('soma: ', sum(quadrados))