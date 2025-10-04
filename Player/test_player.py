import unittest
from Player.player import Player

class TestPlayer(unittest.TestCase):

    def test_color_blanco(self):
        jugador = Player('B')
        self.assertEqual(jugador.obtener_color(), 'B')

    def test_color_negro(self):
        jugador = Player('N')
        self.assertEqual(jugador.obtener_color(), 'N')

if __name__ == '__main__':
    unittest.main()