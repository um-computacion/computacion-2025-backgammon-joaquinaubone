"""Tests unitarios para la clase Dice."""
import unittest
from unittest.mock import patch
from core.dice import Dice

class TestDice(unittest.TestCase):
    """Contiene los tests para verificar el comportamiento de la clase Dice."""

    def test_inicializacion_valores_vacios(self):
        """Verifica que los dados se inicialicen vacíos."""
        dice = Dice()
        self.assertEqual(dice.obtener_valores(), [])

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
        self.assertEqual(mock_randint.call_count, 2)
    
    @patch('random.randint', side_effect=[1, 2, 5, 6])
    def test_tirar_multiples_veces_sobrescribe(self, mock_randint):
        """Verifica que tirar() sobrescribe los valores anteriores."""
        dice = Dice()

        # Primera tirada
        dice.tirar()
        self.assertEqual(dice.obtener_valores(), [1, 2])

        # Segunda tirada sobrescribe
        dice.tirar()
        self.assertEqual(dice.obtener_valores(), [5, 6])
        self.assertEqual(mock_randint.call_count, 4)

    def test_tirar_genera_valores_en_rango_valido(self):
        """Verifica que tirar() sin mock genera valores entre 1-6."""
        dice = Dice()

        # Tirar múltiples veces para asegurar aleatoriedad
        for _ in range(10):
            dice.tirar()
            valores = dice.obtener_valores()

            # Verificar que hay 2 valores
            self.assertEqual(len(valores), 2)

            # Verificar rango [1, 6]
            for valor in valores:
                self.assertIn(valor, [1, 2, 3, 4, 5, 6])



if __name__ == '__main__':
    unittest.main()