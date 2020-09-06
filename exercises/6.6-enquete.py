

pessoas = {
    'amanda': 'cobol',
    'roberta': 'ada',
    'arnaldo': '',
    'jeson': '',
    'kaila': 'agora',
    'rodrigo': 'smalltalk 80'    
}

for pessoa, linguagem in pessoas.items():
    if linguagem == '':
        print(f'{pessoa}, queres participar da enquete?')
    else:
        print(f'{pessoa}, escolheste {linguagem} que é a melhor')
    print('\n')