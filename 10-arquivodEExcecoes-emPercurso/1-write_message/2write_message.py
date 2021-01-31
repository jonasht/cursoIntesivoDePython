#concatenando dados em um arquivo

nomeDoArquivo = 'programa.txt'

with open(nomeDoArquivo, 'a') as file_object:
    file_object.write('eu também amo encontrar significado em grande base de dados\n')
    file_object.write('eu amo cirar apps que possam executar num browser\n')
