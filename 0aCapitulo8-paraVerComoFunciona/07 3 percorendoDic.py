#percorendo dicionario

linguagens_favoritas = {
    'jonas': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'lua',
}

for nome in linguagens_favoritas.keys(): #keys() eh qnd n precisar trabalhar c todos os valores
    print(nome.title())

print('\n')
for nome in linguagens_favoritas: #keys() eh qnd n precisar trabalhar c todos os valores
    print(nome.title())