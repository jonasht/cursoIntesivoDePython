# usando json.dumb() e json.load()

import json
from random import randint

numeros = [randint(0,20) for i in range(6)]
print('numeros aleatorios:')
print(numeros)

nomeArquivo = 'numeros.json'
with open(nomeArquivo, 'w') as arquivo:
    json.dump(numeros, arquivo)


