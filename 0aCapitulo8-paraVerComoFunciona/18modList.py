# modificando uma lista
unprited_designs = ['iphone', 'robot', 'carrinho']
completed_models = []

print('\n' + 30*'=-'+'=')

while unprited_designs:
    current_designs = unprited_designs.pop()

    print(f'imprimindo modelos {current_designs}')
    completed_models.append(current_designs)

print('\n')
for completed_model in completed_models:
    print(completed_model)