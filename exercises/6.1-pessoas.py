# use um dicionario p armazenar informaçoes sobre uma pessoa q conheças
#armazene seu primeiro nome, sobrenome, idade, e cidade. 
# deverá ter as chaves como first_name, last_name, age e city.
# mostre cada informaçao armazenada no dicionario 
import colorama
colorama.init()
r = '\033[31m' # red
b = '\033[34m' # blue
f = '\33[m'

pessoas = {
    'first_name': 'pitana',
    'last_name': 'jhango',
    'age': '20',
    'city': 'kalenia'
}

print(r, '\ndados da pessoas', f)
print(b, '\tprimeiro nome: ' + pessoas['first_name'].title())
print('\tsobrenome: ' + pessoas['last_name'].title())
print('\tidade: ' + pessoas['age'])
print('\tcidade: ' + pessoas['city'].title(), f)

