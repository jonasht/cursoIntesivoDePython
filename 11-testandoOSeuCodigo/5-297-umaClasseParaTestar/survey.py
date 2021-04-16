class anonmymousServey():

    def __init__(self, pergunta):
        self.pergunta = pergunta
        self.respostas = []

    def mostrar_pergunta(self):
        print(self.pergunta)

    def resposta_armazenada(self, nova_resposta):
        self.respostas.append(nova_resposta)

    def mostrar_resultados(self):
        print('resultados de pesquisa:')
        for resposta in self.respostas:
            print('-' + resposta)
