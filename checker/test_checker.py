"""Tests unitarios para la clase Checker."""

import unittest
from checker.checker import Ficha

class TestFicha(unittest.TestCase):
    """Contiene los tests para verificar el comportamiento de la clase Checker."""

    def test_color_blanco(self):
        """Verifica que la clase Checker se inicializa correctamente."""
        ficha = Ficha('B')
        self.assertEqual(ficha.obtener_color(), 'B')

    def test_color_negro(self):
        """Verifica el correcto funcionamiento del método principal (si aplica)."""
        ficha = Ficha('N')
        self.assertEqual(ficha.obtener_color(), 'N')


if __name__ == '__main__':
    unittest.main()