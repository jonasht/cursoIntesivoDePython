nomeDoArquivo = 'guest_book.txt'


while 1:
    
    nome = input('qual é seu nome:')
    print('0 para sair')
    if nome == '0':
        break
    
    with open(nomeDoArquivo, 'a') as book:
        book.write(f'nome: {nome}\n')


with open(nomeDoArquivo) as objeto:
    for linha in objeto:
        print(linha.rstrip())