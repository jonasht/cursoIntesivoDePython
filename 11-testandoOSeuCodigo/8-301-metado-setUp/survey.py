

class anonymousSurvey():

    def __init__(self, question):
        self.question = question
        self.responses = []

    # mostrar pergunta
    def show_question(self):
        print(self.question)

    # resposta armazenada
    def store_response(self, new_response):
        self.responses.append(new_response)

    # mostrar resultados
    def show_results(self):
        print('resultado de pesquisa:')
        for response in self.responses:
            print(' - ' + response)
