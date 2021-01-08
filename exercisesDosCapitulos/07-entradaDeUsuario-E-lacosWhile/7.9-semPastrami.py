# 
sandwich_orders = ['atum', 'pastrami','ovo', 'frango','pastrami',  'churiço', 'melão', 'macarão', 'banana', 'pera', 'arroz', 'feijão',
                   'pastrami']


finished_sandwiches = []
for lista in sandwich_orders:
    print(f'lista de pedidos: {lista}')

print('\n desculpe, não temos pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:

    fazendo = sandwich_orders.pop()
    print(f'fazendo seu sanduiche de {fazendo}')
    finished_sandwiches.append(fazendo)

print(finished_sandwiches)
    