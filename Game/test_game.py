import unittest
from Game.game import Juego


class TestJuego(unittest.TestCase):

    def test_cambiar_turno(self):
        juego = Juego()
        self.assertEqual(juego.turno, 'B')
        juego.cambiar_turno()
        self.assertEqual(juego.turno, 'N')
        juego.cambiar_turno()
        self.assertEqual(juego.turno, 'B')

if __name__ == '__main__':
    unittest.main()