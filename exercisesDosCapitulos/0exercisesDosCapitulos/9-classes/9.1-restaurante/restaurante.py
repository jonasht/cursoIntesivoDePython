

class Restaurant(): 
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self): 
        print(f'o nome do restaurante eh {self.restaurant_name.title()}')
        print(f'o tipo de culinaria eh {self.cuisine_type.title()}')
        
    def open_restaurant(self): 
        print('o restaurante estah aberto ')

print()

# atribuindo
r1 = Restaurant('flores', 'vegetariana')
r2 = Restaurant('carnelia', 'variado')

print(f'o nome do restaurante eh {r1.restaurant_name}')
print(f'com o tipo de culinaria {r1.cuisine_type}')

print(f'o nome do restaurante eh {r2.restaurant_name}')
print(f'com o tipo de culinaria {r2.cuisine_type}')

