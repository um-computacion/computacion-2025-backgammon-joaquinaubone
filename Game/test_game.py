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


    def test_hay_movimientos_disponibles_true(self):
        self.assertTrue(self.game.hay_movimientos_disponibles([1, 2]))

    def test_interpretar_tirada_no_doble(self):
        resultado = self.game.interpretar_tirada(3, 5)
        self.assertEqual(resultado, [3, 5])

    def test_interpretar_tirada_doble(self):
        resultado = self.game.interpretar_tirada(4, 4)
        self.assertEqual(resultado, [4, 4, 4, 4])


if __name__ == '__main__':
    unittest.main()