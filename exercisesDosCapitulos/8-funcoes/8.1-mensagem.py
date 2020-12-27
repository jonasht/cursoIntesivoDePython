# mensagem - usando função/def

def display_message(tds):
    for todo in tds:
        print(f'\n{todo.title()}, eu estou aprendendo função neste capitulo')
        print(f'{todo.title()}, I\'m learning function in this chapter\n')
        
todos = ['mateus', 'fernando', 'gabriel', 'caio']

display_message(todos)