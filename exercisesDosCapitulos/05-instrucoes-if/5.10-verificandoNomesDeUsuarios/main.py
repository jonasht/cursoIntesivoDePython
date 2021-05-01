current_users = ['Jonas', 'felipe', 'admin', 'lucas', 'Mateus']
new_users = ['ana', 'Adao', 'joSe', 'Doli', 'Diego', 'jonas']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'desculpe, nome: {new_user.lower() } nao estah disponivel .')
    else:
        print(f'   otimo, nome: {new_user.lower()} ainda estah disponivel.')
