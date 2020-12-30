pet_1 = {
    'nome': 'minhau',
    'tipo': 'gato',
    'sexo': 'macho',
    'cor': 'preto',
    'dono': 'jonas'
}
pet_2 = {
    'nome': 'lence',
    'tipo': 'cachorro',
    'sexo': 'famino',
    'cor': 'marrom pitado',
    'dono': 'jonas'
}
pet_3 = {
    'nome': 'linus',
    'tipo': 'cachorro',
    'sexo': 'masculino',
    'cor': 'preto',
    'dono': 'jonas'
}
pets = []
pets.append(pet_1)
pets.append(pet_2)
pets.append(pet_3)

print(pets)

for i in range(len(pets)):
    print('<'*10 + str(i) + '>'*10)
    for pet, info in pets[i].items():
        print(f'{pet.title():>10}: {info.title():<1}')