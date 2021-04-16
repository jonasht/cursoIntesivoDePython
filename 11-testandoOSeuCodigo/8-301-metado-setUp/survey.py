

class anonymousSurvey():

    def __init__(self, pergunta):
        self.pergunta = pergunta
        self.respostas = list()

    # mostrar pergunta
    def mostrar_pergunta(self):
        print(self.pergunta)

    # resposta armazenada
    def armazenar_resposta(self, novaResposta):
        self.respostas.append(novaResposta)

    # mostrar resultados
    def mostrar_resultados(self):
        print('resultado de pesquisa:')
        for i, resposta in enumerate(self.respostas):
            print(f'{i+1} - {resposta}')
