# um dicionario dentro de um dicionario

user = {
    'albeeins': {
        'first': 'alberto',
        'last': 'einstain',
        'location': 'princeton',
    },
    
    'marcur': {
        'first': 'maria',
        'last': 'curie',
        'location': 'paris'
    }
}
print('----'*10)
for username, user_info in user.items():
    print(f'Username: {username}')
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    
    print('\tfull name: ' + full_name.title())
    print('\tlocation:' + location.title())
print('----'*10)    