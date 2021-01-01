lugares = []

while 1:
    print('s para sair')
    onde = str(input('se pudesses visitar um lugar do mundo,\npara onde tu irias?\nlugar:'))
    if onde == 's': break
    lugares.append(onde)


print('\nlugares para onde gostarias de ir')
for i in range(len(lugares)):
    print(f'{i}-{lugares[i]}')