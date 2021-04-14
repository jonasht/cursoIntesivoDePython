from name_fuction0 import *

print('enter q ou s para sair')

while True:
    first = input('\n por favor me de um primeiro nome: ')
    if first == 'q' or first == 's': 
        break
    last = input('por favor, me de um ultimo nome: ')

    if last == 'q' or last == 's': 
        break
    
    formatted_name = get_formatted_name(first, last)
    print(f'\n nome formatado: {formatted_name}')
    