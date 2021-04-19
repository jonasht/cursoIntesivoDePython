# sobrescrevendo metdodos da classe-pai

def l(): print('=-'*30+'=')
class Car(): 
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        
        #long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        long_name = f'  {self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        print(f'    esta carro tem {self.odometer_reading} milhas percorridas')
    
    def update_odometer(self, mileage):
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f'    voce não pode diminuir o odometro com {mileage}, somente maior que {self.odometer_reading}')

    def increment_odometer(self, miles): # somar quantidade do odometro
        self.odometer_reading += miles
        

class EletricCar(Car):
    
    def __init__(self, make, model, year):
        # inicializa os atributos da classe pai
        super().__init__(make, model, year)
        
        self.battery = 80
        
    def describe_battery(self): # descrição da bateria
        print(f'esta carro tem uma bateria de {self.battery} kWh ')

    def fill_gas_tank(self):
        print(f'este carro não precisa de tanque de gasolina, eh eletrico')
        
    

print()
l()

meu_tesla = EletricCar('tesla', 'model s', 2016)
print(f'carro: {meu_tesla.get_descriptive_name()}')

l()
meu_tesla.describe_battery()
meu_tesla.fill_gas_tank()
l()
