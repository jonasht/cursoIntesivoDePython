# arquivos grandes: um milhão de digitos

arquivoNome = "./pi_million_digits.txt"

with open(arquivoNome) as file_object:
    linhas = file_object.readlines()


string_de_pi = ''

for linha in linhas:
    string_de_pi += linha.strip()
    
print()
print(f'{string_de_pi[:1000]}...') # [:***] eh para n abrir tudo porque trava o pc 
print()
    