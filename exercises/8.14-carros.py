print('\n')

def fazer_carro(marca, modelo, **ops):
    
    dicCarro = {'marca': marca, 'modelo': modelo}
    
    for k, v in ops.items():
        dicCarro[k] = v
    
    return dicCarro

infos = fazer_carro('subaru', 'outback', cor='azul')

print(infos)