# falhando silenciosamente

print()

def contarPalavras(nomeDoArquivo):
    try:
        with open(nomeDoArquivo) as f_obj:
            conteudo = f_obj.read()
    except FileNotFoundError:
        # com pass, o programa nao mostrarah que falhou 
        pass
    
    else:
        palavras = conteudo.split()
        num_palavras = len(palavras)
        
        print(f'o arquivo {nomeDoArquivo} tem cerca de {num_palavras} palavras')

        
        
nomeDeArquivos = ['alice.txt', 'little_women.txt', 
                 'moby_dick.txt', 'siddhartha.txt']

for nomeDeArquivo in nomeDeArquivos:
    contarPalavras(nomeDeArquivo)