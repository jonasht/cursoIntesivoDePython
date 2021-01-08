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

print('s para sair\nq to quit')
while True:
    n = sair = input('nome:')
    if sair == 's' or 'q': break
    sair = a = input('album:')
    if sair == 's' or 'q': break   
    sair = f = input('faixa:')
    if sair == 's' or 'q': break   
    mostrar = make_album(n, a, f)
    
    print('artista informação:\n', mostrar)

l()
    
    