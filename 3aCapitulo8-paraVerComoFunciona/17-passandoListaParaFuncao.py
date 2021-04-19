# passando lista para função

def  great_users(names):
    for name in names:
        msg = f'hello, {name.title()}!'
        print(msg)

usernames = ['jonas', 'hek', 'luis']
great_users(usernames)
    
    