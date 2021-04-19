# usando exceções para evitar falhas

from _typeshed import SupportsGetItem


print('me de tres numeros, e eu os dividirei ')
print('give me two number and I will divide them')
print('s para sair\nenter q to quit ')

while True:
    print('first number: ')
    primeiro_numero = input('\nprimeiro numero: ')

    if primeiro_numero == 's' or primeiro_numero == 'q':
        break
    print('second number:')
    segundo_numero = input('\nsegundo numero: ')
    
    if segundo_numero == 's' or segundo_numero == 'q' :
        break
    resposta = int(primeiro_numero) / int(segundo_numero)
    print(resposta)


    
# se digitar 5 e 0 não  mais erro 