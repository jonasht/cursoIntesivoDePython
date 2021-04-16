import unittest
from survey import anonymousSurvey


class testAnonymousSurvey(unittest.TestCase):

    def test_store_single_response(self):

        question = 'qual foi o primeiro idioma que voce aprendeu a falar'
        my_survey = anonymousSurvey(question)
        my_survey.store_response('Ingles')

        self.assertIn('Ingles', my_survey.responses)


unittest.main()
