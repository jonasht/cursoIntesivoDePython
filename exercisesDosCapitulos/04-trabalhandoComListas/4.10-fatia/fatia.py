cubos = [i**3 for i in range(1, 11)]
print(cubos)

print('\nos tres primeiros itens de uma lista sao:')
for cubo in cubos[:3]:
    print(f'{cubo} ', end='')

print('\nos tres itens do meio de uma lista sao:')
for cubo in cubos[3:6]:
    print(f'{cubo} ', end='')

print('\nos tres ultimos "+ 1" itens de uma lista sao:')
for cubo in cubos[6:10]:
    print(f'{cubo} ', end='')
print()
