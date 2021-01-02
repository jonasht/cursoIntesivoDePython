# 

def l(): print('=-'*40+'=') # enfeite=-=-=-=-=-=-=-=-

class Car(): 
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        
        #long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        
        long_name = f'Carro:\n  {self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        print(f'    Este carro tem {self.odometer_reading} milhas percorridas')
    
    def update_odometer(self, mileage):
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f'    voce não pode diminuir o odometro com {mileage}, somente maior que {self.odometer_reading}')

    def increment_odometer(self, miles): # somar quantidade do odometro
        self.odometer_reading += miles

class Battery(): 
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f'    Este carro tem uma bateria de {self.battery_size}-kWh ')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 480
        message = f'    Este carro pode andar aproximadamente {range} '
        message += 'milhas em sua carga total'
        print(message)





class EletricCar(Car):
    
    def __init__(self, make, model, year):
        # inicializa os atributos da classe pai
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def fill_gas_tank(self):
        print(f'    Este carro não precisa de tanque de gasolina, eh eletrico')
        

        

print()
