import json


nomeArquivo = 'username2.json'
def saudarUsuario():
    try:
        with open(nomeArquivo) as arquivo:
            nomeUsuario = json.load(arquivo)
            

        # nao estah funcionando com FileNotFoundError: 
        # como estah no livro
    except:
        nomeUsuario = input('qual é seu nome:')

        with open(nomeArquivo, 'w') as arquivo:
            json.dump(nomeUsuario, arquivo)
            print(f'nós lembraremos de voce quando voltar {nomeUsuario}')

    else:
        print(f'bem vindo de volta {nomeUsuario}')
        
            
saudarUsuario()