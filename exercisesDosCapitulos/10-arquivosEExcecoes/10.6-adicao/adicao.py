
try:
    numero1 = int(input('numero:'))
    numero2 = int(input('numero 2:'))
    
except ValueError:
    print(f'voce digitou um valor não-numero')
    
else:
    print(f'{numero1} + {numero2} = {numero1+numero2}')
    #print(f'{numero1} * {numero2} = {numero1*numero2}')
    #print(f'{numero1} - {numero2} = {numero1-numero2}')

    