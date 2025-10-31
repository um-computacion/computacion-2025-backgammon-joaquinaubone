"""Tests unitarios para la clase Player."""
import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    """Contiene los tests para verificar el comportamiento de la clase Player."""

    def test_color_blanco(self):
        """Verifica que el jugador blanco tenga el color 'B'."""
        jugador = Player('B')
        self.assertEqual(jugador.obtener_color(), 'B')

    def test_color_negro(self):
        """Verifica que el jugador negro tenga el color 'N'."""
        jugador = Player('N')
        self.assertEqual(jugador.obtener_color(), 'N')
    


    def test_simbolo_blanco(self):
        """Verifica que el símbolo del jugador blanco sea 'X'."""
        jugador = Player('B')
        self.assertEqual(jugador.obtener_simbolo(), 'X')

    def test_simbolo_negro(self):
        """Verifica que el símbolo del jugador negro sea 'O'."""
        jugador = Player('N')
        self.assertEqual(jugador.obtener_simbolo(), 'O')


if __name__ == '__main__':
    unittest.main()