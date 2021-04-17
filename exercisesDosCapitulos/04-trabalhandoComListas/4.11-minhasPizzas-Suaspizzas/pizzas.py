pizzas = ['brocolis', 'pepperoni', 'mista']

# fazendo copia/passando para pizzas dos amigos
friend_pizzas = pizzas[:]

# adionando pizza na list() pizzas
pizzas.append('vegetariana')

# adicionando pizza na list() friend_pizzas
friend_pizzas.append('frango')

# mostrando pizzas favoritas:
print('\nminhas pizzas favoritas são:')
for i, pizza in enumerate(pizzas):
    print(f'{i+1} - {pizza} ')

# mostrando pizzas favoritas 
print('\npizzas favoritas do meu amigo sao:')
for i, pizza in enumerate(friend_pizzas):
    print(f'{i+1} - {pizza}')
