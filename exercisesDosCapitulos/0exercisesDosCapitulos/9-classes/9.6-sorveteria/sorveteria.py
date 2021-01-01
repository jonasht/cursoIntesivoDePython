

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

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='icecream'):
        super().__init__(name, cuisine_type)
        self.flavors = []
    
    def describe_flavors(self):
        print('sabores: ')
        for flavor in self.flavors:
            print(flavor)
            
            

# atribuindo
#um.describe_restaurant()


um = IceCreamStand('Algo')

um.flavors = ['chocolate', 'limao', 'morango']
um.describe_flavors()


