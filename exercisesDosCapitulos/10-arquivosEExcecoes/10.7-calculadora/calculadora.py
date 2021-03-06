
while 1:
    
    try:
        
        numero = input('numero:')
        if numero == 's':
            break
        numero1 = int(numero)

        numero = input('numero 2:')
        if numero == 's':
            break
        numero2 = int(numero)
        
    except ValueError:
        print(f'voce digitou um valor não-numero')
        break
        
    else:
        print(f'{numero1} + {numero2} = {numero1+numero2}')
        print(f'{numero1} * {numero2} = {numero1*numero2}')
        print(f'{numero1} - {numero2} = {numero1-numero2}')

        