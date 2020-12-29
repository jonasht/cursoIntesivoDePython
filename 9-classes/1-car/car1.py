# definindo um valor default para um atributo 
class Car(): 
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        
        #long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        print(f'esta carro tem {self.odometer_reading} milhas percorridas')
        
    

print()
print('carro:')
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

print(my_new_car.read_odometer())
