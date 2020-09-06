# preenchendo um dicionario com dados de entrada do usuario 

responses = {}

polling_active = True

while polling_active:
    name = input('qual é seu nome?\nn: ')
    response = input('qual montanha gostarias de escalar algum dia?\nmontanha: ')
    responses[name] = response
    
    repeat = input('gostarias de deixar outra pessoas responder? Yes/no : ')
    
    if repeat == 'no' or 'n':
        polling_active = False
    
print(f'\n{6*"---"}{"<resultados:>":^5}{6*"---"} ')
for name, response in responses.items():
    print(f'\t{name} gostaria de escalar {response}.')
    

    