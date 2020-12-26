# usando argumentos nomeados arbitrarios
print('\n')

def l(): print(30* '=-' + '=')

def construir_perfil(first, last, **user_info):
    profile = {}
    
    profile['Nome'] = first.title()
    profile['Sobrenome'] = last.title()
    
    for key, value in user_info.items():
        profile[key.title()] = value.title()

    return profile

def mostrar(infos):
    l()
    print('=-=-=-= Informações: =-=-=-=-=')
    for k, v in infos.items():
        print(f'\t{k:>11}: {v:<5}')
    l()

user_profile = construir_perfil('alberto', 'unsia',
                                localização='são paulo',
                                campo='programador')
mostrar(user_profile)

user_profile = construir_perfil('jonas', 'teixeira', 
                                localização = 'mogi guaçu',
                                campo = 'programador')

user_profile = construir_perfil('felipe', 'adomalae',
                                tipo_De_Sangue = 'O-',
                                localização = 'mogi guaçu',
                                compo = 'barista')
mostrar(user_profile)

