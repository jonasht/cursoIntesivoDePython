#percorendo dicionario

user = {'username': 'jonas123',
        'nome': 'Jonas',
        'sobrenome': 'Teixeira',
        'email': 'jonas@hotmail.com',
        'senha': '123456'
    }


for key, valor in user.items():
    print('\nkey: ' + key)
    print('valor: ' + valor)

