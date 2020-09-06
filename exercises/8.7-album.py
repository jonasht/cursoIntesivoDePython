print('\n')
def l():print(f'{30*"=-"}=')
l()

def make_album(nome, titulo, faixas=''):
    artista = {
        'artista': nome.title(),
        'titulo': titulo.title()
        }
    if faixas:
        artista['faixas'] = faixas
    return artista

a = make_album('jonas', 'algoaqui')
print(a)
a = make_album('mateus', 'vikings')
print(a)
a = make_album('fernando', 'FERs', 8)
print(a)

l()
    
    