import unittest
from checker.checker import Ficha

class TestFicha(unittest.TestCase):

    def test_color_blanco(self):
        ficha = Ficha('B')
        self.assertEqual(ficha.obtener_color(), 'B')

    def test_color_negro(self):
        ficha = Ficha('N')
        self.assertEqual(ficha.obtener_color(), 'N')


if __name__ == '__main__':
    unittest.main()