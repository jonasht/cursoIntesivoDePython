# usando a função com um laço while

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print('\ns para sair\npor favor me diga teu nome:')
    f_name = input('primeiro nome:').strip()
    if f_name == 's': break
    l_name = input('sobrenome:').strip()
    if l_name == 's': break
    
    
    nome_formatado = get_formatted_name(f_name, l_name)
    print(f'olá, {nome_formatado}')
    
    
    