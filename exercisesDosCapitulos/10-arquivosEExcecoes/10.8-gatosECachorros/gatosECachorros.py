nomeArquivos  = 'cats.txt', 'dogs.txt', 'file.txt'
print()

for nomeArquivo in nomeArquivos:
    
    try:
        with open(nomeArquivo) as nomes:
            for nome in nomes:
                print(nome.strip())
    except FileNotFoundError:
        
        print(f'o arquivo {nomeArquivo} não existe')
