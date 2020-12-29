# modificando o valor de um atributo com um mehtado

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
    
    def update_odometer(self, mileage):
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f'voce não pode diminuir o hodometro com {mileage} somente maior que {self.odometer_reading}')

    

print()
print('carro:')
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())


my_new_car.read_odometer()
print()
print('valor modificando')
my_new_car.odometer_reading = 20
my_new_car.read_odometer()
print()

print('update do hodometro do carro:')
my_new_car.update_odometer(42)
my_new_car.read_odometer()
print()

print('update do hodometro do carro com um menor valor:')
my_new_car.update_odometer(10)
my_new_car.read_odometer()
