import unittest
from rudimentarCalculator import OPERACOES, efetua_operacao
class TestCalculadoraRudimentar(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(efetua_operacao(1, 10, 5), 15)

    def test_subtracao(self):
        self.assertEqual(efetua_operacao(2, 10, 5), 5)

    def test_multiplicacao(self):
        self.assertEqual(efetua_operacao(3, 10, 5), 50)

    def test_divisao(self):
        self.assertEqual(efetua_operacao(4, 10, 5), 2)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            efetua_operacao(4, 10, 0)

if __name__ == '__main__':
    unittest.main()