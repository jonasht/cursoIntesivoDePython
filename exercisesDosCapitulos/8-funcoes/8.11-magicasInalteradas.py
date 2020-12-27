def l(): print(30 * '=-' + '=')


    
    
def mostrar_magicas(magicas_def):
    print('\n')
    l()
    print('nomes de magicas:')
    l()
    for magica in magicas_def:
        print(f'\t{magica.title()}')
    l()

def grandesMagicas(magicas_def):
    for i in range(len(magicas_def)):
        magicas_def[i] = 'grande ' + magicas_def[i]

    print('grandes magicas:')
    for magica in magicas_def:
        print(f'\t{magica.title()}')
    l()

magicos = ['herry', 'mortus', 'facictus', 'luxus', 'medrorius', 'nonpuerestus']   
    
mostrar_magicas(magicos[:]) # [:] isso serve p q uma funcao ñ modfique uma lista
grandesMagicas(magicos[:])