nomeDoArquivo = 'guest.txt'

nome = input('qual é teu nome?')


with open(nomeDoArquivo, 'w') as objetoArquivo:
    objetoArquivo.write(f'nome:{nome}.')
    