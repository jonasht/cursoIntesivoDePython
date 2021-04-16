
from name_fuction import get_formatted_name
import unittest


class namesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('jonas', 'teixeira')
        self.assertEqual(formatted_name, 'Jonas Teixeira')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('jonas', 'teixeira', 'h')
        self.assertEqual(formatted_name, 'Jonas H Teixeira')


unittest.main()
