
import json

def set_numeroFavorito(numeroFavorito):
    
    with open('numero.json', 'w') as a:
        json.dump(numeroFavorito, a)
        print(f'numero favorito {numeroFavorito} guardado')

numeroFavorito = input('qual é seu numero favorito:')
set_numeroFavorito(numeroFavorito)