def l(): print(30 * '=-' + '=')
magicos = ['herry', 'mortus', 'facictus', 'luxus', 'medrorius', 'nonpuerestus']

def mostrar_magicos(magicos_def):
    print('\n')
    l()
    print('nomes de magicos')
    l()8.9-magicas
    for magico in magicos_def:
        print(f'{magico.title()}')
    l()

mostrar_magicos(magicos[:]) # isso serve p q uma funcao ñ modfique uma lista
