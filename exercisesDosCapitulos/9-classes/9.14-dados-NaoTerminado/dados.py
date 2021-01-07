from random import randint

def l(): print(f'\n{"-"*35}')

class Die():
    

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

# dados de 6 ( jah estah definido)

d6 = Die()

resultados = []

for roll_num in range(10):
    result = d6.roll_die()
    resultados.append(result)
    
l()
    
print("10 jogadas de dados de 6 lados:")
for resultado in resultados:
    print(f'{resultado} ', end='')

# dados de dez
d10 = Die(sides=10)

resultados = []

for roll_num in range(10):
    result = d10.roll_die()
    resultados.append(result)

l()

print('10 jogadas de dados de dez:')
for resultado in resultados:
    print(f'{resultado} ', end='')
# dados de vinte 
d20 = Die(sides=20)

resultados = []
for roll_num in range(10):
    result = d20.roll_die()
    resultados.append(result)

l()

print('10 jogadas de dados de vinte:')

for resultado in resultados:
    print(f'{resultado} ', end='')
    
l()
