# usando exceções para evitar falhas

print('me de tres numeros, e eu os dividirei ')
print('give me two number and I will divide them')
print('s para sair\nenter q to quit ')

while True:
    print('\nfirst number: ')
    primeiro_numero = input('primeiro numero: ')

    if primeiro_numero == 's' or primeiro_numero == 'q':
        break
    print('\nsecond number:')
    segundo_numero = input('segundo numero: ')
    
    if segundo_numero == 's' or segundo_numero == 'q' :
        break
    try:
        resposta = int(primeiro_numero) / int(segundo_numero)
    except ZeroDivisionError:
        print('não podes dividir por zero')
        print('you cannot divide by zero')
    else:
        print(resposta)


    
# vai dar erro se digitar 5 e 0 