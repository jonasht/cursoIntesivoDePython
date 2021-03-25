# refatoração

import json


nomeArquivo = 'username4.json'
def get_nomeUsuarioArmazenado():
    try:
        with open(nomeArquivo) as arquivo:
            nomeUsuario = json.load(arquivo)
   
    except FileNotFoundError:
        return None
    else:
        return nomeUsuario
        
def saudarUsuario():

    nomeUsuario = get_nomeUsuarioArmazenado()
    
    if nomeUsuario:        
        print(f'bem vindo de volta {nomeUsuario}')
    else:

        nomeUsuario = input('qual é seu nome:')
        with open(nomeArquivo, 'w') as arquivo:
            json.dump(nomeUsuario, arquivo)
            print(f'nós lembraremos de voce quando voltar {nomeUsuario}')
       
            
saudarUsuario()