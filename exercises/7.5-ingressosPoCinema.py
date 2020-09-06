# ingressos para o cinema
print('\ningressos para o cinema\ndigite s para sair')
while 1:
    idade = input('\ninforme a idade:')
    if idade == 's': break 
    idade = int(idade)    
    if idade <= 3:
        print('o ingresso é de graça')
    elif idade <12:
        print('o ingresso é 10 dolares')
    else:
        print('o ingresso é 15 dolares')