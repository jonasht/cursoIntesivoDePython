import colorama 
colorama.init()

r = '\033[31m' # red
b = '\033[34m' # blue
f = '\33[m'
dict = {
    '-English-': '-Portugues-',
    'book': 'livro',
    'pencil': 'lapis',
    'notebook': 'caderno',
    'teacher': 'professor',
    'student': 'aluno'
    
    }

for en, pt in dict.items():
    print(f'{r}\n{en.title():9} ={b}  {pt.title()}')

print(f)