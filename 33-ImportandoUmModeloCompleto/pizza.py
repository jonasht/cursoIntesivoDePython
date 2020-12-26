def fazer_pizza(tamanho, *ingredientes):
    print()
    print('tamanho ' + str(tamanho) + 
          ' da pizza com os ingredientes: ')
    for ingrediente in ingredientes:
        print('-> ' + ingrediente)
    
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    