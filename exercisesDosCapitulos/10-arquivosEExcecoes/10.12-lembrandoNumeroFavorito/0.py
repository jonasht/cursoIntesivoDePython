import json

nomeArquivo = 'numeroFavorito.json'
#numeroFavorito = '1'
def numeroFavorito():
    try:
        with open(nomeArquivo) as arquivo:
            numeroFavorito = json.load(arquivo)
    except FileNotFoundError:
        numeroFavorito = input('numero favorito: ')
        with open(nomeArquivo, 'w') as arquivo:
            json.dump(numeroFavorito, arquivo)
    else:
        print(f'numero favorito: {numeroFavorito}')

numeroFavorito()
