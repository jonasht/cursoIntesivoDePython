# um teste que passa

from name_fuction import get_formatted_name
import unittest

class namesTestCase(unittest.TestCase):
    
    def test_firstName_lastName(self):
        formatted_name = get_formatted_name('jo', 'teixeira')
        self.assertEqual(formatted_name, 'Jo Teixeira')

unittest.main()

