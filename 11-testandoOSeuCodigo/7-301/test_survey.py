import unittest
from survey import anonymousSurvey


class testAnonymousSurvey(unittest.TestCase):

    def test_store_single_response(self):

        question = 'qual foi o primeiro idioma que voce aprendeu a falar'
        my_survey = anonymousSurvey(question)
        my_survey.store_response('Ingles')

        self.assertIn('Ingles', my_survey.responses)

    def test_store_three_responses(self):
        question = 'qual foi o primeiro idioma que voce aprendeu a falar'
        my_survey = anonymousSurvey(question)

        responses = ['ingles', 'espanhol', 'chines']

        for respose in responses:
            my_survey.store_response(respose)

        for respose in responses:
            self.assertIn(respose, my_survey.responses)


unittest.main()
