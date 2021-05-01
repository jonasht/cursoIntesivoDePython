usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print('ola admin, gostaria de ver o status de relatorio')
        else:
            print(f'ola {username}, obrigado por fazer login novamente')
else:
    print('nós pricisamos encontrar alguns usuarios')
