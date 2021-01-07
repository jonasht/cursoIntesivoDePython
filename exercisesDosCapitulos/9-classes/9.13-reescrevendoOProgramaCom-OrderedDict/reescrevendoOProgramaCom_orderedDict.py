from collections import OrderedDict
palavras = OrderedDict()


def l(): print(14*'=-'+'=') # enfeite


#dict = {
#    '-English-': '-Portugues-',
#    'book': 'livro',
#    '': '',
#    '': '',
#    '': '',
#    '': ''
#    
#    }

palavras['book'] = 'livro'
palavras['pencil'] = 'lapis'
palavras['pen'] = 'caneta'
palavras['notebook'] = 'caderno'
palavras['teacher'] = 'professor'
palavras['student'] = 'aluno'
palavras['school'] = 'escola'


l()

for palavra, traducao in palavras.items():
    print(f'- {palavra.title():>8} = {traducao.title():<9} {" "*5}-')

l()