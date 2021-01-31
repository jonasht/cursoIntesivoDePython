nomeDoArquivo = 'texto.txt'


while 1:
    
    nome = input('por que voce gosta de programar?:')
    print('0 para sair')
    if nome == '0':
        break
    else:
        with open(nomeDoArquivo, 'a') as book:
            book.write(f'{nome}\n')


with open(nomeDoArquivo) as texto:
    for linha in texto:
        print(linha.rstrip())