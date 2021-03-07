import json

nomeUsuario = input('qual eh teu nome: ')


nomeArquivo = 'username.json'

with open(nomeArquivo, 'w') as arquivo:
    json.dump(nomeUsuario, arquivo)
print(f'armazenado: {nomeUsuario}')
