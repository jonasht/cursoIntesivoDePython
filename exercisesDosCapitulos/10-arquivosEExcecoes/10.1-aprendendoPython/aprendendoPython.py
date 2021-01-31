
# para poder achar o arquivo no ubuntu deve-se escrever no terminal
# code "diretorio" do arquivo para poder funcionar
arquivoDeTexto = 't.txt'

def l(): print('=-'*40+'=')

print()
l()
print('mostrando um arquivo todo de uma so vez com arquivo.read()')
with open(arquivoDeTexto) as arq:
    palavras = arq.read()
    
print(palavras)

l()
print('percorrendo o objeto arquivo com um laço "for" ')
with open(arquivoDeTexto) as arquivo:
    for frase in arquivo:
        print(frase.rstrip())

l()
print('armazendo linhas em uma lista e trabalhando com ela fora do "with" usando um "for"')
with open(arquivoDeTexto) as arquivo:
    linhas = arquivo.readlines()        

for linha in linhas:
    print(linha.rstrip())
l()
    
 
