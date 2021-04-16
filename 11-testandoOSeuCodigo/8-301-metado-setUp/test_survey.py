from survey import anonymousSurvey
import unittest

class testAnonymousSurvey(unittest.TestCase):
    
    # metado setUp()
    def setUp(self):
        question = 'qual foi o primeiro idioma que voce aprendeu a falar'
        self.my_survey = anonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
        
    
    # teste de unica resposta armazenada
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    # teste de tres respostas armazenada
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
            

unittest.main()
