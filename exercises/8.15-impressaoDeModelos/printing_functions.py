# modificando uma lista com def 

def imprimir_modelos(NaoImprimidos_designs, completos_modelos):
    
    while NaoImprimidos_designs:
        current_design = NaoImprimidos_designs.pop()
        
        print(f'imprimindo -> {current_design.title()}')
        completos_modelos.append(current_design.title())
        

def mostrar_completo_modelos(completos_modelos):
    print('os seguintes modelos foram imprimidos:')
    for completo_modelo in completos_modelos:
        print(completo_modelo)


   