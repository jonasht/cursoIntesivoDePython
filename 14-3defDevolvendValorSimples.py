# devolvendo um valor simples

def get_formatted_name(first_name, last_name):
    full_name = f'\n{first_name} {last_name}'
    return full_name.title()

programmer = get_formatted_name('jonas', 'teixeira')
print(programmer)