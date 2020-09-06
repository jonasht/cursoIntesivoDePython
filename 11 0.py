# transferindo itens de uma lista para outra 
unconfirmed_users = ['alice', 'brian', 'jonas', 'bruno']

confirmed_users = []

while unconfirmed_users: # enqndo houver users aqui é True e quando n tiver mais, é False e while break
    current_user = unconfirmed_users.pop()
    print('verificando user ' + current_user.title())
    confirmed_users.append(current_user)
    
print('os user seguintes tem sido confirmados:')
for confirmed_user in confirmed_users:
    print(confirmed_user)
    
    
    
    