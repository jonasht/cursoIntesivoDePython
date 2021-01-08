def fazer_sanduiches(*itens):
    print('\nomesfazendo sanduiche')
    
    for item in itens:
        print(f'....colocando {item} ao seu sanduiche')
    print('o sanduiche está pronto')
    
    
fazer_sanduiches('carne assada', 'alface', 'maionese', 'milho')
fazer_sanduiches('carne de peru', 'alface', 'mostarda', 'tomate')
fazer_sanduiches('bife', 'alface', 'ovo', 'maionese')