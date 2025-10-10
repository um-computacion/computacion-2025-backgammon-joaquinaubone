"""Tests unitarios para la clase Juego."""

import unittest
from game.game import Juego
from board.board import Tablero
from player.player import Player
from dice.dice import Dice


class TestJuego(unittest.TestCase):
    """Pruebas para verificar la lógica principal de la clase Juego."""
    def setUp(self):
        """Configura los objetos necesarios antes de cada test."""            
        self.tablero = Tablero()
        self.dados = Dice()
        self.jugador_blanco = Player('B')
        self.jugador_negro = Player('N')
        self.game = Juego(self.tablero, self.dados, self.jugador_blanco, self.jugador_negro)

    def test_cambiar_turno(self):
        """Verifica que el cambio de turno alterne correctamente entre los jugadores."""
        self.assertEqual(self.game.turno_actual, 'B')
        self.game.cambiar_turno()
        self.assertEqual(self.game.turno_actual, 'N')
        self.game.cambiar_turno()
        self.assertEqual(self.game.turno_actual, 'B')
    
    def test_obtener_jugador_actual(self):
        """Verifica que se obtenga correctamente el jugador del turno actual."""
        jugador = self.game.obtener_jugador_actual()
        self.assertEqual(jugador.obtener_color(), 'B')
    
    def test_verificar_fin_del_juego_false(self):
        """Verifica que el juego no haya terminado al inicio."""
        self.assertFalse(self.game.verificar_fin_del_juego())


    def test_hay_movimientos_disponibles_true(self):
        """Verifica que existan movimientos disponibles válidos."""
        self.assertTrue(self.game.hay_movimientos_disponibles([1, 2]))

    def test_interpretar_tirada_no_doble(self):
        """Verifica que una tirada normal se interprete correctamente."""
        resultado = self.game.interpretar_tirada(3, 5)
        self.assertEqual(resultado, [3, 5])

    def test_interpretar_tirada_doble(self):
        """Verifica que una tirada doble genere cuatro valores iguales."""
        resultado = self.game.interpretar_tirada(4, 4)
        self.assertEqual(resultado, [4, 4, 4, 4])
    
    def test_intentar_jugada_valida(self):
        """Verifica que una jugada válida mueva una ficha correctamente."""
        self.game.intentar_jugada(0, 1)
        self.assertEqual(self.tablero.get_point(1)[-1], 'B')

    def test_intentar_jugada_invalida(self):
        """Verifica que una jugada inválida lance un ValueError."""
        with self.assertRaises(ValueError):
            self.game.intentar_jugada(5, 6)  # no es turno de negras





if __name__ == '__main__':
    unittest.main()