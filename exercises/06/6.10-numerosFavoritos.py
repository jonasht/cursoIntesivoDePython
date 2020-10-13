pessoas = {
    'ana': [1, 8, 4],
    'pitona': [78, 5, 888],
    'elen': [232, 7, 8, 6, 1, 2, 4]
}

for pessoa, i in pessoas.items():
    print(f'\nos numeros favoritos de {pessoa} são:')
    for n in pessoas[pessoa]:
        print(f'{n}|', end='')
