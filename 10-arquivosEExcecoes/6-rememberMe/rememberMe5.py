import json

def get_username_guardado():
    filename = 'username5.json'

    try:
        with open(filename) as arquivo:
            username = json.load(arquivo)
    except FileNotFoundError:
        return None
    
    else:
        return username

def get_novo_username():
    username = input("qual é seu nome: ")
    filename = 'username5.json'

    
    with open(filename, 'w') as arquivo:
        json.dump(username, arquivo)
    return username

def saudar_usuario():
    username = get_username_guardado()
    if username:
        print(f'bem vindo de volta {username}')
        
    else:
        username = get_novo_username()
        print(f'nós lembraremos de voce quando voltar, {username}')
saudar_usuario()
