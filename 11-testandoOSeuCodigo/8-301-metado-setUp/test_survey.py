from survey import anonymousSurvey
import unittest


class testAnonymousSurvey(unittest.TestCase):

    # metado setUp()
    def setUp(self):
        pergunta = 'qual foi o primeiro idioma que voce aprendeu a falar'
        self.minhaPesquisa = anonymousSurvey(pergunta)
        self.respostas = ['English', 'Spanish', 'Mandarin']

    # teste de unica resposta armazenada

    def test_store_single_response(self):
        self.minhaPesquisa.armazenar_resposta(self.respostas[0])
        self.assertIn(self.respostas[0], self.minhaPesquisa.respostas)

    # teste de tres respostas armazenada
    def test_store_three_responses(self):
        for resposta in self.respostas:
            self.minhaPesquisa.armazenar_resposta(resposta)

        for resposta in self.respostas:
            self.assertIn(resposta, self.minhaPesquisa.respostas)


unittest.main()
