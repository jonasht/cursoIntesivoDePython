# usando json.dumb() e json.load()

import json

nomeArquivo = 'numbers.json'

with open(nomeArquivo) as arquivo:
    numeros = json.load(arquivo)

print(numeros)