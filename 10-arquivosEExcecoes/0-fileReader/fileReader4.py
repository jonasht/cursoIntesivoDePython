# criando uma lista de linhas dum arquivo 

arquivoNome = 'pi_digits.txt'

with open(arquivoNome) as file_object:
    linhas = file_object.readlines()
    
for linha in linhas:
    print(linha.rstrip())