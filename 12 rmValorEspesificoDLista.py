# removendo todas as intencias de valores especificos de uma lista 

from time import sleep
pets = ['gato','gato', 'cahorro', 'vaca', 'gato', 'coelho', 'cabra', 'cavalo',
         'gato', 'gato', 'gato', 'gato', 'gato',
        ]

def m_pet():
    for pet in pets:
        print(f' {pet}', end='')
        
def l(): print('\n' + 20*'=-'+'=')


l()
while 'gato' in pets:
    pets.remove('gato')
    
    print(' removendo...')
    m_pet()
    sleep(.5)
    
l()
m_pet()