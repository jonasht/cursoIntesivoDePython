# passandoNumeroArbitarioDeArgumentos
def l (): print(20 * '=-'+'=')
def fazer_pizza(*toppings):
    l()
    print('fazendo a pizza as seguintes ingredientes:')
    for topping in toppings:
        print(f'\t - {topping.title()}')
    l()
    print('\n')
    
fazer_pizza('pepperoni')
fazer_pizza('cogumelos', 'pimentao verde', 'queijo extra', 'banana', 'feijao', 'cebola extra')