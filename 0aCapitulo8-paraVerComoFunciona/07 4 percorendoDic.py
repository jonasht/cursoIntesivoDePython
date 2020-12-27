#percorendo as chaves de um dicionario em ordem usando um laço

linguagens_favoritas = {
    'jonas': 'python...',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'lua',
    'lucas': 'julia',
    'fernando': 'php',
    'Amanda': 'java',
    'carol': 'agora'
}


print('\n')
for nome in sorted(linguagens_favoritas.keys()): 
    print(nome.title() + ', thanks for choosing a best programming language!')