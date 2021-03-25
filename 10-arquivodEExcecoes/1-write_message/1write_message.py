# escrevendo varias linhas

nomeDoAquivo = 'programa.txt'

with open(nomeDoAquivo, 'w') as file_object:
    file_object.write('eu amo programar\n')
    file_object.write('eu amo criar novos jogos\n')
