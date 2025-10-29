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
    
    def test_nombre_por_defecto_blanco(self):
        """Verifica que el nombre por defecto de blancas sea 'jugador_blanco'."""
        jugador = Player('B')
        self.assertEqual(jugador.obtener_nombre(), 'jugador_blanco')

    def test_nombre_por_defecto_negro(self):
        """Verifica que el nombre por defecto de negras sea 'jugador_negro'."""
        jugador = Player('N')
        self.assertEqual(jugador.obtener_nombre(), 'jugador_negro')

    def test_nombre_personalizado(self):
        """Verifica que se pueda asignar un nombre personalizado."""
        jugador = Player('B', 'Juan')
        self.assertEqual(jugador.obtener_nombre(), 'Juan')

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