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
    
    def test_obtener_jugador_actual(self):
        jugador = self.game.obtener_jugador_actual()
        self.assertEqual(jugador.obtener_color(), 'B')
    
    def test_verificar_fin_del_juego_false(self):
        self.assertFalse(self.game.verificar_fin_del_juego())


if __name__ == '__main__':
    unittest.main()