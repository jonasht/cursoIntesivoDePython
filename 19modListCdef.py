# modificando uma lista com def 

def imprimir_modelos(NaoImprimidos_designs, completos_modelos):
    
    while NaoImprimidos_designs:
        current_design = NaoImprimidos_designs.pop()
        
        print(f'imprimindo -> {current_design.title()}')
        completos_modelos.append(current_design.title())
        

def mostrar_completo_modelos(completos_modelos):
    l()
    print('os seguintes modelos foram imprimidos:')
    for completo_modelo in completos_modelos:
        print(completo_modelo)

def l():
    print('=-'*15+'=')
NaoImprimidos_designs = ['capinha de celular', 'robot pendent', 'dodecahedron']
completos_modelos = []

print('\n')
l()
imprimir_modelos(NaoImprimidos_designs, completos_modelos)

l()

mostrar_completo_modelos(completos_modelos)
   