print('\n')
def build_profile(primeiro, ultimo, **user_info):
    
    profile = {}
    profile['primeiro_nome'] = primeiro
    profile['ultimo_nome'] = ultimo
    
    for key, value in user_info.items(): 
        profile[key] = value
    return profile


infos = build_profile('jonas', 'teixeira', cidade='mogi',
                        idade='18',
                        sexo='masculino',
                        profissão='programador'
                        )

for key, item in infos.items():
    print(f'{key}: {item}')