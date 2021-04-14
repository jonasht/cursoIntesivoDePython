from survey import *

pergunta = 'qual idioma voce aprendeu a falar?'
minha_avaliacao = anonmymousServey(pergunta)
# minha_avaliacao = anonymousServey
minha_avaliacao.mostrar_pergunta()
print('enter q para sair')

while True:
    resposta = input('idioma: ')
    if resposta == 'q' or resposta == 's':
        break
    minha_avaliacao.resposta_armazenada(resposta)

print('obrigado por participar da pesquisa!')
minha_avaliacao.mostrar_resultados()

        