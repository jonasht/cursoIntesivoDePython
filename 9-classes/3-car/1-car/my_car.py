# importanto uma unica classe

from car import Car
print()


meu_novo_carro = Car('audi', 'a4', 2016)
print(meu_novo_carro.get_descriptive_name())

meu_novo_carro.odometer_reading = 23
meu_novo_carro.read_odometer()



