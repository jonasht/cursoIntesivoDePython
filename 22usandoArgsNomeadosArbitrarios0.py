# usando argumentos nomeados arbitrarios
print('\n')
def construir_perfil(first, last, **user_info):
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    
    for key, value in user_info.items():
        profile[key] = value.title()

    return profile

user_profile = construir_perfil('alberto', 'unsia',
                                location='são paulo',
                                field='programmer')
print(user_profile)

user_profile = construir_perfil('jonas', 'teixeira', 
                                city = 'mogi guaçu',
                                field = 'programmer')
print(user_profile)