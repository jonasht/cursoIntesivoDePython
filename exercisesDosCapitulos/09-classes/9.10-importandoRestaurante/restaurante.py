

class Restaurant(): 
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print('=-'* 20+'=')
        print(f'    restaurante {self.restaurant_name.title()}')
        print(f'    com culinaria {self.cuisine_type.title() }')
        print('=-'* 20+'=')
        
    def open_restaurant(self): 
        print('Restaurante aberto ')

print()

