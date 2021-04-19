# valores default

def describe_pet(pet_name, animal_type='cachorro'):
    
    print(f'\neu tenho um {animal_type.title()}.')
    print(f'o nome do meu {animal_type} eh {pet_name.title()}.')
    
#describe_pet(pet_name='kwintus', animal_type='gato' )
describe_pet(pet_name='petrunus')

describe_pet('petronus')

describe_pet(animal_type='ave', pet_name='pilins')