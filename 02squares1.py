

# usando uma linha só, list comprehensions/abrangencia de lista
quadrados = [valor**2 for valor in range(1, 11)]    
print(quadrados)

print('minimo: ', min(quadrados))
print('maximo: ', max(quadrados))
print('soma: ', sum(quadrados))