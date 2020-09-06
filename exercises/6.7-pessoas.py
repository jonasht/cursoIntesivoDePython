def l(): print(30*'¨')
people = []
pessoa_1 = {
    'Nome': 'pitana',
    'sobrenome': 'jango',
    'idade': '20',
    'cidade': 'kalenia'
    }   

pessoa_2 = {
    'Nome': 'Amanda',
    'sobrenome': 'robson',
    'idade': '56',
    'cidade': 'portia'
    }
pessoa_3 = {
    'Nome': 'Dani',
    'sobrenome': 'targuerian',
    'idade': '32',
    'cidade': 'pedra do dragão'
    }

people.append(pessoa_1)
people.append(pessoa_2)
people.append(pessoa_3)  

for i in range(len(people)):
    l()
    print(f'Usuario[{i}]')
    for username, userinfo in people[i].items():
        print(f'{username.title():>10}: {userinfo.title():<10}')