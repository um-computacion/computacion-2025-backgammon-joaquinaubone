"""Tests unitarios para la clase Checker"""

import unittest
from core.checker import Checker

class TestFicha(unittest.TestCase):
    """Contiene los tests para verificar el comportamiento de la clase Checker."""

    def test_color_blanco(self):
        """Verifica que la clase Checker se inicializa correctamente."""
        ficha = Checker('B')
        self.assertEqual(ficha.obtener_color(), 'B')

    def test_color_negro(self):
        """Verifica el correcto funcionamiento del método principal (si aplica)."""
        ficha = Checker('N')
        self.assertEqual(ficha.obtener_color(), 'N')

    def test_repr_blanco(self):
        """Verifica que __repr__ devuelve la representación correcta para blancas."""
        ficha = Checker('B')
        self.assertEqual(repr(ficha), "Checker('B')")

    def test_repr_negro(self):
        """Verifica que __repr__ devuelve la representación correcta para negras."""
        ficha = Checker('N')
        self.assertEqual(repr(ficha), "Checker('N')")
    
    def test_str_blanco(self):
        """Verifica que __str__ devuelve 'X' para fichas blancas."""
        ficha = Checker('B')
        self.assertEqual(str(ficha), 'X')

    def test_str_negro(self):
        """Verifica que __str__ devuelve 'O' para fichas negras."""
        ficha = Checker('N')
        self.assertEqual(str(ficha), 'O')

    


if __name__ == '__main__':
    unittest.main()