available_toppings = ['mushrooms', 'azeitona', 'pimentao verde',
                      'pepperoni', 'abaxi', 'queijo extra']

requested_toppings = ['cogumelos', 'batata frita', 'queijo extra']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'adicionando {requested_topping}')
    else:
        print(f'desculpe, não temos {requested_topping}')
        
print('\n terminamos de fazer sua pizza')
