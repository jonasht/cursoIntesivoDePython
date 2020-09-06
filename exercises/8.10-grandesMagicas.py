def l(): print(30 * '=-' + '=')



    
    

def grandesMagicos(magicos_def):
    for i in range(len(magicos_def)):
        magicos_def[i] = 'grande ' + magicos_def[i]

    print('grandes magicos:')
    for magica in magicos_def:
        print(f'\t{magica.title()}')
    l()
magicos = ['herry', 'mortus', 'facictus', 'luxus', 'medrorius', 'nonpuerestus']

grandesMagicos(magicos[:])