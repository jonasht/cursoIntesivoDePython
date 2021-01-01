def l(): print(30 * '=-' + '=')
magicos = ['herry', 'mortus', 'facictus', 'luxus', 'medrorius', 'nonpuerestus']

m_magicos=[]

def Mostrar_magicos(magicos_def):
    while magicos_def:
        magico = magicos_def.pop()
        m_magicos.append(magico.title())
    return m_magicos

l()
magis = Mostrar_magicos(magicos[:])
for magi in magis:
    print(f'{magi}')