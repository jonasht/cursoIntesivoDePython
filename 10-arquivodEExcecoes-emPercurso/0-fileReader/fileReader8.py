# arquivos grandes: um milhão de digitos

arquivoNome = "./pi_million_digits.txt"

with open(arquivoNome) as file_object:
    linhas = file_object.readlines()


string_de_pi = ''

for linha in linhas:
    string_de_pi += linha.strip()
    
print()
print(f'{string_de_pi[:100]}...') # [:***] eh para n abrir tudo porque trava o pc 
print()

aniversario = input('qual o dia do seu aniversario [ddmmaa]: ')
if aniversario in string_de_pi:
    print('seu aniversario aparece nos primeiros milhoes de digitos de pi ')
else:
    print('seu aniversario nao aparece nos primeiros milhoes de digitos de pi')