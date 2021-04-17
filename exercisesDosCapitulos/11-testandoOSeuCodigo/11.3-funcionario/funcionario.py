from employee import Employee
import unittest


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.funcionario = Employee('jonas', 'programas', 65000)

    def test_give_default_raise(self):
        self.funcionario.give_raise()
        self.assertEqual(self.funcionario.salario, 70000)

    def test_give_custom_raise(self):
        self.funcionario.give_raise(10000)
        self.assertEqual(self.funcionario.salario, 75000)


unittest.main()
