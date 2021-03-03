# analisando textos

nomeDoArquivo = 'alice.txt'

print()

try:
    with open(nomeDoArquivo) as f_obj:
        conteudo = f_obj.read()
except FileNotFoundError:
    print(f'sorry, the file {nomeDoArquivo} does not exist')
    print(f'desculpe, o arquivo {nomeDoArquivo} não existe')
else:
    palavras = conteudo.split()
    num_palavras = len(palavras)
    print(f'o arquivo {nomeDoArquivo} tem cerca de {num_palavras} palavras')
    