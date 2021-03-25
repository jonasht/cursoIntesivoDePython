import json


def enfeitar():
    print('=-'*30+'=')

def get_numeroFavorito():
    with open('numero.json') as arquivo:
        conteudo = json.load(arquivo)
    return conteudo
enfeitar()
print(f'seu numero favorito é {get_numeroFavorito()}')
enfeitar()
