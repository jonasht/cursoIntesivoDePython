# escrevendo dados em arquivo vazio

nomeDoAquivo = 'programa.txt'

with open(nomeDoAquivo, 'w') as file_object:
    file_object.write('eu amo programar')
    
