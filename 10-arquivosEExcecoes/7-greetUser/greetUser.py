# salvando e lendo dados gerados pelo usuario

import json

nomeArquivo = 'username.json'
def l(): print('=-'*30+'=')
l()

with open(nomeArquivo) as arquivo:
    nomeUsuario = json.load(arquivo)
    print(f'bem-vindo de volta {nomeUsuario}')
l()