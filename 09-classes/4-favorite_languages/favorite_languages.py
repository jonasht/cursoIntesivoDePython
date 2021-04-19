#biblioteca padrao de python 
from collections import OrderedDict

favorite_laguages = OrderedDict()

favorite_laguages ['jen'] = 'python'
favorite_laguages['jonas'] = 'python'
favorite_laguages['edward'] = 'c'
favorite_laguages['sonia'] = 'lua'
favorite_laguages['roberto'] = 'java'

print('-'*40)


for name, language in favorite_laguages.items():
    print(f'a linguagem de programa de {name.title():.<7}: {language.title()}')