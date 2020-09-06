# argumentos nomeados
def describe_pet(animal_type, pet_name):
    
    print(f'\neu tenho um {animal_type.title()}.')
    print(f'o nome do meu {animal_type} eh {pet_name.title()}.')
    
describe_pet(pet_name='kwintus', animal_type='gato' )
describe_pet(animal_type='cachorro', pet_name='petrunus')