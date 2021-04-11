idiomas = ['portugues', 'ithkuil', esperanto]
idiomas.append('ingles')

idiomas.insert(0,'latim')

print(idiomas)

frase = 'eu estou aprendendo a falar ' + idiomas[0].title() + ' e sei falar ' + idiomas[3].title()

print(frase)

print(sorted(idiomas))

idioma = idiomas.pop(1)
print('o idioma ' + idioma.title() + ' é falado no brasil')

idiomas.sort()
print(idiomas)

idiomas.remove('ithkuil')
print(idiomas)