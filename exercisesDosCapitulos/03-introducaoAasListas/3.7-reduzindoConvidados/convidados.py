convidados = [
    'Albert Einstein', 'Carl Sagan', 
    'Charles Darwin', 'Michio Kaku', 
    'Neil Degrasse Tyson', 'Nikola Tesla', 
    'Richard Dawkins', 'Richard Feynman'
]

for nome in convidados:
    print(f'{nome.title()}, te convido para vir almoçar e jantar')

del(convidados[3])

for nome in convidados:
    print(f'{nome.title()}, te convido para vir almoçar e jantar')

convidados.insert(0, 'elisabet')
convidados.insert(2, 'carlos darvino')
convidados.append('ricardo doquins')

for nome in convidados:
    print(f'{nome.title()}, te convido para vir almoçar e jantar')


nome = convidados.pop()
print(f'{nome.title()}, desculpe, não hah mais espaço na mesa')

for nome in convidados:
    print(f'{nome.title()}, te convido para vir almoçar e jantar')
