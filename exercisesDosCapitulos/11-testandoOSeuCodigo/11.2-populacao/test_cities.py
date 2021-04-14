from city_function import funcDeCidade
import unittest


class teste(unittest.TestCase):
    def test_city_country(self):
        # 1 - desta vez o teste city deve falhar
        # cidade_pais = funcDeCidade('santiago', 'chile', 1000000)

        # 2- funcao populacao opcional
        cidade_pais = funcDeCidade('santiago', 'chile')

        self.assertEqual(cidade_pais, 'Santiago, Chile - 5000000')

    def test_city_country_population(self):
        cidade_pais = funcDeCidade('santiago', 'chile', 5000000)
        self.assertEqual(cidade_pais, 'Santiago, Chile - 5000000')

unittest.main()
