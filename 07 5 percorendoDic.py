#percorendo valores d um dicionario com laço

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
for linguagem in linguagens_favoritas.values():
    print(linguagem.title())
