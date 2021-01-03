from car import EletricCar, Car

meu_carro = Car('volkswagen', 'beetle', 2016)
print(meu_carro.get_descriptive_name())

meu_tesla = EletricCar('tesla', 'modelo s', 2016)
print(meu_tesla.get_descriptive_name())