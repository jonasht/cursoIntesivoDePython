nomeArquivo = 'arquivo.txt'

with open('arquivo.txt') as a:
    conteudo = a.read()


def qtd(qtd):
    print(f'quantidade de "{qtd}":',conteudo.count(qtd))
    
qtd('you')
qtd('are')
qtd('we')
qtd('eat')
qtd('is')