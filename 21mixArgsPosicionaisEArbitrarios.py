# misturando argumentos posicionais e arbitrario

def l (): print(30* '=-' + '=')
def fazer_pizza(tamanho, *toppings):
    l()
    print(f'fazendo uma pizza de {tamanho} centimentros com os seguintes ingredientes:')
    for topping in toppings:
        print(f'\t - {topping}')
    l()
    
fazer_pizza(20, 'pepperoni')
fazer_pizza(30, 'pepperoni', 'queijo extra', 'tomate')
fazer_pizza(40, 'cogumelos', 'pimentao verde', 'pimentao amarelo', 'queijo extra', 'cebola extra')