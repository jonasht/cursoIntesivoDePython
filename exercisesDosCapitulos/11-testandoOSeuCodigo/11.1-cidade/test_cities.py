from city_function import funcDeCidade
import unittest


class teste(unittest.TestCase):
    
    def test_city_country(self):
        cidade_pais = funcDeCidade('santiago', 'chile')
        self.assertEqual(cidade_pais, 'Santiago, Chile')
unittest.main()
