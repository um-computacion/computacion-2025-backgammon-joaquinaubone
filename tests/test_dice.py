"""Tests unitarios para la clase Dice."""
import unittest
from unittest.mock import patch
from core.dice import Dice

class TestDice(unittest.TestCase):

    def test_inicializacion_valores_vacios(self):
        """Verifica que los dados se inicialicen vacíos."""
        dice = Dice()
        self.assertEqual(dice.obtener_valores(), [])

    """Contiene los tests para verificar el comportamiento de la clase Dice."""
    @patch('random.randint', side_effect=[5, 2])
    def test_tirar_devuelve_dos_valores(self, randint_patched):
        """Verifica que tirar() genere dos valores válidos y diferentes."""
        dice = Dice()
        dice.tirar()
        valores = dice.obtener_valores()
        self.assertEqual(len(valores), 2)
        self.assertEqual(valores[0], 5)
        self.assertEqual(valores[1], 2)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 2)    

    @patch('random.randint', side_effect=[3, 3])
    def test_tirar_valores_dobles(self, mock_randint):
        """Verifica que tirar() pueda generar dobles."""
        dice = Dice()
        dice.tirar()
        valores = dice.obtener_valores()
        self.assertEqual(valores, [3, 3])


if __name__ == '__main__':
    unittest.main()