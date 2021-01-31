nome_arquivo = 't.txt'

print()

with open(nome_arquivo) as a:
    linhas = a.readlines()

for linha in linhas:
    print(f'{linha.rstrip()} = ', end='')
    linha = linha.rstrip()
    print(linha.replace('cachorros', 'gatos'))
print()

nome_arquivo = 'python.txt'

print()

with open(nome_arquivo) as a:
    linhas = a.readlines()

for linha in linhas:
    print(f'{linha.rstrip()} = ', end='')
    linha = linha.rstrip()
    print(linha.replace('Python', 'linguagem C'))
print()