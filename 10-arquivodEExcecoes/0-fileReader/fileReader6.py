# 

arquivoNome = 'pi_digits.txt'

with open(arquivoNome) as file_object:
    linhas = file_object.readlines()


string_de_pi = ''

for linha in linhas:
    string_de_pi += linha.strip()
    
print()
print(string_de_pi)
print()
    