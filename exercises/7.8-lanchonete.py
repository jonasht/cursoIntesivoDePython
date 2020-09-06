# 
sandwich_orders = ['atum', 'ovo', 'frango', 'churiço', 'melão', 'macarão', 'banana', 'pera', 'arroz', 'feijão']


finished_sandwiches = []

while sandwich_orders:

    fazendo = sandwich_orders.pop()
    print(f'fazendo seu sanduiche de {fazendo}')
    finished_sandwiches.append(fazendo)

print(finished_sandwiches)
    