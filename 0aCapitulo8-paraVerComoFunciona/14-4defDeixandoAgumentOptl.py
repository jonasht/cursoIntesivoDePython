# deixando o argumento opcional

def get_formatted_name(first_name, last_name, middle_name='' ):
    if middle_name:
        full_name = f'\n{first_name} {middle_name} {last_name}'
    else:
        full_name = f'\n{first_name} {last_name}'
    return full_name.title()

programmer = get_formatted_name('jonas', 'teixeira', 'henrique')
print(programmer)

programmer = get_formatted_name('jonas', 'teixeira')
print(programmer)

